from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import serializers, status
from rareapi.models import RareUser

class UserView(ViewSet):
    
    def retrieve(self, request, pk):
        """Handle GET requests for a single user

        Args:
            Response --- JSON serialized post
        """
        user = RareUser.objects.get(pk=pk)
        uid = request.META['HTTP_AUTHORIZATION']
        print(uid)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def list(self, request):
        permission_classes = [IsAdminUser, ]
        """Handle GET requests to get all posts

        Returns:
            Response -- JSON serialized list of posts
        """
        users = RareUser.objects.all()
        uid = request.query_params.get('type', None)
        if uid is not None:
          posts = posts.filter(user_id=uid)  
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data) 
    
    
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = RareUser
        fields = ('id', 'first_name', 'last_name','bio','email','created_on','active','is_staff','profile_image_url','uid')
