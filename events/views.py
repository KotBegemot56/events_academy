from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from events.models import Event, Guest

from events.serializers import EventSerializer, EventGuestsSerializer, GuestsSerializer, GuestsViewSerializer, \
    UserSerializer


class GuestsList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestsSerializer
    permission_classes = (IsAuthenticated,)


class GuestsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestsViewSerializer
    permission_classes = (IsAuthenticated,)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)


class AllEventsGuests(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all().prefetch_related("guests")
    serializer_class = EventGuestsSerializer


class EventGuests(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Event.objects.all().prefetch_related("guests")
    serializer_class = EventGuestsSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
