from taggit.models import Tag
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from myapp.models import Blog, Comment, Headerad, Ads, Logo, HomepageSlider, TitleandTag, SiteDescription, Footer, Video, SearchEngineOptimization, Product
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from myapp.forms import CommentForm
# Create your views here.
from django.core.mail import send_mail
from myapp.models import Pages
from django.conf import settings
import requests


def Index(request):
    seo = SearchEngineOptimization.objects.all()
    sitelogo = Logo.objects.all().last()
    pages = Pages.objects.all()
    post = Blog.objects.filter(status=1)[:3]
    sliderimage1 = HomepageSlider.objects.first()
    sliderimage2 = HomepageSlider.objects.last()
    title = TitleandTag.objects.all()
    about = SiteDescription.objects.first()
    footer = Footer.objects.first()
    footerlink = Footer.objects.last()
    video = Video.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pnumber = request.POST.get('pnumber')
        ptype = request.POST.get('ptype')
        description = request.POST.get('description')
        context = {'name': name, 'email': email, 'pnumber': pnumber,
                   'ptype': ptype, 'description': description}
        print(context)
        message = f"Name: {name}\nEmail: {email}\nPhone Number: {pnumber}\nPlatform: {ptype}\nProject Description: {description}\n\n\nRegards\n{name}"
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post(
            'https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            request.recaptcha_is_valid = True
            send_mail(ptype, message, email, ['vishvajitrao12@gmail.com'])
            send = True
            return render(request, 'index.html', {'send': send})
        else:
            request.recaptcha_is_valid = False
            return HttpResponse('Invalid details:')

    else:
        pass
    context = {
        'send': False,
        'pages': pages,
        'Logo': sitelogo,
        'post': post,
        'first': sliderimage1,
        'second': sliderimage2,
        'title': title,
        'about': about,
        'footer': footer,
        'footerlink': footerlink,
        'video': video,
        'seo': seo

    }

    return render(request, 'index.html', context)


def PostList(request):
    blog_list = Blog.objects.filter(status=1).order_by('-created_on')
    blog_list1 = Blog.objects.filter(status=1)[:2]
    blog_lists = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 6)
    alltages = Tag.objects.all()
    sitelogo = Logo.objects.all().last()
    pages = Pages.objects.all()
    post = Blog.objects.filter(status=1)[:3]
    sliderimage1 = HomepageSlider.objects.first()
    sliderimage2 = HomepageSlider.objects.last()
    title = TitleandTag.objects.all()
    about = SiteDescription.objects.first()
    footer = Footer.objects.first()
    footerlink = Footer.objects.last()
    video = Video.objects.first()
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    print(blog_list1)
    comment_form = CommentForm()
    context = {
        'blog_list': blog_list,
        'blog_list1': blog_list1,
        'comment_form': comment_form,
        'posts': posts,
        'tags': alltages,
        'send': False,
        'pages': pages,
        'Logo': sitelogo,
        'post': post,
        'first': sliderimage1,
        'second': sliderimage2,
        'title': title,
        'about': about,
        'footer': footer,
        'footerlink': footerlink,
        'video': video

    }
    return render(request, 'blog.html', context)


def PostDetail(request, slug):
    posts = Blog.objects.filter(status=1).order_by('?')[:4]
    ads = Ads.objects.all()
    blog_detail = Blog.objects.filter(slug=slug)[0]
    tags = blog_detail.tags.all()
    pythonpost = Blog.objects.filter(status=1, Category='Python').reverse()
    djangopost = Blog.objects.filter(status=1, Category='Django')
    post = get_object_or_404(Blog, slug=slug)
    comments = post.comments.filter(active=True)
    sitelogo = Logo.objects.all().last()
    pages = Pages.objects.all()
    post = Blog.objects.filter(status=1)[:3]
    sliderimage1 = HomepageSlider.objects.first()
    sliderimage2 = HomepageSlider.objects.last()
    title = TitleandTag.objects.all()
    about = SiteDescription.objects.first()
    footer = Footer.objects.first()
    footerlink = Footer.objects.last()
    video = Video.objects.first()
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return HttpResponseRedirect(reverse('PostDetail', args=[slug]))

    else:
        comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'blog': blog_detail,
        'pythonpost': pythonpost,
        'djangopost': djangopost,
        'tags': tags,
        'posts': posts,
        'ads': ads,

        'send': False,
        'pages': pages,
        'Logo': sitelogo,
        'post': post,
        'first': sliderimage1,
        'second': sliderimage2,
        'title': title,
        'about': about,
        'footer': footer,
        'footerlink': footerlink,
        'video': video


    }
    return render(request, 'blog_detail.html', context)


# Contact us form
def ApplyNow(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        pnumber = request.POST.get('pnumber')
        ptype = request.POST.get('ptype')
        description = request.POST.get('description')
        context = {'name': name, 'email': email, 'pnumber': pnumber,
                   'ptype': ptype, 'description': description}
        print(context)
        return HttpResponse('Thanks')
    else:
        pass
    return render(request, 'carrer.html')


# Individual tutorial page


def TutorialPage(request):
    pythontopic = Blog.objects.filter(status=1, Category='Python')
    print(pythontopic)
    context = {
        'pythontopic': pythontopic,
    }
    return render(request, 'tutorial.html', context)


def DjangoPage(request):
    djangotopic = Blog.objects.filter(status=1, Category='Django').reverse()
    context = {
        'djangotopic': djangotopic,
    }
    return render(request, 'django.html', context)


# Ads placement
def tagged(request, slug):
    headerad = Headerad.objects.all()
    tag = get_object_or_404(Tag, slug=slug)
    tagposts = Blog.objects.filter(status=1, tags=tag)
    return render(request, 'tagpost.html', {'tagposts': tagposts, 'slug': slug, 'headerad': headerad})


# All pages
def page(request, slug):
    pages = Pages.objects.all()
    page = Pages.objects.filter(slug=slug)
    return render(request, 'page.html', {'page': page, 'pages': pages})


def Dashboard(request):
    publishpost = Blog.objects.filter(status=1).count()
    draftpost = Blog.objects.filter(status=0).count()
    allpost = Blog.objects.all().count()
    publish = Blog.objects.filter(status=1)
    draftpost = Blog.objects.filter(status=0).count()
    allpost = Blog.objects.all().count()

    context = {
        'publishpost': publishpost,
        'draftpost': draftpost,
        'allpost': allpost,
        'publish': publish,

    }
    return render(request, 'dashboard.html', context)


def Contact(request):
    return render(request, 'contact.html')



def Products(request):
    product = Product.objects.all()
    print(product)
    return render(request, 'product.html', {'product': product})

def ProductsDetails(request, slug):
    product = Product.objects.get(pslug=slug)
    print(product)
    return render(request, 'product-detail.html', {'p': product})