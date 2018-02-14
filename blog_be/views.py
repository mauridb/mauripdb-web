# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from blog_be.models import Author, Post
from django.shortcuts import render


def index(request):
    """
    Index page of my website.
    """

    # TODO
    context = {}
    return render(request, 'index.html', context)


def sign_up(request):
    """
    Registration page
    """

    # TODO
    context = {}
    return render(request, 'sign_up.html', context)


def sign_in(request):
    """
    Login page
    """

    # TODO
    context = {}
    return render(request, 'sign_in.html', context)
