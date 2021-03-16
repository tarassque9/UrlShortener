from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('main/', views.MainView.as_view(), name='main'),
    path('detail/<int:id>/', views.DetailView.as_view(), name='detail'),
    path('<str:slug>/', views.urlRedirect, name='redirect')
]
