from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users//', views.UserDetail.as_view()),
    path('contests/', views.ContestList.as_view()),
    path('contest//', views.ContestDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
