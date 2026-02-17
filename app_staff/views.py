from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

class DetailsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'staff/details.html')
