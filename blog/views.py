from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Post
# Create your views here.
class BlogPostsListView(ListView):

	model = Post
	template_name = 'post_list.html'

	def get_queryset(self):
		return Post.published.all().order_by('-published_date')