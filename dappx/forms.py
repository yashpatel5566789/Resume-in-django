from django import forms
from django.conf import settings
from dappx.models import UserProfileInfo, Resume
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, NumberInput, DateInput, DateField
from django.forms import modelformset_factory
from tinymce.widgets import TinyMCE
from .models import WorkExperience, Certification,Education
from django.forms import modelformset_factory
from django.forms import BaseModelFormSet

class MyModelFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(MyModelFormSet, self).__init__(*args, **kwargs)
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
        fields = ['name', 'user', 'id', ]
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'For example: Data Scientist or Sales Manager'}),
                   'user': forms.HiddenInput(),
                   'id': forms.HiddenInput(), }
        labels = {'name': 'Resume name'}


class WorkExperienceForm(ModelForm):
    start_date = DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DateInput(format='%d/%m/%Y', attrs={'class': 'date-picker', 'placeholder': 'DD/MM/YYYY'}))
    end_date = DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                         widget=DateInput(format='%d/%m/%Y', attrs={'class': 'date-picker', 'placeholder': 'DD/MM/YYYY'}))

    class Meta:
        model = WorkExperience
        fields = ['position', 'company', 'city', 'start_date', 'end_date', 'achievements', 'resume', ]
        widgets = {'achievements': TinyMCE(attrs={'class': 'objective-box', 'cols': 50, 'rows': 10}),
                   'position': TextInput(attrs={'placeholder': 'For example: Bank Teller'}),
                   'company': TextInput(attrs={'placeholder': 'For example: Bank Central Asia'}),
                   'city': TextInput(attrs={'placeholder': 'For example: Jakarta'}),
                   'resume': forms.HiddenInput(), }


WorkExperienceFormSet = modelformset_factory(WorkExperience, form=WorkExperienceForm, formset=MyModelFormSet, extra=1,
                                             max_num=5)

class CertificationForm(ModelForm):
    date_obtained = DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                              widget=DateInput(format='%d/%m/%Y', attrs={'class': 'date-picker', 'placeholder': 'DD/MM/YYYY'}))

    class Meta:
        model = Certification
        fields = ['name', 'date_obtained', 'city', 'resume', ]
        widgets = {'name': TextInput(attrs={'placeholder': 'For example: Certified Technical Architect'}),
                   'city': TextInput(attrs={'placeholder': 'For example: New York'}),
                   'resume': forms.HiddenInput(), }
        labels = {'name': 'Certification name'}


CertificationFormSet = modelformset_factory(Certification, form=CertificationForm, formset=MyModelFormSet, max_num=5)

class EducationForm(ModelForm):
    start_date = DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                           widget=DateInput(format='%d/%m/%Y', attrs={'class': 'date-picker', 'placeholder': 'DD/MM/YYYY'}))
    end_date = DateField(required=False, input_formats=settings.DATE_INPUT_FORMATS,
                         widget=DateInput(format='%d/%m/%Y', attrs={'class': 'date-picker', 'placeholder': 'DD/MM/YYYY'}))

    class Meta:
        model = Education
        fields = ['school', 'degree', 'major', 'gpa', 'city', 'start_date', 'end_date', 'resume', ]
        widgets = {'school': TextInput(attrs={'placeholder': 'For example: University of San Francisco'}),
                   'degree': TextInput(attrs={'placeholder': 'For example: Bachelor of Science'}),
                   'major': TextInput(attrs={'placeholder': 'For example: Economics'}),
                   'gpa': NumberInput(attrs={'placeholder': 'For example: 3.7'}),
                   'city': TextInput(attrs={'placeholder': 'For example: San Francisco'}),
                   'resume': forms.HiddenInput(), }
        labels = {'gpa': 'GPA'}


EducationFormSet = modelformset_factory(Education, form=EducationForm, formset=MyModelFormSet, max_num=3)