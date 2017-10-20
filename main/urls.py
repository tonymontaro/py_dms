from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as token_views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^roles/?$', views.RoleList.as_view(), name='role_list_create'),
    url(r'^roles/(?P<pk>[0-9]+)/?$', views.RoleDetailsView.as_view(), name='role_details'),
    url(r'^users/?$', views.UserList.as_view(), name='user_list_create'),
    url(r'^users/(?P<pk>[0-9]+)/?$', views.UserDetail.as_view(), name='user_details'),
    url(r'^login/?$', token_views.obtain_auth_token, name='login')
]

urlpatterns = format_suffix_patterns(urlpatterns)
