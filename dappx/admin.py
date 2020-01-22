from django.contrib import admin
from .models import UserProfileInfo, User
# Register your models here.from django.contrib import admin
from .models import (
    Resume,
    WorkExperience,
    Certification,
    Profile,
    Education,
    Career,
    Project,
    Additional_courses,
    Internship,
    Achievement,
    Hobbies,
)


class EducationAdmin(admin.ModelAdmin):
    search_fields = ['school', ]
    list_display = ['school', 'resume', ]


class ResumeAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ['name', ]
    list_filter = ['created_at', ]
    list_display = ['name', 'user', 'created_at', 'updated_at', ]


class WorkExperienceAdmin(admin.ModelAdmin):
    search_fields = ['position', 'company', ]
    list_display = ['position', 'company', 'resume', ]


class CertificationAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', 'resume', ]


class ProfileAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'name',
        'email',
        # 'address',
        # 'city',
        # 'country',
        'phone_number',
        # 'objective',
        # 'linked_in',
        # 'sub_expires_on',
    )


class CareerAdmin(admin.ModelAdmin):
    fields = [
        'resume',
        'career'

    ]


class ProjectAdmin(admin.ModelAdmin):
    fields = [
        'resume',
        'project_name',
        'description',
        'role',
        'platform',
    ]


class Additional_coursesAdmin(admin.ModelAdmin):
    fields = [
        'resume',
        'course_name',
    ]


class InternshipAdmin(admin.ModelAdmin):
    fields = [
        'resume',
        'company_name',
        'project_name',
        'start_date',
        'end_date',
    ]


class AchievementAdmin(admin.ModelAdmin):
    fields = [
        'resume',
        'achievement'

    ]


class HobbiesAdmin(admin.ModelAdmin):
    fields = [
        'resume',
        'hobbies'

    ]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(UserProfileInfo)
admin.site.register(Career, CareerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Additional_courses, Additional_coursesAdmin)
admin.site.register(Internship, InternshipAdmin)
admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Hobbies, HobbiesAdmin)
