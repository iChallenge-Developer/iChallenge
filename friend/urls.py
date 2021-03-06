from django.urls import path, include
from .views import *

app_name='friend'

urlpatterns = [
    path('list/', fd_list, name="fd_list"),
    path('create/', fd_create, name="fd_create"),
    path('create/new/<int:pk>', new_fd_create, name="new_fd_create"),
    path('list/detail/<int:pk>', fd_detail, name="fd_detail"),
    path('more/<int:pk>/',fd_more, name="fd_more"),
    path('approve/<int:pk>', fd_approve, name="fd_approve"),
    path('deny/<int:pk>', fd_deny, name="fd_deny"),
    path('delete/<int:pk>', fd_delete, name="fd_delete"),
    path('motivate/', MotivationAjax.as_view(), name="fd_motivate"),
    path('motivate/remove/', MotivationRemoveAjax.as_view(), name="motivation_remove"),
    path('search/', SearchAjax.as_view(), name="fd_search"),
    path('user/search/', SearchUserAjax.as_view(), name="new_friend_search"),
]
