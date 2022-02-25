from django.urls import re_path

from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^accounts/login/$', views.login, name='login'),
    re_path(r'^accounts/logout$', views.logout, name='logout'),
    re_path(r'^register/$', views.register, name='register'),

    re_path(r'^profile/(?P<username>\w+)$', views.profile, name='profile'),
    re_path(r'^add-product/$', views.addProduct, name='add-product'),
    re_path(r'^search-products/$', views.search, name='search-product'),
    re_path(r'^product-details/(?P<productId>[0-9]+)$', views.productDetails, name='product-detail')
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
