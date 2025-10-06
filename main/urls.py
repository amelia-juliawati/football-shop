from django.urls import path
from main.views import show_main, create_products, show_products, show_xml, show_json, show_xml_by_id, show_json_by_id, register, user_login, user_logout, edit_products, delete_products, add_product_entry_ajax, update_product_entry_ajax, user_login_ajax, register_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-products/', create_products, name='create_products'),
    path('products/<str:id>/', show_products, name='show_products'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:products_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:products_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('register-ajax/', register_ajax, name='register_ajax'),
    path('login/', user_login, name='login'),
    path('login-ajax/', user_login_ajax, name='user_login_ajax'),
    path('logout/', user_logout, name='logout'),
    path('products/<uuid:id>/edit', edit_products, name='edit_products'),
    path('products/<uuid:id>/delete', delete_products, name='delete_products'),
    path('create-product-ajax/', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('update-product-ajax/<uuid:product_id>/', update_product_entry_ajax, name='update_product_entry_ajax'),
]