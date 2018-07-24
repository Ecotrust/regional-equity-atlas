from django.contrib import admin
from rea.models import *
from ckeditor.widgets import CKEditorWidget

class InlineContentAdmin(admin.StackedInline):
    model = Content
    fields = ('focus', 'content')
    extra = 0
    classes = ['collapse', 'open']
    verbose_name = 'Content'
    verbose_name_plural = 'Contents'
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }


class ContentAdmin(admin.ModelAdmin):
    list_display = ('theme_content', 'focus')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

class ThemeContentAdmin(admin.ModelAdmin):
    list_display = ('theme',)
    verbose_name_plural = 'related Activities'
    inlines = [
        InlineContentAdmin,
    ]

class FocusAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'order')

# Register your models here.
admin.site.register(ThemeContent, ThemeContentAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Topic)
admin.site.register(Focus, FocusAdmin)
