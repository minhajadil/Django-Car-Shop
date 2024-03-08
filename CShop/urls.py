from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('userauth.urls')),
    path('car/', include('cars.urls')),
    path('', views.home,name='homepage'),
    path('brand/<slug:brand_slug>', views.home,name='brandfilter'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
