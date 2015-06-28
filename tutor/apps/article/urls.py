from django.conf.urls import include, url
from tutor.apps.article import views

urlpatterns = [
    url(r'^1/', views.basic_one, name='basic_one'),
    url(r'^2/', views.template_two, name='template_two'),
    url(r'^3/', views.template_three_simple, name='template_three_simple'),
]