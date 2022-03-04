from django.urls import path
from .import views
# from notes.views import *

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('nav/', views.navigation, name="navigation"),
    path('login/', views.userlogin, name="login"),
    path('signup/', views.signup1, name="signup"),
    path('login_admin/', views.login_admin, name="login_admin"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('n/', views.nav, name="admin_nav"),
    path('logout/', views.user_logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('change/', views.changepwd, name="changepwd"),
    path('edit/', views.edit, name="edit"),
    path('upload/',views.upload_notes,name="upload_notes"),
    path('view',views.view_mynotes,name="view_mynotes"),
    path('delete/<int:id>',views.delete_mynotes,name="delete"),
    path('view_user',views.view_user,name="view_user"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user"),
    path('pending', views.pending, name="pending"),
    path('assign/<int:id>', views.assign_status, name="assign"),
    path('accept', views.accepted_notes, name="accepted_notes"),
    path('rejected', views.rejected_notes, name="rejected"),
    path('all_notes', views.all_notes, name="all_notes"),
    path('delete_notes/<int:id>',views.delete_notes,name="delete_notes"),
    path('viewallnotes',views.viewallnotes, name="viewallnotes"),

]