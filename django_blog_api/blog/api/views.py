from rest_framework.generics import (
	ListAPIView, 
	RetrieveAPIView,
	DestroyAPIView,
	CreateAPIView,
	RetrieveUpdateAPIView,
	)

from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

from django.db.models import Q
from rest_framework.filters import (
	SearchFilter,
	OrderingFilter,
	)

from rest_framework.pagination import (
	LimitOffsetPagination,
	PageNumberPagination,
	)

from .pagination import PostLimitOffsetPagination, PostPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from blog.models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostListAPIView(ListAPIView):
	serializer_class = PostListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['title','content']
	pagination_class = PostPageNumberPagination
	permission_classes = [AllowAny]


	def get_queryset(self, *args, **kwargs):
		queryset_list = Post.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)
				).distinct()
		return queryset_list


class PostDetailAPIView(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'title'
	permission_classes = [AllowAny]


class PostUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'title'
	permission_classes = [IsOwnerOrReadOnly]

	def perform_update(self, serializer):
		serializer.save(author=self.request.user)
 
class PostDeleteAPIView(DestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	lookup_field = 'title'
	permission_classes = [IsOwnerOrReadOnly]


class PostCreateAPIView(CreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostDetailSerializer
	# permission_classes = [ IsAuthenticated]

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

