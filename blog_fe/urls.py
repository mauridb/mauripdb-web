from django.conf.urls import url
from blog_be import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_in/', views.sign_in, name='sign-in'),
    url(r'^sign_up/', views.index, name='sign-up')
]
