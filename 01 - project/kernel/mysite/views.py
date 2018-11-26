from django.views.generic import ListView, DetailView, TemplateView


from blog.models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/products.html'
    context_object_name = 'latest_posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/product.html'
    context_object_name = 'post'

class HomeView(TemplateView):
    template_name = 'mysite/landing.html'
    page_name = 'landing'

# Create your views here.
# class HomeView(View):
#     def get(self, request):
#         return HttpResponse('Hello Generic View')
    
#     def post(self, request):
#         pass

# def home_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Hello Function View')
#     else:
#         pass

