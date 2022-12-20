from django.http import HttpResponseServerError
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rareapi.models import RareUser

class RareUserView(ViewSet):
    """Rare Users view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single user

        Returns:
            Response -- JSON serialized user
        """
        rare_user = RareUser.objects.get(pk=pk)
        uid = request.META['HTTP_AUTHORIZATION']
        auth_user = RareUser.objects.get(uid=uid)
        if auth_user.is_staff == False:
            return Response(None, status=status.HTTP_403_FORBIDDEN)
        
        serializer = RareUserSerializer(rare_user)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all users

        Returns:
            Response -- JSON serialized list of users
        """
        rare_users = RareUser.objects.all()
        uid = request.META['HTTP_AUTHORIZATION']
        auth_user = RareUser.objects.get(uid=uid)
        if auth_user.is_staff == False:
            return Response(None, status=status.HTTP_403_FORBIDDEN)
        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data)

    def update(self, request, pk):
        rare_user = RareUser.objects.get(pk=pk)
        rare_user.first_name = request.data["first_name"]
        rare_user.last_name = request.data["last_name"]
        rare_user.uid = request.data["uid"]
        rare_user.bio = request.data["bio"]
        rare_user.email = request.data["email"]
        rare_user.created_on = request.data["created_on"]
        rare_user.active = request.data["active"]
        rare_user.is_staff = request.data["is_staff"]
        rare_user.profile_image_url = request.data["profile_image_url"]
        rare_user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['put'], detail=True)
    def change_is_staff(self, request, pk):
        rare_user = RareUser.objects.get(pk=pk)

        rare_user.is_staff = not rare_user.is_staff
        rare_user.save()
        serializer = RareUserSerializer(rare_user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True)
    def change_is_active(self, request, pk):
        rare_user = RareUser.objects.get(pk=pk)

        rare_user.active = not rare_user.active
        rare_user.save()
        serializer = RareUserSerializer(rare_user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RareUserSerializer(serializers.ModelSerializer):
    """JSON serializer for rare users"""
    class Meta:
        model = RareUser
        fields = ('id', 'first_name', 'last_name', 'uid', 'bio', 'email', 'created_on', 'active', 'is_staff', 'profile_image_url')
