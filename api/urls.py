from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    #user
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    #contests
    path('contests/', views.ContestList.as_view()),
    path('contests/<int:pk>', views.ContestDetail.as_view()),

    #raiting
    #request
    #favorites

]

urlpatterns = format_suffix_patterns(urlpatterns)
