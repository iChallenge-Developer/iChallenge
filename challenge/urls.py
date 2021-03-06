from django.urls import path, include
from .views import *
from . import views

app_name = 'challenge'


#TODO
#detail, delete,
urlpatterns = [
    path('', home, name='home'),
    path('list/<str:pk>/', challenge_detail, name='challenge_detail'),
    path('create/', challenge_create, name='challenge_create'),
    path('delete/<str:pk>/', challenge_delete, name='challenge_delete'),
    path('list/', view=challenge_list, name='challenge_list'),
    path('calendar/', view=challenge_calendar, name='challenge_calendar'),
    path('enrollment/<str:pk>', challenge_enrollment, name="challenge_enrollment"),
    path('result_ajax/', ResultAjax.as_view(), name="result_ajax"),
    path('invite/<str:invitation>', challenge_invitation, name="challenge_invitation"),
    path('send/invitation/', InvitationAjax.as_view(), name='InvitationAjax'),
    path('invitation/', invitation_accept, name='invitation_accept'),
    path('invitation/failed/', invitation_failed, name="invitation_failed"),
    path('search/', SearchAjax.as_view(), name="challenge_search"),
]