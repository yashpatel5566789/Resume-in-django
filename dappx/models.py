from django.db import models
from django_countries.fields import CountryField
from tinymce.models import HTMLField
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

class Resume(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    position = models.CharField(max_length=255, blank=True)
    company = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    achievements = HTMLField(blank=True)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name_plural = "Work Experience"
        ordering = ['-end_date', ]


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
#    job_title = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
#    address = models.CharField(max_length=255, blank=True)
#    address2 = models.CharField(max_length=255, blank=True)
#    city = models.CharField(max_length=255, blank=True)
#   country = CountryField(blank_label='(Select country)', blank=True)
#    linked_in = models.CharField(max_length=255, blank=True)
#    objective = HTMLField(blank=True)
#   sub_expires_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.name

class Certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=255, blank=True)
#    date_obtained = models.DateField(null=True, blank=True)
#    city = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

#    class Meta:
#        ordering = ['-date_obtained', ]

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    exam = models.CharField(max_length=255, blank=True)
    school = models.CharField(max_length=255, blank=True)
    degree = models.CharField(max_length=255, blank=True)
    cgpa = models.FloatField(null=True, blank=True)


    def __str__(self):
        return self.school

    class Meta:
        verbose_name_plural = "Education"
        
class Career(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    career = models.CharField(max_length=5000, blank=True)
    
    
    def __str__(self):
        return self.career

class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    project_name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=5000, blank=True)
    role = models.CharField(max_length=255, blank=True)
    platform = models.CharField(max_length=255, blank=True)

class Additional_courses(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    course_name = models.CharField(max_length=5000, blank=True)

class Internship(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    project_name = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class Achievement(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    achievement = models.CharField(max_length=5000, blank=True)

class Hobbies(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, blank=True)
    hobbies = models.CharField(max_length=5000, blank=True)