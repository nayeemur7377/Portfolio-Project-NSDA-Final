from django.contrib import admin
from django.urls import path
from Portfolio.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', register_view, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),

    path('home/', home_view, name="home"),
    path("profile/edit/", edit_profile, name="edit_profile"),

    path("resumes/", resume_list_view, name="resume_list"),       
    path('add_resume/', add_resume_view, name="add_resume"),
    path("resume/<int:id>/edit/", edit_resume_view, name="edit_resume"),
    path("resume/<int:id>/", resume_detail_view, name="resume_detail"), 
    path("resume_delete/<int:id>/", resume_delete_view, name="resume_delete"), 

    path('change-password/', change_password_view, name='change_password'),
    path('contact/', contact_page_view, name='contact_page'),
    path('contacts/', contact_list_view, name='contact_list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
