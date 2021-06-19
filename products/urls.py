from django.urls import path
from .views import *
from . import views


app_name = 'products'
urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path('product_info/<slug:slug>/', views.product_info, name='productdetail'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('new/', views.new, name='new'),
    path('used/', views.used, name='used'),
    path('latest/', LatestView.as_view(), name='latest'),
    path('profile/', views.profile, name='profile'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path("admin_product/list/", AdminProductListView.as_view(), name="adminproductlist"),
    path("admin_product/add/", AdminProductCreateView.as_view(), name="adminproductcreate"),
    path('admin_dashboard/users/', views.showusers, name='users'),
    path('admin_dashboard/orders/', views.orderslist, name='orders'),
    path('admin_dashboard/mails/', views.mails, name='mails'),
    path('admin_dashboard/task/', views.tasks, name='tasks'),
    path('admin_dashboard/authentications/', views.authentication, name='authenticate'),
    path('admin_dashboard/pricing/', views.pricing, name='pricing'),
    path('admin_dashboard/event_calendar/', views.event_cal, name='calendar'),
    path('admin_dashboard/analytics/', views.analytics, name='analytics'),
]