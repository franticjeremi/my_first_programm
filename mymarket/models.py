from django.db import models

# Create your models here.
class Mymarket(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    url = models.URLField()
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Configuration(models.Model):
    widget = models.ForeignKey(Mymarket)
    name = models.CharField(max_length=200)
    dataType = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.name

class Method(models.Model):
    widget = models.ForeignKey(Mymarket)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    example = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.name

class Event(models.Model):
    widget = models.ForeignKey(Mymarket)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    def __unicode__(self):
        return self.name

class WidgetExample(models.Model):
    widget = models.ForeignKey(Mymarket)
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=2000)
    def __unicode__(self):
        return self.title