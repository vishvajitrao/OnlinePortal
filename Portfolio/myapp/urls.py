from django.urls import path
from . import views


urlpatterns = [
    path('',views.Index,name='Index'),
    path('blog',views.PostList,name='Blog'),
    path('blog/<slug:slug>/',views.PostDetail, name='PostDetail'),
    path('carrer',views.ApplyNow, name='ApplyNow'),
    path('python-tutorial',views.TutorialPage, name='TutorialPage'),
    path('django-tutorial',views.DjangoPage, name='DjangoPage'),
    path('blog/tags/<str:slug>/',views.tagged, name='tagged'),
    path('page/<str:slug>/',views.page, name='Pages'),
    path('dashboard/',views.Dashboard, name='Dashboard'),
    path('contact/',views.Contact, name='Contact'),
    path('product/',views.Products, name='Products'),
    path('product/<str:slug>/',views.ProductsDetails, name='ProductsDetails'),
]