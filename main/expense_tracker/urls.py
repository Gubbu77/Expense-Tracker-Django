from django.urls import path
from expense_tracker import views

urlpatterns = [
    path('', views.index_view, name= "index"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('index_view', views.index_view, name= "index"),
    path('index/', views.index_view, name= "index"),
    path('add/', views.add_list, name= "add"),
    path('add_list', views.add_list, name= "add_list"),
    path('list/', views.list_view, name= "list_view"),
    path('list_view', views.list_view, name= "list_view"),
    path('delete/<str:pk>', views.del_list, name= "del_list"),
    path('list/delete/<str:pk>', views.del_list, name= "del_list"),
]
