from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),  
    path('lista_productos/', views.lista_productos, name='lista_productos'),
]
