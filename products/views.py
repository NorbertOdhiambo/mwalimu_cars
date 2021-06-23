from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, ListView, View, TemplateView, FormView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from cloudinary.forms import cl_init_js_callbacks


# def index(request):
#     brand = Brand.objects.all()
#     context = {'brand': brand}
#     return render(request, 'index.html', context)


def showusers(request):
    usrs = User.objects.all()
    return render(request, 'adminpage/users.html', {'usrs': usrs})


def mails(request):
    pass


def tasks(request):
    pass


def authentication(request):
    pass


def pricing(request):
    pass


def event_cal(request):
    pass


def analytics(request):
    pass


def profile(request):
    return render(request, 'profile.html')


def orderslist(request):
    all_orders = Order.objects.all().order_by('-id')
    context = {"all_orders": all_orders}
    return render(request, 'adminpage/orders.html', context)


def handler500(request):
    return render(request, '500.html', status=500)


def handler503(request):
    return render(request, '503.html', status=503)


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = "Mwalimu Cars"
        all_products = Product.objects.all().order_by("-id")
        paginator = Paginator(all_products, 8)
        page_number = self.request.GET.get('page')
        product_list = paginator.get_page(page_number)
        # try:
        #     post_list = paginator.page(page_number)
        # except PageNotAnInteger:
        #     # If page is not an integer deliver the first page
        #     post_list = paginator.page(1)
        # except EmptyPage:
        #     # If page is out of range deliver last page of results
        #     post_list = paginator.page(paginator.num_pages)

        context['product_list'] = product_list
        brand = Brand.objects.all()
        context['brand'] = brand
        # wm_logo = Watermark.objects.all()
        # context['wm_logo'] = wm_logo
        # context['post_list'] = post_list
        return context


def product_info(request, slug):
    product = Product.objects.get(slug=slug)
    product.view_count += 1
    product.save()
    all_products = Product.objects.all().order_by('-id')
    paginator = Paginator(all_products, 8)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    post = get_object_or_404(Product, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':

        if request.POST.get('name') or request.POST.get('phnnumber') or request.POST.get(
                'address') and request.GET.get('email') and request.POST.get('schedule'):
            post = Order()
            post.name = request.POST.get('name')
            post.phone_no = request.POST.get('phnnumber')
            post.address = request.POST.get('address')
            post.email_address = request.GET.get('email', request.user.email)
            post.customer_scheduled_date = request.POST.get('schedule')
            post.save()
            print('data saved to database')

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # if request.user.is_authenticated and request.user.customer:
    #     print('user/customer is logged in')
    # else:
    #     print("customer not logged in")

    # order_details = Order(customer_name=customer_name, phn_number=phn_number, strt_address=strt_address,
    #                       email_address=email_address, schedule=schedule)
    #
    # order_details.save()

    context = {
        'product': product,
        'product_list': product_list,
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'product_info.html', context)


# class ProductDetailView(TemplateView):
#     template_name = "product_info.html"
#
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         url_slug = self.kwargs['slug']
#         product = Product.objects.get(slug=url_slug)
#         product.view_count += 1
#         product.save()
#         all_products = Product.objects.all().order_by("-id")
#         paginator = Paginator(all_products, 8)
#         page_number = self.request.GET.get('page')
#         product_list = paginator.get_page(page_number)
#         # post = get_object_or_404(Product, slug=url_slug)
#         # comments = post.comments.filter(active=True)
#         # new_comment = None
#         # if self.request.method == 'POST':
#         #     comment_form = CommentForm(data=self.request.POST)
#         #     if comment_form.is_valid():
#         #         # Create Comment object but don't save to database yet
#         #         new_comment = comment_form.save(commit=False)
#         #         # Assign the current post to the comment
#         #         new_comment.post = post
#         #         # Save the comment to the database
#         #         new_comment.save()
#         # else:
#         #     comment_form = CommentForm()
#
#         context['product'] = product
#         context['product_list'] = product_list
#         # context['post'] = post
#         # context['comments'] = comments
#         # context['new_comment'] = new_comment
#         # context['comment_form'] = comment_form
#         return context


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created for ' + user)
            return redirect('products:login')

    context = {'form': form}
    return render(request, 'register2.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('products:index')
        else:
            messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'login2.html', context)


def logoutUser(request):
    logout(request)
    return redirect('products:index')


def new(request):
    pass


def used(request):
    pass


# def latest(request):
#     return render(request, 'latest.html')

class LatestView(TemplateView):
    template_name = "latest.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = "Mwalimu Cars"
        all_products = Product.objects.all().order_by("-id")
        paginator = Paginator(all_products, 8)
        page_number = self.request.GET.get('page')
        product_list = paginator.get_page(page_number)
        context['product_list'] = product_list
        # brand = Brand.objects.all()
        # context['brand'] = brand
        # wm_logo = Watermark.objects.all()
        # context['wm_logo'] = wm_logo
        # context['post_list'] = post_list
        return context


def admin_dashboard(request):
    return render(request, 'adminpage/admin_dashboard.html')


# admin_section

class AdminProductListView(ListView):
    template_name = "adminpage/products_list.html"
    queryset = Product.objects.all().order_by("-id")
    context_object_name = "allproducts"


class AdminProductCreateView(CreateView):
    template_name = "adminpage/product_create.html"
    form_class = ProductForm
    success_url = reverse_lazy("products:adminproductlist")

    def form_valid(self, form):
        p = form.save()
        images = self.request.FILES.getlist("more_images")
        for i in images:
            ProductImage.objects.create(product=p, image=i)
        return super().form_valid(form)
