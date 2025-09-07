from django import forms
from .models import *

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = [
            'title', 
            'description', 
            'file', 
            'profile_pic', 
            'name', 
            'email', 
            'phone_number', 
            'address', 
            'linkedin_url', 
            'github_url', 
            'portfolio_url', 
            'education', 
            'experience', 
            'skills'
        ]
    
class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ['username', 'email', 'first_name', 'last_name', 'user_type', 'profile_pic']  
    
    