from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def landing(request):
    # return redirect('login')
    return render(request, 'landing.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully signed up.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

# def login(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username  =form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password')
#         else:
#             messages.error(request, 'Please Enter The correct fields')
#     else:
#         return render(request, 'registration/login.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please enter the correct fields.')
    else:
        form = LoginForm()
        # 
    # messages.success(request, 'You have successfully logged in')
    return render(request, 'registration/login.html', {'form': form})




def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def home(request):
    return render(request, 'pages/home.html')

# def login(request):
#     return render(request, 'registration/login.html')

@login_required
def report(request):
    reports = Report.objects.filter(user=request.user)
    
    context = {
        
        'reports': reports
    }
    # print(reports)
    return render(request, 'pages/reporting.html',context)

@login_required
def registerUnits(request):
    return render(request, 'units/registerUnits.html')

@login_required
def unitsHistory(request):
    return render(request, 'units/unitsHistory.html')

@login_required
def examCard(request):
    return render(request, 'exams/examCard.html')

@login_required
def feesStatement(request):
    return render(request, 'fees/feesStatement.html')

@login_required
def user_profile(request):
    # form = ProfileForm()
    profile = Profile.objects.filter(user=request.user)
    context = {
        # 'user': user,
        'profile': profile
    }
    return render(request, 'profile/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,request.FILES ,instance=request.user.profile)
        # p_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user)
        if u_form.is_valid :
            u_form.save()
            # p_form.save()
            messages.success(request, 'Your account have been successfully edited')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user.profile)
        # p_form = ProfileUpdateForm(instance=request.user)


    context = {
        'u_form': u_form,
        # 'p_form': p_form
    }
    return render(request,'profile/edit_profile.html',context)
@login_required
def events(request):
    return render(request, 'funpage/events.html')