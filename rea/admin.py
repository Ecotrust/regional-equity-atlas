from django.contrib import admin
from rea.models import *
from ckeditor.widgets import CKEditorWidget

class ThemeContentAdmin(admin.ModelAdmin):
    list_display = ('theme',)

class ContentAdmin(admin.ModelAdmin):
    list_display = ('theme_content', 'focus')
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

class FocusAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'order')

# Register your models here.
admin.site.register(ThemeContent, ThemeContentAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Topic)
admin.site.register(Focus, FocusAdmin)
