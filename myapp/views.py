from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .mixins import HasPermissionMixin
from .models import Post


class BlogListView(LoginRequiredMixin, ListView):

    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.filter(is_superuser=False)
        return context


class BlogDetailView(LoginRequiredMixin, DetailView):

    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # import ipdb
        # ipdb.set_trace()
        context['post_creator'] = self.object.user  # self.object.user
        return context


class BlogCreateView(CreateView):

    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class BlogEditView(HasPermissionMixin, LoginRequiredMixin, UpdateView):

    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
    permission_required = 'myapp.can_make_flutter_effect'

    # def get_permission_required(self):
    #     return self.permission_required


class BlogDeleteView(HasPermissionMixin, LoginRequiredMixin, DeleteView):

    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
