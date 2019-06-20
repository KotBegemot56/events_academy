from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from events.models import Event, Guest

from events.serializers import EventSerializer, EventGuestsSerializer, GuestsSerializer, GuestsViewSerializer


class GuestsList(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestsSerializer
    permission_classes = (AllowAny,)


class GuestsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestsViewSerializer
    permission_classes = (AllowAny,)


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)


"""This class equal to the upper"""
# class EventDetail(APIView):
#     def get(self, request, pk):
#         try:
#             event = Event.objects.get(id=pk)
#         except Event.DoesNotExist:
#             return Response(data={"message": "Not found"}, status=404)
#         serializer = EventSerializer(instance=event)
#         return Response(data=serializer.data)
#
#     def delete(self, request, pk):
#         try:
#             event = Event.objects.get(id=pk).delete()
#         except Event.DoesNotExist:
#             return Response(data={"message": "Not found"}, status=404)
#
#         return Response(data={"message": "Object deleted successfully"}, status=204)


# Already have this functionality inside ListCreate Api view
class EventCreate(APIView):
    def post(self, request, pk=None):
        payload = request.data
        serializer = EventSerializer(data=payload)
        if serializer.is_valid():
            event = Event(moderator_id=payload['moderator'],
                          title=payload['title'],
                          description=payload['description'],
                          image_url=payload['image_url'],
                          max_guests_limit=payload['max_guest_limit'],
                          )
            event.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data={'messege': 'invalid'}, status=400)

    def put(self, request, pk):
        payload = request.data
        serializer = EventSerializer(data=payload)

    def delete(self, request, pk):
        try:
            event = Event.objects.get(pk=pk).delete
        except Event.DoesNotExists:
            return Response(data={'messege': 'Not found'}, status=404)

        return Response(data={'messege': 'Object has been deleted successfully'}, status=204)

    def patch(self, request, pk):
        return Response(data={'Hello': 'patch'})


""""Create guest. Already did in class GuestsDetail"""
class GuestCreate(APIView):
    def post(self, request):
        payload = request.data
        serializer = GuestsSerializer(data=payload)
        if serializer.is_valid():
            guest = Guest(first_name=payload['first_name'],
                          last_name=payload['last_name'],
                          email=payload['email'],
                          phone_number=payload['phone_number'],
                          )
            guest.save()
            return Response(data=serializer.data, status=201)
        else:
            return Response(data={'messege': 'invalid'}, status=400)


"""Update guest. Already did in class GuestsDetail"""
class GuestUpdate(APIView):
    def put(self, request, pk):
        payload = request.data
        serializer = GuestsSerializer(data=payload)
        if serializer.is_valid():
            guest = Guest.objects.get(pk=pk)
            guest.first_name = serializer.data["first_name"]
            guest.last_name = serializer.data["last_name"]
            guest.email = serializer.data["email"]
            guest.phone_number = serializer.data["phone_number"]
            guest.save()
            Response(data={'messege': 'Guest has been updated successfully'}, status=204)
        else:
            return Response(data={'messege': 'invalid'}, status=400)


class AllEventsGuests(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Event.objects.all().prefetch_related("guests")
    serializer_class = EventGuestsSerializer


class EventGuests(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = Event.objects.all().prefetch_related("guests")
    serializer_class = EventGuestsSerializer
#
# class UserListView(generics.ListCreateAPIView):
#     queryset = MyUserModel.objects.all()
#     serializer_class = serializers.UserSerializer
