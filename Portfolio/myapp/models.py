from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

 

# Create your models here.


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

Category = {
    ('Python','Python Tutorial'),
    ('Python-built-in','Python Built-in Module'),
    ('Python-external','Python External Module'),
    ('Python-tool','Python Coding Tool'),
    ('Django','Django Tutorial'),
    ('Flask','Flask Tutorial'),
}


class Blog(models.Model):
    image = models.FileField(upload_to='post')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])
    
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    Category = models.CharField(choices=Category,max_length=20,default='Python Tutorial')
    tags = TaggableManager()
    
    
    

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    website = models.URLField(null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Headerad(models.Model):
    Ad_name = models.CharField(max_length=20)
    Header_Ad = RichTextField(config_name='awesome_ckeditor')

    def __str__(self):
        return self.Ad_name




class Ads(models.Model):
    Header_Ad = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])
    sidebar_one = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])
    sidebar_two = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])
    bottom = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])
    article_one = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])
    article_two = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])
    article_three = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])

    def __str__(self):
        return "Ads Placement"



    


class Pages(models.Model):
    title = models.CharField(max_length=20,unique=True)
    slug = models.SlugField(unique=True,max_length=20)
    content = RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])



class Logo(models.Model):
    logo = models.FileField('Website Logo',upload_to='logos',blank=True,null=True)
    

 

class Icon(models.Model):
    siteicon = models.FileField('Website Icon',upload_to='icons',blank = True,null=True)
    

class HomepageSlider(models.Model):
    imageone = models.FileField('First Image:- ', upload_to='First',blank=True)
    imagetwo = models.FileField('Second Image:- ', upload_to='Second',blank=True)


class TitleandTag(models.Model):
    title = models.CharField(max_length= 50, blank=True)
    tagline = models.CharField(max_length= 100, blank=True)


class SiteDescription(models.Model):
    about = models.TextField('Site Description:- ',max_length=300)


class Footer(models.Model):
    text = models.CharField('Footer text',max_length=50)
    textlink = models.CharField('Footer link text',max_length=50)



class Video(models.Model):
    video = models.FileField(upload_to='Videos')


robotfollow = (
    ("index,","Yes"),
    ("noindex","No")
)
robotindex = (
    ("follow","Yes"),
    ("nofollow","No")
)
language = (
    ("English","English"),
    ("Hindi","Hindi"),
    ("French","French"),
    ("Spanish","Spanish")
)


class SearchEngineOptimization(models.Model):
    title = models.CharField('Site Title (70 Characters)', max_length=70)
    description = models.TextField('Site Description (150 Characters)', max_length=150)
    keyword = models.TextField('Site Keywords (200 Characters) (Separate with commas)', max_length=200)
    author = models.CharField('Site Author (50)', max_length=50)
    contenttype = models.CharField('Content Type', max_length=20)
    robotfollow = models.CharField('Allow robots to follow all links?', max_length=20, choices=robotfollow)
    robotindex = models.CharField('Allow robots to index your website?', max_length=20, choices=robotindex)
    language = models.CharField('What is your site primary language?', max_length=20, choices=language)
    
    class Meta:
        verbose_name = "Search Engine Optimization Setting"



class Product(models.Model):
    pname = models.CharField('Product Name:- ', max_length=50)
    pprice = models.IntegerField('Product Price:- ')
    pimage = models.FileField('Image of Product:- ', upload_to='Product')
    pspecification =  RichTextUploadingField(blank=True,null=True,external_plugin_resources = [(
        'youtube',
        '/static/ckeditor_plugins/youtube/youtube/',
        'plugin.js',
    )])
    pslug = models.SlugField(default='product')
    pmrp = models.IntegerField('Product M.R.P:- ',default=0)
    yousave = models.IntegerField('You Save:- ', default=0)