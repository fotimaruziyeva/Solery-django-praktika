from django.urls import path
from .views import home_view, shopdetails_view, shop_view, blog_view, faq_view, BlogdetailsView, contact_view

urlpatterns = [
    path('', home_view, name='home-page'),
    path('shop/', shop_view, name='shop-page'),
    path('shopdetails/', shopdetails_view, name='shopdetails-page'),
    path('blog/', blog_view, name='blog-page'),
    path('blog/<int:pk>/', BlogdetailsView.as_view(), name='blogdetails-page'),  
    path('faq/', faq_view, name='faq-page'),
    path('contact/', contact_view, name='contact-page'),
]
