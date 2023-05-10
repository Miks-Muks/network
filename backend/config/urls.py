from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # Urls for app netwokr
    path('', include('network.urls')),

    # Urls for app users
    path('users/', include('users.urls')),
    path('api/', include('api.urls')),


    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Куб administration"
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
