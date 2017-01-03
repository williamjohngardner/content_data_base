from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag


class File(models.Model):
    name = models.CharField(max_length=100)
    content = models.FileField(upload_to='content_files', null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    author = models.CharField(max_length=50)
    vendor = models.CharField(max_length=75)

    def __str__(self):
        return self.name
