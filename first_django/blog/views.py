from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib import messages

from django.shortcuts import redirect, render, get_object_or_404

from django.http import HttpResponse

from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView)

from .forms import CustomerHBDForm
from .models import CustomerHBD, Post

from .tasks import sleepy, send_email_task


def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    context = {'title':'ABOUT'}
    return render(request=request, template_name='blog/about.html', context=context)

def wishes(request):
    sleepy(2)
    if request.method == 'POST':
        form = CustomerHBDForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get("name")
            date = form.cleaned_data.get("date")
            time = form.cleaned_data.get("time")
            messages.success(request, f'Sending mail to {name} on {date} at {time}')
            return redirect('/')
    else:
        form = CustomerHBDForm()
    context = {'form':form, 'title':'Multiple-Wishes'}
    return render(request=request, template_name='blog/wishes.html', context=context)


def index():
    send_email_task.delay()
    return HttpResponse('<h1>EMAIL HAS BEEN SENT WITH CELERY!</h1>')


def Ebook(request):
    context = {'title':'Ebook'}
    return render(request=request, template_name='blog/Ebook.html', context=context)
