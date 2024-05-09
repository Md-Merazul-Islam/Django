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


# def car_details_view(request, car_id):
#     car = get_object_or_404(Car, id = car_id)
#     return render(request,'car_details.html',{'car':car})


# class DetailPostView(DetailView):
#     model = models.Car
#     form_class = forms.CarForm
#     pk_url_kwarg = 'id'
#     template_name = 'car_details.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         post = self.object
#         comments = post.comments.all()

#         if self.request.method == 'POST':
#             comment_form = forms.CommentForm(data=self.request.POST)
#             if comment_form.is_valid():
#                 new_comment = comment_form.save(commit=False)
#                 new_comment.post = post
#                 new_comment.save()
#         else:
#             comment_form = forms.CommentForm()

#         context['comments'] = comments
#         context['comment_form'] = comment_form
#         return context

# views.py


def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    comments = car.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.save()
            return redirect('car_detail', car_id=car_id)
    else:
        form = CommentForm()
    return render(request, 'car_detail.html', {'car': car, 'comments': comments, 'form': form})


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
