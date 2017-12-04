# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse_lazy

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200,db_index = True)
    slug = models.SlugField(max_length=200,db_index = True,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_list_by_category',args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,related_name ='products')
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        index_together =(('id','slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home:product_detail',args=[self.id,self.slug])


class Post(models.Model):
    user = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def get_absolute_url(self):
        return reverse_lazy('post_view', kwargs={'post_id': self.id})

    def __str__(self):
        return self.content
