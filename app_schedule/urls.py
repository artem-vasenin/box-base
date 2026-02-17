from django.urls import path

from app_schedule.views import DetailsView


app_name='schedule'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
