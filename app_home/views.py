from unicodedata import category

from django.views import View
from django.shortcuts import render, Http404
from django.http import HttpResponse, HttpRequest

from .models import Page


class DetailsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        page = Page.objects.filter(category__slug='home').first()

        ctx = {
            'page': page or None,
        }

        return render(request, 'home/details.html', ctx)
