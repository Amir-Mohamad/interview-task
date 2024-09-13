import pandas as pd
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Titanic
from .forms import TitanicForm

class TitanicUploadView(View):
    def get(self, request):
        return render(request, 'core/upload.html')

    def post(self, request):
        file = request.FILES['file']
        df = pd.read_excel(file)
        for index, row in df.iterrows():
            Titanic.objects.create(**row)
        return redirect('core:index')

class TitanicListView(ListView):
    model = Titanic
    template_name = 'core/index.html'
    context_object_name = 'titanic_data'

class TitanicUpdateView(UpdateView):
    model = Titanic
    form_class = TitanicForm
    template_name = 'core/edit.html'
    success_url = reverse_lazy('core:index')
