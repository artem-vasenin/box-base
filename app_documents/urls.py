from django.urls import path

from app_documents.views import DetailsView


app_name='documents'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
