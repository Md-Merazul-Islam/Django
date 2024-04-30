from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from . import forms, models
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView,DeleteView
from  django.utils.decorators import method_decorator



#add post use class base view 
@method_decorator(login_required, name='dispatch')
class AddPostCreateViews(CreateView):
    model = models.Post
    form_class  =  forms.PostForm
    template_name = 'add_post.html'
    success_url= reverse_lazy('add_post')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

#post edit 
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post 
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg= 'id'
    success_url = reverse_lazy('profile')

#delete post 
@method_decorator(login_required, name='dispatch')
class DeletePost(DeleteView):
    model = models.Post
    from_class = forms.PostForm
    template_name ='delete.html'
    pk_url_kwarg= 'id'
    success_url =reverse_lazy('profile')