from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
    path('add/', views.WishCreate.as_view(), name='add'),
    path('<int:pk>/delete', views.WishDelete.as_view(), name='delete'),
]