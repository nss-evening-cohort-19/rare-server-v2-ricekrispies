from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser, Comment
from rest_framework.permissions import AllowAny, IsAdminUser


class CommentView(ViewSet):

    def retrieve(self, request, pk):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post
        """
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        comments = Comment.objects.all()
        # uid = request.query_params.get('type', None)
        # if uid is not None:
        #     comments = comments.filter(user_id=uid)
        serializer = CommentSerializer(comments, many = True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post instance
        """
        user = RareUser.objects.get(pk=request.data["user"])
        post = Post.objects.get(pk=request.data["post"])

        comment = Comment.objects.create(
        created_on=request.data["created_on"],
        content=request.data["content"],
        post=post,
        user=user
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        comment = Comment.objects.get(pk=pk)
        comment.created_on = request.data["created_on"]
        comment.content = request.data["content"]
      
    
        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CommentSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Comment
        fields = ('id', 'user', 'post', 'created_on', 'content')
        depth = 1
