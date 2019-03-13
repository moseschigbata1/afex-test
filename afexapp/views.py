from django.shortcuts import render, get_object_or_404, redirect
from afexapp.forms import UserForm,UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from afexapp.models import UserProfile, Tasks
# Create your views here.

def index(request):
    # name = User.objects.filter(username=username)
    
    # user = get_object_or_404(User, username__iexact=request.user)
    # # user_status = UserProfile.objects.filter(user=user.pk)
    # task = Tasks.objects.filter(username=user.pk)
    # # task = get_object_or_404(Tasks, username=user.pk)
    # context = {'user': user, 'task':task}
    return render(request,'afex/index.html')

# @login_required
# def login_redirect(request):
#     # username = get_object_or_404(User, username__iexact=username)
#     return HttpResponseRedirect(
#         reverse(profile, kwargs={'username': request.GET.username})) 
      

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def profile(request):

    users = get_object_or_404(User, username__iexact=request.user)
    # user_status = UserProfile.objects.filter(user=user.pk)
    task = Tasks.objects.filter(username=users.pk)
    # task = get_object_or_404(Tasks, username=user.pk)
    context = {'user': users, 'task':task}
    return render(request,'afex/home.html', context)

def save_task(request):
    
    user = request.user
    userid = get_object_or_404(User, pk=user.id)
    
    if request.method == 'POST':
        task = request.POST.get('task')
        description = request.POST.get('description')
        date = request.POST.get('date')
        mymodel = Tasks(username=userid, task=task, description=description, date=date)
        mymodel.save()
        # if mymodel.save():
        return HttpResponseRedirect(reverse('profile'))
     
    return render(request, 'afex/task.html', {}) 

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            # if 'profile_pic' in request.FILES:
            #     print('found it')
            #     profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
      
    return render(request,'afex/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})  

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                # return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))
                return HttpResponseRedirect(reverse('profile'))
                # return HttpResponseRedirect('/%s/'%username)
                
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'afex/login.html', {})                             