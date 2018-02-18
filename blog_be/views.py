# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from blog_be.models import Author, Post
from django.shortcuts import render, redirect

import logging
logging.basicConfig(filename='myblog.log', level=logging.DEBUG)


def index(request):
    """
    Index page of my website.
    """


    authors = Author.objects.all()
    posts = Post.objects.all()
    users = User.objects.all()
    context = {
        'authors': authors,
        'posts': posts,
        'users': users,
    }
    return render(request, 'ng_dashboard/index.html', context)


def sign_up(request):
    """
    Registration page
    """

    # TODO
    context = {}
    if request.method == 'POST':
        # create user
        user = User.objects.create(
            email=request.POST.get("email", ""), 
            password=request.POST.get("password", ""), 
            username=request.POST.get("username",""),
            first_name=request.POST.get("first_name",""),
            last_name=request.POST.get("last_name","")
            )
        print(user)
        if user:
            author = Author.objects.create(web_user=user)
            logging.info('Web user & Author registered into the platform')

    return render(request, 'ng_dashboard/ng_registration/sign_up.html', context)


def sign_in(request):
    """
    Login page
    """
    context = {}
    if request.method == 'POST':
        try:
            user = User.objects.get(email=request.POST.get("email", ""))

            # check if user credentials are correct
            if request.POST.get("email", "") and request.POST.get("password", "") and user.check_password(request.POST.get("password", "")):
                logging.info('User correct credentials')
                # TODO: redirect to dashboard page
            else:
                logging.info('Wrong passed credentials')
                context['error_message'] = "Wrong password!"
                return redirect('sign-in', context)
        except Exception, e:
            logging.info(e)
        

    return render(request, 'ng_dashboard/ng_registration/sign_in.html', context)


def dashboard(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        context = {
            'posts': posts,
        }
        return render(request, 'ng_dashboard/dashboard.html', context)



