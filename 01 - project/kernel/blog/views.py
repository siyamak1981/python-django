from django.views.generic import ListView
from .models import Post
from .models import Comment
from django.core.mail import send_mail
from .forms import CommentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from .models import Post, Comment
from django.urls import reverse


def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 1) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
    # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
    # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'page': page,
                                                    'posts': posts })
                                                   

# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/post_list.html'
#     context_object_name = 'posts'
#     paginate_by = 2
#     page_name = 'اخبار'



def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    posts = post
    comments = post.comments.filter(active=True)
 
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
       
            new_comment.post = post
         
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'blog/post.html',{'post': post, 'comments': comments,'comment_form': comment_form})


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post.html'
#     context_object_name = 'post'
#     page_name = 'خبر '
    
#     def get_context_data(self, *args, **kwargs):
#         context = super(PostDetailView, self).get_context_data(*args, **kwargs)
#         context['comments'] = Comment.objects.filter(post = context['post'])
#         context['latest_posts'] = Post.objects.all()[:2]
#         return context
        
   
    


