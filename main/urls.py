from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^auth', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^roles/?$', views.RoleList.as_view(), name='role_list_create'),
    url(r'^roles/(?P<pk>[0-9]+)/?$',
        views.RoleDetailsView.as_view(),
        name='role_details'),
    url(r'^users/?$',
        views.UserList.as_view(),
        name='user_list_create'),
    url(r'^users/(?P<pk>[0-9]+)/?$',
        views.UserDetail.as_view(),
        name='user_details'),
    url(r'^users/login/?$', obtain_jwt_token, name='login'),
    url(r'^documents/?$',
        views.DocumentList.as_view(),
        name='document_list_create'),
    url(r'^documents/(?P<pk>[0-9]+)/?$',
        views.DocumentDetail.as_view(),
        name='document_details'),
    url(r'^users/(?P<pk>[0-9]+)/documents/?$',
        views.UserDocuments.as_view(),
        name='user_documents'),
    url(r'^api/?$', views.documentation),
    url(r'^.*$', views.index),
]

urlpatterns = format_suffix_patterns(urlpatterns)
