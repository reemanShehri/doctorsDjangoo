from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
app_name='accounts'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('search/', views.search_results, name='search_results'),
    path('update_profile/',views.update_profile, name='update_profile'), 
    path('login/',views.user_login, name='login'), 
    path('myprofile/', views.myprofile, name='myprofile'),
    path('logout/', views.logout, name='logout'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('<slug:slug>/', views.doctors_detail, name='doctors_detail'),
   # لازم الslug يكون اخر سطر عشانم يصير ارور 

 
]