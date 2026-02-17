from django.urls import path

from app_contacts.views import DetailsView


app_name='contacts'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
