from django.urls import path
from app1 import views
from core import views
from.views import Home1,Add_student,Delete_student,Editstudent
urlpatterns = [
   # path('', Home.as_view(),name='home'),#
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('home/',Home1.as_view(),name='home1'),
    path('add-student/', Add_student.as_view(),name='add-student'),
    path('delete-student/',Delete_student.as_view(), name='delete-student'),
    path('edit-student/<int:id>',Editstudent.as_view(),name='edit-student'),
    
]
