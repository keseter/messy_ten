from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
import datetime

from main.forms import ProductForm
from main.models import Product


@login_required(login_url='/login')  # Restrict: harus login untuk melihat main
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm': '240123456',
        'name': request.user.username,
        'class': 'PBP A',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url='/login')
def create_product(request):
    # fallback non ajax
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        product_entry = form.save(commit=False)  # 
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)


@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, "product_detail.html", context)


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    #  kalau field created_at sudah ada di DB, sort dari terbaru
    try:
        product_list = Product.objects.all().order_by('-created_at')
    except Exception:
        product_list = Product.objects.all()

    data = [
        {
            'user_id': product.user_id,
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'created_at': getattr(product, 'created_at', None).isoformat()
                          if getattr(product, 'created_at', None) else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'user_id': product.user_id,
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request, "edit_product.html", context)


@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

#ajax

@login_required(login_url='/login')
@csrf_exempt  
@require_POST
def add_product_ajax(request):
    # create product via ajax
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return JsonResponse({
            "ok": True,
            "product": {
                "id": str(product.id),
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "thumbnail": product.thumbnail,
                "category": product.category,
                "is_featured": product.is_featured,
                "user_id": product.user_id,
            }
        }, status=201)
    return JsonResponse({"ok": False, "error": form.errors}, status=400)


@login_required(login_url='/login')
@require_POST
def update_product_ajax(request, id):
    # update product via ajax
    product = get_object_or_404(Product, pk=id, user=request.user)
    form = ProductForm(request.POST, instance=product)
    if form.is_valid():
        product = form.save()
        return JsonResponse({
            "ok": True,
            "product": {
                "id": str(product.id),
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "thumbnail": product.thumbnail,
                "category": product.category,
                "is_featured": product.is_featured,
                "user_id": product.user_id,
            }
        })
    return JsonResponse({"ok": False, "error": form.errors}, status=400)


@login_required(login_url='/login')
@require_POST
def delete_product_ajax(request, id):
    
    product = get_object_or_404(Product, pk=id, user=request.user)
    product.delete()
    return JsonResponse({"ok": True})


#  AUTH AJAX 
@csrf_exempt
@require_POST
def login_ajax(request):
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        resp = JsonResponse({
            "success": True,
            "redirect_url": reverse("main:show_main"),
        })
        resp.set_cookie("last_login", str(datetime.datetime.now()))
        return resp

    errors = []
    for field, msgs in form.errors.get_json_data().items():
        for m in msgs:
            errors.append({"field": field, "message": m["message"]})
    return JsonResponse({"success": False, "errors": errors}, status=400)


@csrf_protect
@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({
            "success": True,
            "redirect_url": reverse("main:login"),
            "message": "Your account has been created.",
        }, status=201)
    # kirimkan error 
    errors = []
    for field, msgs in form.errors.get_json_data().items():
        for m in msgs:
            errors.append({"field": field, "message": m["message"]})
    return JsonResponse({"success": False, "errors": errors}, status=400)


@csrf_exempt
@require_POST
def logout_ajax(request):
    logout(request)
    resp = JsonResponse({"success": True, "redirect_url": reverse("main:login")})
    resp.delete_cookie("last_login")
    return resp
