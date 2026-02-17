from django.urls import path

from app_materials.views import DetailsView


app_name='materials'

urlpatterns = [
    path('', DetailsView.as_view(), name='details'),
]
