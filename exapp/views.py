from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class mainView(APIView):
    def get(self,request):
        return Response('HELLO! Would!',status=status.HTTP_200_OK)

class PostView(APIView):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)

        return Response(serializer.data, status=status.HTTP_200_OK)
