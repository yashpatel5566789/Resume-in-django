from django.conf.urls import url
from dappx import views
from .views import EducationView,CareerView,ProjectView, \
    InternshipView,AchievementView,HobbiesView,Additional_coursesView, ProfileView, ResumeView

# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    #url(r'^profile/$',views.profile,name='profile'),
    # url(r'^career/$', views.career, name='career'),
    # url(r'^education/$', views.education, name='education'),
    # url(r'^project/$', views.project, name='project'),
    # url(r'^additional/$', views.additional, name='additional'),
    # url(r'^internship/$', views.internship, name='internship'),
    # url(r'^achievement/$', views.achievement, name='achievement'),
    # url(r'^hobbie/$', views.hobbie, name='hobbie'),

    url(r'^education/$',EducationView.as_view(),name='education'),
    url(r'^career/$',CareerView.as_view(),name='career'),
    url(r'^project/$',ProjectView.as_view(),name='project'),
    url(r'^internship/$',InternshipView.as_view(),name='internship'),
    url(r'^achievement/$',AchievementView.as_view(),name='achievement'),
    url(r'^hobbie/$',HobbiesView.as_view(),name='hobbie'),
    url(r'^additional/$',Additional_coursesView.as_view(),name='additional'),
    url(r'^profile/$',ProfileView.as_view(),name='profile'),
    url(r'^resume/$',ResumeView.as_view(),name='resume'),
]
