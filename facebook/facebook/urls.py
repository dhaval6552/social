from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  # Examples:
                  # url(r'^$', 'facebook.views.home', name='home'),
                  # url(r'^blog/', include('blog.urls')),

                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^', include('Facebookapp.urls')),
                  url(r'^friendship/', include('friendship.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                           document_root=settings.STATIC_ROOT)
