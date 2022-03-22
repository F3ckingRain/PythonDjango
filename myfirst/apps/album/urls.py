from django.urls import path
from . import views
app_name = 'album'

urlpatterns = [
    path('',views.home,name='home'),
    path('album',views.home,name='home'),
    path('album/track/<int:track_id>/',views.track,name='track'),
    path('album/track/<int:track_id>/leave_comment',views.leave_comment,name='leave_comment')

]