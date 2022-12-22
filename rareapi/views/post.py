from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser
from rest_framework.permissions import AllowAny, IsAdminUser


class PostView(ViewSet):

    def retrieve(self, request, pk):
        permission_classes = [AllowAny,]
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized post
        """
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        
        uid = request.META['HTTP_AUTHORIZATION']        
        rare_user = RareUser.objects.get(uid=uid)
        posts = Post.objects.all()
        uid = request.query_params.get('type', None)
        if uid is not None:
            posts = posts.filter(user_id=uid)
        if rare_user.is_staff == False:
            posts = posts.filter(approved=True)
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized post instance
        """
        rareUser = RareUser.objects.get(uid=request.data["uid"])

        if rareUser.is_staff == True:
            post = Post.objects.create(
            title=request.data["title"],
            publication_date=request.data["publication_date"],
            content=request.data["content"],
            approved=True,
            image_url=request.data["image_url"],
            user=rareUser
            )
        else:
            post = Post.objects.create(
            title=request.data["title"],
            publication_date=request.data["publication_date"],
            content=request.data["content"],
            approved=False,
            image_url=request.data["image_url"],
            user=rareUser
            )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.publication_date = request.data["publication_date"]
        post.content = request.data["content"]
        post.approved = request.data["approved"]
        post.image_url = request.data["image_url"],

        #The below is for when we incorp categories
        # category = Category.objects.get(pk=request.data["category"])
        # post.category = category
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    @action(methods=['put'], detail=True)
    def change_approved(self, request, pk):
        post = Post.objects.get(pk=pk)
        
        post.approved = not post.approved
        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'publication_date', 'content', 'approved', 'image_url')
        depth = 1
