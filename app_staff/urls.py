from django.urls import path

from app_staff.views import DetailsView


app_name='staff'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
