from django.urls import path, include
from . import views
from .views import (ItemDetailView,
                    add_to_cart,
                    OrderSummaryView,
                    remove_from_cart,
                    remove_single_item_from_cart,
                    CheckoutView,
                    PaymentView
                    )

app_name = 'product_urls'


urlpatterns = [
    path('', views.index, name='home-page'),
    path('new', views.new, name='new-page'),
    path('register/', views.registerPage, name='register-page'),
    path('login/', views.loginPage, name='login-page'),
    path('logout/', views.logoutUser, name='logout-page'),
    path('cart/', OrderSummaryView.as_view(), name='cart-page'),
    path('<slug>/', ItemDetailView.as_view(), name='view-page'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-cart-page'),
    path('/checkout/', CheckoutView.as_view(), name='checkout-page'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove_item_from_cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment-page')





]
