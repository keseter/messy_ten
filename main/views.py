from django.shortcuts import render

def show_main(request):
    context = {
        "app_name": "MessyTen",
        "student_name": "Edward Jeremy Worang",  
        "student_class": "C"   
    }
    return render(request, "main.html", context)
