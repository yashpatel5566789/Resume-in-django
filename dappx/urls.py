from django.conf.urls import url
from dappx import views
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^career/$', views.career, name='career'),
    url(r'^education/$', views.education, name='education'),
    url(r'^project/$', views.project, name='project'),
    url(r'^additional/$', views.additional, name='additional'),
    url(r'^internship/$', views.internship, name='internship'),
    url(r'^achievement/$', views.achievement, name='achievement'),
    url(r'^hobbie/$', views.hobbie, name='hobbie'),
]