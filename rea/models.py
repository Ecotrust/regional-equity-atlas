from django.db import models
from data_manager.models import Layer, Theme

# Create your models here.
class ThemeContent(models.Model):
    theme = models.ForeignKey(Theme)

    def __str__(self):
        return str(self.theme.display_name)

class Topic(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Focus(models.Model):
    name = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic)

    def __str__(self):
        return "%s_%s" % (str(self.topic), self.name)

    class Meta:
        verbose_name_plural = "Focuses"

class Content(models.Model):
    theme_content = models.ForeignKey(ThemeContent)
    focus = models.ForeignKey(Focus, default=None, null=True, blank=True)
    content = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return "%s_%s" % (self.theme_content, self.focus if self.focus else 'Base')
