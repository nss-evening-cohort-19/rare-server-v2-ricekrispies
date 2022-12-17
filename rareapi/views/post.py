from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import Post, RareUser

class PostView(ViewSet):

    def retrieve(self, request, pk):
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
        posts = Post.objects.all()
        uid = request.query_params.get('type', None)
        if uid is not None:
            posts = posts.filter(user_id=uid)
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
                user=rareUser
                approved=True
                )
        else:
            post = Post.objects.create(
                title=request.data["title"],
                publication_date=request.data["publication_date"],
                content=request.data["content"],
                approved=False
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

        #The below is for when we incorp categories
        # category = Category.objects.get(pk=request.data["category"])
        # post.category = category
        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for posts
    """
    class Meta:
        model = Post
        fields = ('id', 'user', 'title', 'publication_date', 'content', 'approved')
        depth = 1
