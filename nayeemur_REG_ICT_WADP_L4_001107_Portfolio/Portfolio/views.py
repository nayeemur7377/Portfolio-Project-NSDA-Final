from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from Portfolio.forms import *
from django.shortcuts import  get_object_or_404
from django.contrib.auth import update_session_auth_hash


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if CustomUserModel.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = CustomUserModel.objects.create_user(
            username=username,
            email=email,
            password=password1,
        )
        messages.success(request, "Registration successful. Please login.")
        return redirect('login')
    return render(request, "register.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, "login.html")



def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def change_password_view(request):
    if request.method == "POST":
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not request.user.check_password(current_password):
            messages.error(request, "Current password is incorrect.")
            return redirect("change_password")

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return redirect("change_password")

        request.user.set_password(new_password)
        request.user.save()
        update_session_auth_hash(request, request.user)  
        messages.success(request, "Password updated successfully.")
        return redirect("home")
    return render(request, "change_password.html")



def home_view(request):
    return render(request, 'home.html')



@login_required
def add_resume_view(request):
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home') 
    else:
        form = ResumeForm()
    context={
            'form':form
        }  
    return render(request,"add_resume.html",context)


@login_required
def resume_list_view(request):
    data=ResumeModel.objects.all() 
    context={
        'data':data,
    }
    return render(request,"resume_list.html",context)

@login_required
def resume_detail_view(request,id):
    resume=ResumeModel.objects.get(id=id)
    return render(request,"view_resume.html",{'resume':resume})

@login_required
def edit_resume_view(request, id):
    resume = get_object_or_404(ResumeModel, id=id)

    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return redirect("resume_list")  
    else:
        form = ResumeForm(instance=resume)

    return render(request, "edit_resume.html", {"form": form})


@login_required
def resume_delete_view(request,id):
    resume=ResumeModel.objects.get(id=id).delete()
    return redirect("resume_list")


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserEditForm(request.POST, request.FILES, instance=request.user)  
        if form.is_valid():
            form.save()
            return redirect("home")  
    else:
        form = UserEditForm(instance=request.user)
    return render(request, "edit_profile.html", {"form": form})

@login_required
def contact_page_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

       
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact_page')  

    return render(request, "contact_page.html")


@login_required
def contact_list_view(request):
    messages = ContactMessage.objects.all().order_by("-created_at")
    return render(request, "contact_list.html", {"messages": messages })