from django.urls import path
from usuarios import views

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout, name='sair')
]
