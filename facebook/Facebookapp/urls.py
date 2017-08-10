from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'facebook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^', views.home,name='home'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^register/$', views.register_view, name='register'),
    url(r'^home$',views.home,name='home'),
    # url(r'^profile$',views.profile,name='profile'),
    url(r'^(?P<id>[0-9]+)/$' , views.profile, name='profile'),
    url(r'^edit_profile',views.edit_profile,name='edit_profile')
    #url(r'^logout/$', views.logout, {'template_name': 'logout'}, name='logout'),
    #url(r'^signup/$', views.signup, name='signup'),

]