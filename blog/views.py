from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView

from .models import Post


class BlogPostsListView(ListView):

	model = Post
	template_name = 'post_list.html'

	def get_queryset(self):
		return Post.published.all().order_by('-published_date')


class BlogPostDetailView(DetailView):

	model = Post
	template_name = 'post_detail.html'
