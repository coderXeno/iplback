from django.urls import path
from .views import IpldataListApiView,IplmatcheswondataListApiView,IplmatchesplayedvswonListApiView,IpltopeconomicalbowlersListApiView,IplextrarunsconcededperseasonApiView

urlpatterns = [
    path('ipldata/',IpldataListApiView.as_view()),
    path('iplmatcheswondata/',IplmatcheswondataListApiView.as_view()),
    path('iplmatchesplayedvswon/',IplmatchesplayedvswonListApiView.as_view()),
    path('ipltopeconomicalbowlers/',IpltopeconomicalbowlersListApiView.as_view()),
    path('iplextrarunsconceded/',IplextrarunsconcededperseasonApiView.as_view())
    #path('ipldata/<int:ipl_id>', IpldataDetailApiView.as_view()),
]