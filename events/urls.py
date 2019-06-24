from django.urls import path

from events.views import EventList, EventGuests, AllEventsGuests, GuestsDetail, GuestsList, EventDetail, UserListView, \
    UserCreateView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Events API')

urlpatterns = [
    path('events/', EventList.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    path('events/guests/', AllEventsGuests.as_view()),
    path('events/<int:pk>/guests/', EventGuests.as_view()),
    path('guests/', GuestsList.as_view()),
    path('guests/<int:pk>/', GuestsDetail.as_view()),
    path('', schema_view),
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
    path('user/create/', UserCreateView.as_view()),
    path('users/', UserListView.as_view())
]
