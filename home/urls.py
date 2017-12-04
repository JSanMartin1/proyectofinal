from django.conf.urls import url
from . import views
from django.contrib.auth.views import login ,logout
urlpatterns = [
    #url(r'^$', views.home),
    url(r'^signup/',views.signup),
    url(r'^Listing/',views.Listing),
    url(r'^Contact/',views.Contact),
    url(r'^Historial/',views.Historial),
    url(r'^login/$',login,{'template_name':'home/login.html'}),
    url(r'^logout/$',logout,{'template_name':'home/logout.html'}),
    url(r'^$',views.product_list,name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list,name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail,name='product_detail'),

]
