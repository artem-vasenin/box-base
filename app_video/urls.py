from django.urls import path

from app_video.views import DetailsView


app_name='video'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
