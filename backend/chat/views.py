from django.views.generic import ListView, View
from django.shortcuts import render
from .models import Room, Message


# Create your views here.


class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'chat/rooms.html'
    paginate_by = 5


class RoomDetailView(View):
    def get(self, request, slug):
        room = Room.objects.get(user=request.user)
        messages = Message.objects.filter(user=request.user)
        return render(request, 'chat/room.html', {'room': room, 'messages': messages})
