from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Album, Track, Text
from django.urls import reverse


def home(request):
    latest_album_list = Track.objects.all()
    return render(request, 'album/list.html', {'latest_album_list': latest_album_list})

def track(request, track_id):
    try:
        a = Track.objects.get(id=track_id)
        b = Text.objects.get(id=track_id)
    except:
        raise Http404('Трек не найден')

    latest_comments = a.comment_set.order_by('-id')[:15]

    return render(request, 'album/track.html', {'track': a, 'text': b, 'latest_comments': latest_comments})


def leave_comment(request, track_id):
    try:
        a = Track.objects.get(id=track_id)
    except:
        raise Http404('Страница не найдена')

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('album:track', args=(a.id)))
