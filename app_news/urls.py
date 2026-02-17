from django.urls import path

from app_news.views import DetailsView


app_name='news'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
