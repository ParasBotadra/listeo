from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Homepage(TemplateView):
    """
    This API loads the homepage
    url: /
    """
    def get(self, request, *args, **kwargs):
        self.template_name = 'home/index.html'
        return render(request, self.template_name)
