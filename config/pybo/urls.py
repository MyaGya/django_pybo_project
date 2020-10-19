from django.urls import path

from . import views

urlpatterns = [
    path('', views.index), # /pybo/
    path('<int:question_id>/', views.detail),
]