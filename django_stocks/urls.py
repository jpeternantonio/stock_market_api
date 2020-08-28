from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('stock.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/', include('stock.api.urls', namespace='api')),
]
