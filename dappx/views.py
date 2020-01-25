from dappx.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from .forms import EducationForm
# from formtools.wizard.views import SessionWizardView
from .forms import (
    ResumeForm,
    WorkExperienceFormSet,
    CertificationFormSet,
    EducationForm,
    CareerForm,
    ProjectForm,
    InternshipForm,
    AchievementForm,
    HobbiesForm,
    Additional_coursesForm,
    ProfileForm,
    # CareerFormSet,
    # EducationFormSet
)
from .models import Education


class EducationView(TemplateView):
    template_name = 'dappx/education.html'

    def get_queryset(self, request):
        qs = Education.objects.all()
        return render(request, self.template_name, {'qs': qs })

    def get(self, request):
        form = EducationForm()
        qs = Education.objects.all()
        args = {'form': form, 'qs': qs}
        return render(request, self.template_name, args)

    def post(self, request):
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #post.resume = request.resume
            post.save()
            #text = form.cleaned_data['exam']
            form = EducationForm()
            return redirect('/dappx/education/')

        args = {'form': form}
        return render(request, self.template_name, args)


def index(request):
    return render(request, 'dappx/index.html')


class ProfileView(TemplateView):
    template_name = 'dappx/profile.html'

    def get(self, request):
        form = ProfileForm()
        # posts = Education.object.all()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.resume = request.resume
            post.save()
            # text = form.cleaned_data['exam']
            form = EducationForm()
            return redirect('/dappx/profile/')

        args = {'form': form}
        return render(request, self.template_name, args)


# def profile(request):
#    return render(request,'dappx/profile.html')


class CareerView(TemplateView):
    template_name = 'dappx/career.html'

    def get(self, request):
        form = CareerForm()
        # posts = Education.object.all()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = CareerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.resume = request.resume
            post.save()
            # text = form.cleaned_data['exam']
            # form = EducationForm()
            return redirect('/dappx/career/')

        args = {'form': form}
        return render(request, self.template_name, args)


# def career(request):
#    return render(request, 'dappx/career.html')


# def education(request):
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

class ProjectView(TemplateView):
    template_name = 'dappx/project.html'

    def get(self, request):
        form = ProjectForm()
        # posts = Education.object.all()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.resume = request.resume
            post.save()
            # text = form.cleaned_data['exam']
            # form = EducationForm()
            return redirect('/dappx/project/')

        args = {'form': form}
        return render(request, self.template_name, args)


# def project(request):
#    return render(request, 'dappx/project.html')
class Additional_coursesView(TemplateView):
    template_name = 'dappx/additional_courses.html'

    def get(self, request):
        form = Additional_coursesForm()
        # posts = Education.object.all()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = Additional_coursesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.resume = request.resume
            post.save()
            # text = form.cleaned_data['exam']
            # form = EducationForm()
            return redirect('/dappx/additional/')

        args = {'form': form}
        return render(request, self.template_name, args)


# def additional(request):
#    return render(request, 'dappx/additional_courses.html')


class InternshipView(TemplateView):
    template_name = 'dappx/internship.html'

    def get(self, request):
        form = InternshipForm()
        # posts = Education.object.all()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = InternshipForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.resume = request.resume
            post.save()
            # text = form.cleaned_data['exam']
            # form = EducationForm()
            return redirect('/dappx/internship/')

        args = {'form': form}
        return render(request, self.template_name, args)


# def internship(request):
#   return render(request, 'dappx/internship.html')

class AchievementView(TemplateView):
    template_name = 'dappx/achievement.html'

    def get(self, request):
        form = AchievementForm()
        # posts = Education.object.all()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = AchievementForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.resume = request.resume
            post.save()
            # text = form.cleaned_data['exam']
            # form = EducationForm()
            return redirect('/dappx/achievement/')

        args = {'form': form}
        return render(request, self.template_name, args)


# def achievement(request):
#    return render(request, 'dappx/achievement.html')
class HobbiesView(TemplateView):
    template_name = 'dappx/hobbie.html'

    def get(self, request):
        form = HobbiesForm()
        # posts = Education.object.all()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HobbiesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # post.resume = request.resume
            post.save()
            # text = form.cleaned_data['exam']
            # form = EducationForm()
            return redirect('/dappx/hobbie/')

        args = {'form': form}
        return render(request, self.template_name, args)


# def achievement(request):
#    return render(request, 'dappx/achievement.html')


def hobbie(request):
    return render(request, 'dappx/hobbie.html')


def my_resumes(request):
    user = request.user
    # resumes = Resume.objects.filter(user=user).order_by('-created_at')
    return render(request, 'dappx/profile.html', {})


FORMS = [('resumes', ResumeForm),
         ('work_experience', WorkExperienceFormSet),
         ('certifications', CertificationFormSet),
         # ('career', CareerFormSet),
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
