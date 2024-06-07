from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DetailView
from django.urls import reverse_lazy
from .models import Tweet
from .forms import TweetForm

class IndexView(ListView):
    model = Tweet
    template_name = 'tweets/index.html'
    context_object_name = 'tweets'
    ordering = '-created_at'

class CreateView(CreateView):
    form_class = TweetForm
    template_name = 'tweets/create.html'
    success_url = reverse_lazy("Tweets:index")

    def form_valid(self, form):
        tweet = form.save(commit=False)
        tweet.user=self.request.user
        tweet.save()
        return super().form_valid(form)
    
class DeleteView(DeleteView):
    model = Tweet
    success_url = reverse_lazy('Tweets:index')

class UpdateView(UpdateView):
    model = Tweet
    form_class = TweetForm
    template_name = 'tweets/update.html'
    success_url = reverse_lazy('Tweets:index')

class DetailView(DetailView):
    model = Tweet
    template_name = 'tweets/detail.html'