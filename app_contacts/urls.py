from django.urls import path

from app_contacts.views import DetailsView, AddFormView


app_name='contacts'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
    path('add-form/', AddFormView.as_view(), name='add-form'),
]
