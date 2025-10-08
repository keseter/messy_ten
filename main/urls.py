from django.urls import path
from . import views   

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),

  
    path('create-product/', views.create_product, name='create_product'),
    path('product/<uuid:id>/', views.show_product, name='show_product'),
    path('product/<uuid:id>/edit', views.edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', views.delete_product, name='delete_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<uuid:product_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:product_id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('login-ajax/', views.login_ajax, name='login_ajax'),
    path('register-ajax/', views.register_ajax, name='register_ajax'),
    path('logout-ajax/', views.logout_ajax, name='logout_ajax'),
    path('product/add-ajax', views.add_product_ajax, name='add_product_ajax'),
    path('product/<uuid:id>/update-ajax', views.update_product_ajax, name='update_product_ajax'),
    path('product/<uuid:id>/delete-ajax', views.delete_product_ajax, name='delete_product_ajax'),
]
