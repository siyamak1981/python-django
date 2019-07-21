from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.generic import ListView, DetailView, TemplateView
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404
# class ShopListView(ListView):
#     model = Product
#     template_name = 'shop/products.html'
#     context_object_name = 'products'
#     paginate_by = 1
#     page_name = ' فروشگاه '
  

#     def get_context_data(self, *args, **kwargs):
#         context = super(ShopListView, self).get_context_data(*args, **kwargs)
#         context['product'] = Product.objects.filter()
#         context['categories'] = Category.objects.all()
#         return context
       
        
# class ShopDetailView(DetailView):
#     model = Product
#     template_name = 'shop/product.html'
#     context_object_name = 'product'
#     page_name = 'محصول '

#     def get_context_data(self, *args, **kwargs):
#         context = super(ShopDetailView, self).get_context_data(*args, **kwargs)
#         cart_product_form = CartAddProductForm()
#         context['product'] = Product.objects.all()
#         context['cart_product_form'] = cart_product_form
#         return context




   
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available = True)
     
 
    if category_slug:
        category =get_object_or_404(Category, slug=category_slug)
        products = products.filter(category= category) 
        page = request.GET.get('page')
        paginator = Paginator(products, 1) 
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        
    return render(request, 'shop/products.html', {'category':category,
                                                    'posts': posts,
                                                    'page':page,
                                                    'categories':categories,
                                                    'products': products
                                                     })
  
        


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form= CartAddProductForm()
    return render(request,
                  'shop/product.html',
                  {'product':product,
                  'cart_product_form': cart_product_form})

    
# from django.contrib.auth.models import User
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# def index(request):
#     page_obj = Product.objects.all()
#     page = request.GET.get('page', 6)

#     paginator = Paginator(page_obj, 1)
#     try:
#         page_obj = paginator.page(page)
#     except PageNotAnInteger:
#         page_obj = paginator.page(1)
#     except EmptyPage:
#         page_obj = paginator.page(paginator.num_pages)

#     return render(request, 'shop/list.html', { 'page_obj': page_obj })

# from django.core.paginator import Paginator, EmptyPage,\
#                                   PageNotAnInteger

# def post_list(request):
#     object_list = Product.published.all()
#     paginator = Paginator(object_list, 3) # 3 posts in each page
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request,
#                   'blog/post/list.html',
#                   {'page': page,
#                    'posts': posts})

