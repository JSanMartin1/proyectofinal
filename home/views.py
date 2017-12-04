# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Category,Product,Post
from django.shortcuts import render,redirect,get_list_or_404, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CartAddProductForm,Post_form
from django.contrib.auth import get_user_model

# Create your views here.
def home(request):
	return render(request,'home/base.html')

def Contact(request):
	return render(request,'home/Contact.html')

def Historial(request):
	log_user=request.user
	log_Post=Post.objects.filter(user=log_user)
	args = {'user': request.user,'Posts':log_Post}
	return render(request,'home/Historial.html',args)

def Listing(request):
	form = Post_form(request.POST  or None)
	if request.method=='POST':
		if form.is_valid():
			Post = form.save(commit=False)
			Post.user = request.user
			Post = Post.save()
		return redirect('/')

	return render(request,'home/Listing.html',{'form':form})

def product_list(request,category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category,slug=category_slug)
		products = products.filter(category=category)
	return render(request,'home/list.html',{'category':category,
												'categories':categories,
												 'products':products})


def product_detail(request,id,slug):
	product = get_object_or_404(Product,id=id,slug=slug,available=True)
	cart_product_form = CartAddProductForm()
	return render(request,
					'home/detail.html',
					{'product':product,
					'cart_product_form':cart_product_form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = UserCreationForm()

        args = {'form':form}
        return render(request,'home/signup.html',args)
