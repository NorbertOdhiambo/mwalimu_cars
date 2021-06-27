from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(ProductImage)
admin.site.register(Brand)
admin.site.register(SliderArrows)
admin.site.register(LogoAnimation)
admin.site.register(Poster)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Feature)


class ProductAdmin(SummernoteModelAdmin):
    list_display = ('make', 'model', 'slug', 'price', 'upload_date')
    # list_filter = ("status",)
    search_fields = ['make', 'description']
    prepopulated_fields = {'slug': ('make',)}
    summernote_fields = ('description',)


admin.site.register(Product, ProductAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
