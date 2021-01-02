from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from django.views.generic import View
from accounts.models import Account, Profile, TutionClassDetails, vedio
from .forms import RegistationForm, LoginForm, AccountUpdateForm, ProfileForm, TutionClassForm, VedioForm

def register_view(request):
    if request.method == 'POST':
        form = RegistationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('/')
        else:
            context = {'registration_form' : form}
    else:
        form = RegistationForm()
        context = {'registration_form' : form}
    return render(request, 'register.html', context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    else:
        return render(request, 'logout.html')


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('/')
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'login.html', context)

def updateAccount(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(initial = {
            'email': request.user.email,
            'username': request.user.username,
        })
    context['account_form'] = form
    return render(request, 'account.html', context)
    

class ProfileView(View):
    def get(self, *args, **kwargs):

        profile = Profile.objects.get(user=self.request.user)
        tution_class = TutionClassDetails.objects.filter(user=profile)
        context = {'profile':profile, 'tution_class':tution_class}
        return render(self.request, 'profile.html', context)

class ProfileUpdateView(View):
    def get(self, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        tution_class_details = TutionClassDetails.objects.filter(user = profile)
        single_tution_class = None
        for i in tution_class_details:
            single_tution_class = i
        vedios = vedio.objects.filter(user=profile)
        single_vedio = None
        for i in vedios:
            single_vedio = i
        p_form = ProfileForm(instance=profile)
        t_form = TutionClassForm(instance=single_tution_class)
        v_form = VedioForm(instance=single_vedio)
        context = {'p_form':p_form, 't_form':t_form, 'v_form':v_form}
        return render(self.request, 'profileupdate.html', context)

    def post(self, *args, **kwargs):
        user_instance = self.request.user
        profile_instance = get_object_or_404(Profile, user=user_instance)
        if 'submit_p_form' in self.request.POST:
            p_form = ProfileForm(self.request.POST or None, self.request.FILES or None, instance=user_instance)
            if p_form.is_valid():
                p_form.save()
        if 'submit_t_form' in self.request.POST:
            t_form = TutionClassForm(self.request.POST, instance=profile_instance)
            if t_form.is_valid():
                instance = t_form.save(commit=False)
                instance.save()
        if 'submit_v_form' in self.request.POST:
            v_form = VedioForm(self.request.POST, instance=profile_instance)
            if v_form.is_valid():
                instance = v_form.save(commit=False)
                instance.save()
        return redirect('profile')


        