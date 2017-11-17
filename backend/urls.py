from backend import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^index/$', views.Manager.as_view()),
    url(r'^change/(?P<id>\d+)/$', views.ChangePost.as_view(), name='changepost'),
    url(r'^loginout/$', views.LoginOut.as_view())
]
