
from django.contrib import admin
from django.urls import path
from config.pybo import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pybo/', views.index)
]
