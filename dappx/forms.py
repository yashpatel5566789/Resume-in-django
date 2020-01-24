from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.forms import BaseModelFormSet
from django.forms import ModelForm,TextInput,DateInput,DateField
from django.forms import modelformset_factory
from tinymce.widgets import TinyMCE

from .models import UserProfileInfo,Resume,Education
from .models import WorkExperience,Certification,Career,Project,Additional_courses, \
    Internship,Achievement,Hobbies,Profile


class MyModelFormSet(BaseModelFormSet):
    def __init__(self,*args,**kwargs):
        super(MyModelFormSet,self).__init__(*args,**kwargs)
        for form in self.forms:
            form.empty_permitted = False


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = ['name','user','id',]
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'For example: Data Scientist or Sales Manager'}),
                   'user': forms.HiddenInput(),
                   'id': forms.HiddenInput(),}
        labels = {'name': 'Resume name'}


class WorkExperienceForm(ModelForm):
    start_date = DateField(required=False,input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DateInput(format='%d/%m/%Y',
                                            attrs={'class': 'date-picker','placeholder': 'DD/MM/YYYY'}))
    end_date = DateField(required=False,input_formats=settings.DATE_INPUT_FORMATS,
                         widget=DateInput(format='%d/%m/%Y',
                                          attrs={'class': 'date-picker','placeholder': 'DD/MM/YYYY'}))

    class Meta:
        model = WorkExperience
        fields = ['position','company','city','start_date','end_date','achievements','resume',]
        widgets = {'achievements': TinyMCE(attrs={'class': 'objective-box','cols': 50,'rows': 10}),
                   'position': TextInput(attrs={'placeholder': 'For example: Bank Teller'}),
                   'company': TextInput(attrs={'placeholder': 'For example: Bank Central Asia'}),
                   'city': TextInput(attrs={'placeholder': 'For example: Jakarta'}),
                   'resume': forms.HiddenInput(),}


WorkExperienceFormSet = modelformset_factory(WorkExperience,form=WorkExperienceForm,formset=MyModelFormSet,
                                             extra=1,
                                             max_num=5)


class CertificationForm(ModelForm):
    # date_obtained = DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS, widget=DateInput(
    # format='%d/%m/%Y', attrs={'class': 'date-picker', 'placeholder': 'DD/MM/YYYY'}))

    class Meta:
        model = Certification
        fields = ['name',
                  # 'date_obtained',
                  # 'city',
                  'resume',]
        widgets = {'name': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
                   # 'city': TextInput(attrs={'placeholder': 'For example: New York'}),
                   'resume': forms.HiddenInput(),
                   }
        labels = {'name': 'Certification name'}


CertificationFormSet = modelformset_factory(Certification,form=CertificationForm,formset=MyModelFormSet,max_num=5)


# class EducationForm(ModelForm):
#   
#    class Meta:
#        model = Education
#        fields = ['exam','school', 'degree', 'cgpa','resume', ]
#        widgets = {'school': TextInput(attrs={'placeholder': 'For example: University of San Francisco'}),
#                   'degree': TextInput(attrs={'placeholder': 'For example: Bachelor of Science'}),
#                   'cgpa': NumberInput(attrs={'placeholder': 'For example: 3.7'}),
#                   'resume': forms.HiddenInput(), }
#        labels = {'cgpa': 'CGPA'}
#
#
# EducationFormSet = modelformset_factory(Education, form=EducationForm, formset=MyModelFormSet, max_num=3)
class ProfileForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Profile
        fields = "__all__"
        # fields = ['exam','school', 'degree','cgpa',]


class EducationForm(forms.ModelForm):
    exam = forms.CharField()

    class Meta:
        model = Education
        fields = "__all__"
        # fields = ['exam','school', 'degree','cgpa',]


# class EducationForm(forms.Form):
#    exam = forms.CharField(max_length=100)
#    school = forms.CharField(max_length=100)
#    degree = forms.CharField(max_length=100)
#    cgpa = forms.FloatField()
#
#    def __str__(self):
#        return self.school
#
#    class Meta:
#        verbose_name_plural = "Education"

class CareerForm(forms.ModelForm):
    career = forms.CharField()

    class Meta:
        model = Career
        fields = "__all__"
        # fields = ['exam','school', 'degree','cgpa',]


# class CareerForm(ModelForm):
#    class Meta:
#        model = Career
#        fields = ['career', 'resume', ]
#        widgets = {'career': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
#                   'resume': forms.HiddenInput(), }
#        labels = {'career': 'career name'}
#
#
# CareerFormSet = modelformset_factory(Career, form=CareerForm, formset=MyModelFormSet, max_num=5)


class ProjectForm(forms.ModelForm):
    project_name = forms.CharField()

    class Meta:
        model = Project
        fields = "__all__"
        # fields = ['exam','school', 'degree','cgpa',]


# class ProjectForm(ModelForm):
#    model = Project
#    fields = ['name', 'description', 'role', 'platform', 'resume', ]
#    widgets = {'name': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
#               'description': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
#               'role': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
#               'platform': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
#               'resume': forms.HiddenInput(), }
#    labels = {'name': 'project name'}


# class Additional_coursesForm(ModelForm):
#    model = Additional_courses
#    fields = ['name', 'resume', ]
#    widgets = {'name': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
#               'resume': forms.HiddenInput(), }
#    labels = {'name': 'additional courses name'}


class InternshipForm(forms.ModelForm):
    project_name = forms.CharField()

    class Meta:
        model = Internship
        fields = "__all__"
        # fields = ['exam','school', 'degree','cgpa',]


# class InternshipForm(ModelForm):
#    start_date = DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
#                           widget=DateInput(format='%d/%m/%Y',
#                                            attrs={'class': 'date-picker', 'placeholder': 'DD/MM/YYYY'}))
#    end_date = DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
#                         widget=DateInput(format='%d/%m/%Y',
#                                          attrs={'class': 'date-picker', 'placeholder': 'DD/MM/YYYY'}))
#
#    class Meta:
#        model = Internship
#        fields = ['company_name', 'project_name', 'start_date', 'end_date', 'resume', ]
#        widgets = {
#            'company_name': TextInput(attrs={'placeholder': 'For example: Bank Teller'}),
#            'project_name': TextInput(attrs={'placeholder': 'For example: Bank Central Asia'}),
#            'resume': forms.HiddenInput(), }
#

class AchievementForm(forms.ModelForm):
    achievement = forms.CharField()

    class Meta:
        model = Achievement
        fields = "__all__"
        # fields = ['exam','school', 'degree','cgpa',]


# class AchievementForm(ModelForm):
#    model = Achievement
#    fields = ['achievement', 'resume', ]
#    widgets = {'achievement': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
#               'resume': forms.HiddenInput(), }
#    labels = {'achievement': 'career name'}
#
class HobbiesForm(forms.ModelForm):
    hobbies = forms.CharField()

    class Meta:
        model = Hobbies
        fields = "__all__"
        # fields = ['exam','school', 'degree','cgpa',]


# class HobbiesForm(ModelForm):
#    model = Hobbies
#    fields = ['hobbies', 'resume', ]
#    widgets = {'hobbies': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
#               'resume': forms.HiddenInput(), }
#    labels = {'hobbies': 'career name'}


class Additional_coursesForm(forms.ModelForm):
    course_name = forms.CharField()

    class Meta:
        model = Additional_courses
        fields = "__all__"
        # fields = ['exam','school', 'degree','cgpa',]
