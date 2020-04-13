from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from blog.models import Post

post_detail_url = HyperlinkedIdentityField(
	view_name = 'posts-api:detail',
	lookup_field = 'title'
	)

class PostDetailSerializer(ModelSerializer):
	url = post_detail_url
	author = SerializerMethodField()

	class Meta:
		model = Post
		fields = [
			'url',
			'id',
			'author',
			'title',
			'content',
			'date_posted',
		]
		
	def get_author(self, obj):
		return str(obj.author.username)

class PostListSerializer(ModelSerializer):
	author = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'author',
			'title',
			'content',
			'date_posted',
		]

	def get_author(self, obj):
		return str(obj.author.username)
