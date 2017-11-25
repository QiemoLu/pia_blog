from backend import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^index/$', views.Manager.as_view()),
    url(r'^loginout/$', views.LoginOut.as_view()),
    url(r'^post/add/$', views.PostAdd.as_view()),
    url(r'^post/delete/(\d+)/$', views.delete_post, name="delete_post"),

    url(r'^category/delete/(\d+)/$', views.delete_category, name="delete_category"),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/add$', views.CategoryAdd.as_view()),
    url(r'^category/change/(?P<id>\d+)/$', views.CategoryChange.as_view(),
        name='category_change'),
    url(r'^change/(?P<id>\d+)/$', views.ChangePost.as_view(),
        name='changepost'),
    url(r'^aboutme/$', views.AboutMe.as_view(), name='aboutme')
]
