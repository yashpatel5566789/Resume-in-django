from dappx.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render , redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import EducationForm
# from formtools.wizard.views import SessionWizardView
from .forms import (
    ResumeForm,
    WorkExperienceFormSet,
    CertificationFormSet,
    EducationForm,
    CareerFormSet,
    # EducationFormSet
)

class EducationView(TemplateView):
    template_name = 'dappx/education.html'

    def get(self, request):
        form = EducationForm()
        # posts = Education.object.all()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.resume = request.resume
            post.save()
            text = form.cleaned_data['exam']
            form = EducationForm()
            return redirect('/dappx/edu/')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)


def index(request):
    return render(request, 'dappx/index.html')


def profile(request):
    return render(request, 'dappx/profile.html')


def career(request):
    return render(request, 'dappx/career.html')


#def education(request):
#    if request.method == 'POST':
#        form = EducationForm(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('/profile/')
#
#        else:
#            form = EducationForm()
#            form.save()
#
#    return render(request, 'dappx/education.html', {})
#
#    # return render(request,'dappx/education.html')


def project(request):
    return render(request, 'dappx/project.html')


def additional(request):
    return render(request, 'dappx/additional_courses.html')


def internship(request):
    return render(request, 'dappx/internship.html')


def achievement(request):
    return render(request, 'dappx/achievement.html')


def hobbie(request):
    return render(request, 'dappx/hobbie.html')


def my_resumes(request):
    user = request.user
    # resumes = Resume.objects.filter(user=user).order_by('-created_at')
    return render(request, 'dappx/profile.html', {})


FORMS = [('resumes', ResumeForm),
         ('work_experience', WorkExperienceFormSet),
         ('certifications', CertificationFormSet),
         ('career', CareerFormSet),
         # ('education', EducationFormSet),
         ]
FORM_TYPES = ('work_experience', 'certifications', 'education', 'career',)
TEMPLATES = {'resumes': 'dappx/profile.html',
             'work_experience': 'dappx/education.html',
             'certifications': 'dappx/additional.html',
             'education': 'dappx/education.html',
             'career': 'dappx/career.html',
             'project': 'dappx/project.html',
             'addtional_courses': 'dappx/additional.html',
             'internship': 'dappx/internship.html',
             'achievement': 'dappx/achievement.html'
             }


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'dappx/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'dappx/login.html', {})

# def get_name(request):
#    if request.method == 'POST':
#        form = EducationForm(request.POST)
#        if form.is_valid():
#            return HttpResponseRedirect('/profile/')
#
#        else:
#            form = EducationForm()
#            form.save()
#
#        return render(request, 'education.html',{'form':form})
