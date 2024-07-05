from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class CofeeView(TemplateView):
    template_name = 'cofee.html'

class CoffeesView(TemplateView):
    template_name = 'coffees.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
