from rest_framework import viewsets
from .serializers import PostSerializer
from .models import 

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
