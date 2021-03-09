from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Tag

class IndexView(TemplateView):
    template_name = "myapp/chart.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = Tag.objects.all()
        return context