from django.http import HttpResponseServerError
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
