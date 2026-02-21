from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest

from .forms import ExcursionForm


class DetailsView(View):
    """ EndPoint показа страницы контакта """
    def get(self, request: HttpRequest) -> HttpResponse:
        form = ExcursionForm()
        ctx = {
            'form': form,
        }
        return render(request, 'contacts/details.html', ctx)

    """ EndPoint добавления заявки """
    def post(self, request: HttpRequest) -> HttpResponse:
        form = ExcursionForm(request.POST)

        if form.is_valid():
            form.save()
            print('valid')
            messages.success(request, 'Заявка успешно добавлена')
        else:
            messages.error(request, 'Заявка не добавлена')
            print(form.errors)

        return render(request, 'contacts/details.html', {'form': form})
