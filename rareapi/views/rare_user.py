from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rareapi.models import RareUser

class RareUserView(ViewSet):
    """Rare Users view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user
        """
        rare_user = RareUser.objects.get(pk=pk)
        serializer = RareUserSerializer(rare_user)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """
        rare_users = RareUser.objects.all()
        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data)
    
    @action(methods=['post'], detail=True)
    def active(self, request, pk):
        """"Post Request for a user to become active"""
        rareuser = RareUser.objects.get(pk=request.data["id"], active=request.data["True"])
        ActiveRareUser.objects.create(
            activerareuser = rareuser
        )
        return Response({'message': 'Active User'}, status=status.HTTP_201_CREATED)
    
    @action(methods=['delete'], detail=True)
    def notactive(self, request, pk):
        """Delete request for a user to become inactive"""
        rareuser = RareUser.objects.get(pk=request.data["id"], active=request.data["True"])
        activeUser = ActiveRareUser.objects.filter(
            activerareuser = rareuser
        )
        activeUser.delete()
        return Response({'message': 'User deactivated'}, status=status.HTTP_204_NO_CONTENT)
      
class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users"""
    class Meta:
        model = RareUser
        fields = ('id', 'first_name', 'last_name', 'uid', 'bio', 'email', 'created_on', 'active', 'is_staff', 'profile_image_url')
  