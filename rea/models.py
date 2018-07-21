from django.db import models
from data_manager.models import Layer

# Create your models here.
class Header(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    order = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s_%s" % (self.order, self.name)

    def __str__(self):
        return u"%s_%s" % (self.order, self.name)

class Topic(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    order = models.IntegerField(default=0)
    header = models.ForeignKey(Header)

    def __unicode__(self):
        return u"%s_%s" % (self.header.name, self.name)

    def __str__(self):
        return u"%s_%s" % (self.header.name, self.name)

class Focus(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    order = models.IntegerField(default=0)
    topic = models.ForeignKey(Topic)
    #ignore these for now.
    zoom = models.IntegerField(null=True, blank=True, default=None)
    x_coord = models.FloatField(null=True, blank=True, default=None)
    y_coord = models.FloatField(null=True, blank=True, default=None)

    def __unicode__(self):
        return u"%s_%s_%s" % (self.topic.header.name, self.topic.name, self.name)

    def __str__(self):
        return u"%s_%s_%s" % (self.topic.header.name, self.topic.name, self.name)

    class Meta:
        verbose_name_plural="Focuses"

class LayerState(models.Model):
    focus = models.ForeignKey(Focus)
    layer = models.ForeignKey(Layer)
    active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    opacity = models.FloatField(default=1.0)

    def __unicode__(self):
        return u"%s_%s_%s_%d" % (self.focus.topic.header.name, self.focus.topic.name, self.focus.name, self.order)

    def __str__(self):
        return u"%s_%s_%s_%d" % (self.focus.topic.header.name, self.focus.topic.name, self.focus.name, self.order)

    def toDict(self):
        return {
            'active': self.active,
            'order': self.order,
            'opacity': self.opacity,
            'layer': self.layer.pk
        }
