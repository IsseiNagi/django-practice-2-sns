from django.contrib import admin
from django.urls import path, include
# mediaのセッティングを行うために。
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snsapp.urls'))
    # settingsで指定したMEDIA_URLが呼ばれたら、settingsで指定したMEDIA_ROOTを見にいけという指定
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# settingsで指定したSTATIC_URLが呼ばれたら、settingsで指定したSTATIC_ROOTを見にいけという指定
