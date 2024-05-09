from typing import Any
from django.shortcuts import render, redirect, get_object_or_404
from cars import models
from cars.models import Car
from cars import forms
from cars.models import Brand
from django.views.generic import DetailView
from cars.forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.views.generic import DetailView


def home(request, category_slug=None):
    data = models.Car.objects.all()

    if category_slug is not None:
        # category = get_object_or_404(Brand, slug=category_slug)
        # kon object er part ta ber kore niye also
        category = Brand.objects.get(slug=category_slug)
        data = models.Car.objects.filter(category=category)
    categories = Brand.objects.all()

    return render(request, 'home.html', {'data': data, 'categories': categories})


class DetailPostView(DetailView):
    model = models.Car
    form_class = forms.CarForm
    pk_url_kwarg = 'id'
    template_name = 'car_detail.html'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post  # Set the car_id field
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
