from django.urls import path
from . import views

urlpatterns = [
    path('Manager/',views.manager,name = 'manager'),
    path('Employer/',views.employer,name='employer'),
    path('Team-leader/',views.teamleader,name='tlhome'),
    path('Team-leaderuploadpage/',views.teamworkfilepage,name='tlworkfilesupl'),
    path('edit/<str:pk>/',views.edit,name='edit'),
    path('edit1/<str:pk>/',views.edit1,name='edit1'),
    path('update1/<int:pk>/', views.update1, name='update1'),
    path('update/<int:pk>/', views.update, name='update'),

    path('files/',views.files , name = 'files'),
    path('register/', views.registerpage, name='register'),
    path('', views.loginpage, name='login-page'),
    path('logout/', views.logoutuser, name='logout-page'),
]