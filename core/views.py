from django.shortcuts import render
from django.http import HttpResponse
from .models import UrlData, UrlStatistic
import random
import string
from django.shortcuts import redirect
from .forms import UrlForm
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import localtime, now
from django.contrib import messages

class DetailView(View):
    template_name = 'url_detail.html'
    
    def get(self, request, id):
        statistic = UrlStatistic.objects.filter(url_id=id)
        return render(request, self.template_name, context={'statistic': statistic})
        

class MainView(View):
    template_name = 'index.html'
    
    def get(self, request):
        form = UrlForm()
        urls = UrlData.objects.all()
        host = 'http://127.0.0.1:8000/'
        context = {'urls': urls,
                   'form': form,
                   'host': host}
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = UrlForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            try:
                obj = UrlData.objects.get(url=url)
                return redirect('/main')
            except ObjectDoesNotExist:
                slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
                new_url = UrlData(url=url, slug=slug)
                new_url.save()
                return redirect('/main')
        else:
            messages.add_message(request, messages.INFO, 'Form is not valid. Please enter valid URL')
            return redirect('/main')

def urlRedirect(request, slug):
    ip_address = request.META.get('REMOTE_ADDR')
    request_time = localtime(now())
    refferer = request.META.get('HTTP_REFERER')
    obj = UrlData.objects.get(slug=slug)
    obj_stat = UrlStatistic.objects.create(url_id=obj.id, request_time=request_time, ip_address=ip_address, refferer=refferer)
    obj_stat.save()
    data = UrlData.objects.get(slug=slug)
    return redirect(data.url)

