from django.db import models

from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    
    USER=[
        ('Admin','Admin'),
        ('viewer','Viewer')
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    profile_pic = models.ImageField(upload_to="Media/Profile_Pics", null=True, blank=True)
    
    def __str__(self):  
        
        return f"{self.user_type}-{self.username}"
    

class ResumeModel(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_pics/", null=True, blank=True)
    
    file = models.FileField(upload_to='resumes/', blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    portfolio_url = models.URLField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or 'Untitled'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    
    