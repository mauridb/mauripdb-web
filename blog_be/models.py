# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    web_user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)

    def set_web_user_first_name(self, first_name):
        self.web_user.first_name = first_name

    def set_web_user_last_name(self, last_name):
        self.web_user.last_name = last_name

    # TODO: Create Post
    def create_post(self):
        pass

    # TODO: Update Post
    def update_post(self):
        pass

    # TODO: Delete Post
    def delete_post(self):
        pass

    def __str__(self):
        return "%s %s" % (self.web_user.first_name, self.web_user.last_name)


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    subtitle = models.CharField(max_length=100, blank=False, null=False)
    tag = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(max_length=500, blank=True, null=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, blank=False, null=False)

    def __str__(self):
        return "%s" % self.title
