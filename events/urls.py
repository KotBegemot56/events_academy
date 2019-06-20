from django.urls import path

from events.views import EventList, EventCreate, EventGuests, AllEventsGuests, GuestsDetail, GuestsList, EventDetail, \
    GuestCreate, GuestUpdate

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('events/', EventList.as_view()),
    path('events/create/', EventCreate.as_view()),
    path('events/<int:pk>/', EventDetail.as_view()),
    path('events/guests/', AllEventsGuests.as_view()),
    path('events/<int:pk>/guests/', EventGuests.as_view()),
    path('guests/', GuestsList.as_view()),
    path('guests/<int:pk>/', GuestsDetail.as_view()),
    path('guests/create/', GuestCreate.as_view()),
    path('guests/update/<int:pk>/', GuestUpdate.as_view()),
    path('', schema_view)
]
