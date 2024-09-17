from django.contrib import admin
from django.urls import path, include
from .views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="top"),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('imageupload/', include('app_imageupload.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
