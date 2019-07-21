import requests
from django.views.generic import ListView, DetailView, TemplateView,CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import BadHeaderError
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import CantactForm
from .models import Contact
from blog.models import Post
from shop.models import Product
from painless.models.mixins import AjaxFormMixin
from painless import mail_templates as mailify
from django.conf import settings
from django.shortcuts import redirect

# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page


class HomeView(TemplateView):
    model = Post
    template_name = 'mysite/landing.html'
    context_object_name = 'post'
    page_name = 'landing'
    paginate_by = 2


    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['latest_posts'] = Post.objects.filter()[:2]
        context['latest_product'] = Product.objects.filter()[:3]
        
        return context


# @method_decorator(cache_page(60*60*24), name ='dispatch')
class ContactView(SuccessMessageMixin, CreateView):
    template_name = 'mysite/contact.html'
    form_class = CantactForm
    model = Contact
    success_url = reverse_lazy('mysite:contact')
    success_message = "پیام شما با موفقیت ثبت شد"
    page_name = 'تماس با ما'
 
    def form_valid(self, form):
        # start Recaptcha Validation
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret':settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response':recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        # end Recaptcha Validation
        if result['success']:
            self.object = form.save(commit = False)
            subject = 'فرم تماس با ما'
            message = 'ممنون از اینکه با ما تماس گرفته اید در اولین فرصت با شما تماس خواهیم گرفت'
            to_mail = form.cleaned_data['email']
            html_msg = mailify.get_html_message('news')
            
            try:
                send_mail(subject, message, 'siyamak1981@gmail.com', [to_mail], html_message=html_msg)
            except BadHeaderError:
                return HttpResponse('error')
            self.object.save()
            
            return super(contactView, self).form_valid(form)

        else:
            messages.warning(self.request, 'لطفا recaptcha را کلیک کنید')
            return redirect('mysite:contact')