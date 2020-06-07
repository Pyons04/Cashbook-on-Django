from django.views import generic
from .models import UsageMaster
from .forms  import UsageMasterForm
from .models import Usage
from .forms  import UsageForm
import logging
import datetime
import calendar

from django.urls import reverse
from django.shortcuts import render
# Create your views here.

class IndexView(generic.FormView):
    model = UsageMaster
    form_class = UsageMasterForm
    template_name = 'childe.html'
    success_url = '/mainapp'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masters'] = UsageMaster.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class SummaryView(generic.ListView):
    model = UsageMaster
    template_name = 'summary.html'

    def beggining_and_end_of_month(self):
        beggining = datetime.date.today().replace(day=1)

        today = datetime.date.today()
        end_date = calendar.monthrange(today.year, today.month)[1]
        end = datetime.date(today.year, today.month, end_date)

        return [beggining, end]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['masters'] = UsageMaster.objects.all
        context['usages'] = Usage.objects.all
    
        context['date_from'] = self.beggining_and_end_of_month()[0].strftime('%Y-%m-%d') # selfで呼び出し先のインスタンスを指定する。
        context['date_to']   = self.beggining_and_end_of_month()[1].strftime('%Y-%m-%d')
        
        return context
    
    def post(self, request, *args, **kwargs):
        context = {}
        context['date_from'] = datetime.datetime.strptime(request.POST.get('date_from'), '%Y-%m-%d')
        context['date_to']   = datetime.datetime.strptime(request.POST.get('date_to'), '%Y-%m-%d')

        context['masters'] = UsageMaster.objects.all
        context['usages'] = Usage.objects.filter(date__range =(context['date_from'], context['date_to']))

        context['date_from'] = request.POST.get('date_from')
        context['date_to']   = request.POST.get('date_to')

        return render(request, 'summary.html', context)

class UsageView(generic.FormView):
    model = Usage
    form_class = UsageForm
    template_name = 'usage.html'
    success_url = '/mainapp/usage'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usages'] = Usage.objects.all()
        return context

    def form_valid(self, form):
        new_usage = form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)

class UsageUpdateView(generic.UpdateView):
    model = Usage
    template_name = 'usage_edit.html'
    form_class = UsageForm
    success_url = '/mainapp/usage'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class GenreDeleteView(generic.DeleteView):
    model = UsageMaster
    template_name = 'delete.html'
    success_url = '/mainapp/'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args,**kwargs)

class UsageDeleteView(generic.DeleteView):
    model = Usage
    template_name = 'delete.html'
    success_url = '/mainapp/usage'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args,**kwargs)
    
