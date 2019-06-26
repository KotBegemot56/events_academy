from django.urls import path
from events.views import EventList, EventGuests, AllEventsGuests, GuestsDetail, GuestsListView, EventDetail
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Events API')

urlpatterns = [
    path('events/', EventList.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    path('events/guests/', AllEventsGuests.as_view()),
    path('events/<int:pk>/guests/', EventGuests.as_view()),
    path('guests/', GuestsListView.as_view()),
    path('guests/<int:pk>/', GuestsDetail.as_view()),
    path('', schema_view),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
