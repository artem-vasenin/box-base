from django.urls import path

from app_home.views import DetailsView


app_name='home'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
