from django.contrib import admin
from dappx.models import UserProfileInfo, User
# Register your models here.from django.contrib import admin
from .models import (
Resume,
WorkExperience,
Certification,
Profile,
Education,
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
        'address',
        'city',
        'country',
        'phone_number',
        'objective',
        'linked_in',
        'sub_expires_on',
    ) 

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(WorkExperience, WorkExperienceAdmin) 
admin.site.register(Certification, CertificationAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(UserProfileInfo)