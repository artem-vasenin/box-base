from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpRequest

from .forms import ExcursionForm


class DetailsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        form = ExcursionForm()
        ctx = {
            'form': form,
        }
        return render(request, 'contacts/details.html', ctx)



class AddFormView(View):
    """ Контроллер добавления заявки """
    def post(self, request: HttpRequest) -> HttpResponse:
        next_url = request.GET.get('next') or '/'
        form = ExcursionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Заявка успешно добавлена')
        else:
            messages.error(request, 'Заявка не добавлена')

        return redirect(next_url)
