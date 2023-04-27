from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #user
    path('users/', views.UserListView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),
    #contests
    path('contests/', views.ContestListView.as_view()),
    path('contests/<int:pk>', views.ContestDetailView.as_view()),

    #raiting
    #request
    #favorites

]

urlpatterns = format_suffix_patterns(urlpatterns)
