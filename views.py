from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profiles, UserCreationForm,UpdateUserForm
from django.contrib import messages 
from .forms import Login_Form,userCreationForms,UpdateProfileForm
from django import forms
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, get_object_or_404

from .models import Profiles

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.shortcuts import render


def doctors_detail(request, slug):
   
    doctors_detail = get_object_or_404(Profiles, slug=slug)
    return render(request, 'user/doctors_detail.html', {
        'doctors_detail': doctors_detail,
    })



@login_required
def myprofile(request):
   try:
       profile = Profiles.objects.get(user=request.user)
   except Profiles.DoesNotExist: 
       profile = None
   return render(request, 'user/myprofile.html',
                  {'profile': profile})

def doctor_list(request):
    doctors=Profiles.objects.all()

    return render(request,'user/doctor_list.html',{

        'doctors': doctors,

    })


def user_login(request):
    if request.method=='POST':
      print('f')
      form =Login_Form()
      username=request.POST['username']
      password=request.POST['password']
      user=authenticate(request, username=username, password=password)
      
      if user is not None:
          print('s')

          login(request, user)
          return redirect('accounts:doctor_list')
      else:
          print('t')

          messages.error(request, 'Invalid username or password') 
          return render(request, 'user/login.html', {'form': form})
    else:
         print('l')

         form =Login_Form()
    return render(request, 'user/login.html', {
        'form': form,
      })





def logout(request):
   
    return render(request, 'user/logout.html', {
      
    })
 



class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label=_("الاسم الأول"), max_length=50)
    last_name = forms.CharField(label=_("الاسم الأخير"), max_length=50)
    email = forms.EmailField(label=_("البريد الإلكتروني"), max_length=254)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')


def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST,request.FILES, instance=request.user.profiles)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:myprofile')  # 
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profiles)
    
    return render(request, 'user/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })






def signup(request):
    if request.method == 'POST':
        form = userCreationForms(request.POST)
        if form.is_valid():
             form.save()
             username=form.cleaned_data.get('username')
             passsword=form.cleaned_data.get('password')
             user=authenticate(request, username=username , passsword=passsword)

             login(request,user)
             return redirect('accounts:doctor_list')

    else:
        form = userCreationForms()

    return render(request, 'user/signup.html', {'form': form})





def search_results(request):
    doctor_name = request.GET.get('doctor_name')
    location = request.GET.get('location')
    specialization = request.GET.get('specialization')

    results = Profiles.objects.all()

    if doctor_name:
        results = results.filter(name__icontains=doctor_name)
    if location:
        results = results.filter(address__icontains=location)
    if specialization:
        results = results.filter(Specialist_doctor__icontains=specialization)

    context = {
        'results': results,
        'doctor_name': doctor_name,
        'location': location,
        'specialization': specialization
    }
    return render(request, 'user/search_results.html', context)
