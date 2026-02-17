from django.urls import path

from app_photo.views import DetailsView


app_name='photo'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
