from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

    path('login/', views.loginpage, name='login'),
    path('register/', views.registerpage, name='register'),
    path('logout/', views.logoutpage, name='logout'),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"), name="reset_password"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),
         name="password_reset_confirm"),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
         name="password_reset_complete"),
]
