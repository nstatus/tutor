from django.conf.urls import include, url
from tutor.apps.loginsys import views

urlpatterns = [
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
]
