from django.urls import path
from techuser import views

app_name = "tech_user"

urlpatterns = [
    path('', views.ownprofile, name='ownprofile'),
    path('authorprofile/<username>', views.authorprofile, name='authorprofile'),
    path('registration/', views.registrationview, name='registration'),
    path('login/', views.loginview, name='login'),
    path('logouturl/', views.logoutview, name='logouturl'),
    path('user-settings/', views.settingsview, name='user-settings'),
    path('basic-settings/', views.basicsetting, name='basic-settings'),
    path('other-settings/', views.othersetting, name='other-settings'),
    path('profilepic-settings/', views.addprofilepic, name='profilepic-settings'),
    path('passchange/', views.changepass, name='passchange'),
]
