from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	search_fields = ['title','content']

	class Meta:
		model = Post

admin.site.register(Post, PostModelAdmin)
