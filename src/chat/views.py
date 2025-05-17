from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    register_error = request.session.pop("register_error", None)
    return render(request, "chat/index.html", {"register_error": register_error})


@login_required
def room(request, room_name):
    return render(request, "chat/room.html", context={"room_name": room_name})
