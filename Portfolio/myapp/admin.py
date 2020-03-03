from django.contrib import admin
from myapp.models import *
# Register your models here.


admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(SearchEngineOptimization)
admin.site.register(Comment)
admin.site.register(Ads)
admin.site.register(Headerad)
admin.site.register(Pages)
admin.site.register(Logo)
admin.site.register(Icon)
admin.site.register(HomepageSlider)


class Titileandtag(admin.ModelAdmin):
    list_display = ('title','tagline','id')
admin.site.register(TitleandTag, Titileandtag)



admin.site.register(SiteDescription)
admin.site.register(Footer)
admin.site.register(Video)
