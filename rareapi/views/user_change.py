from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rareapi.models import UserChange
from rareapi.models import RareUser

class UserChangeView(ViewSet):

    def list(self, request):

        user_change = UserChange.objects.all()
        # uid = request.query_params.get('type', None)
        # if uid is not None:
        #     posts = posts.filter(user_id=uid)
        serializer = UserChangeSerializer(user_change, many = True)
        return Response(serializer.data)

    def create(self, request):

        user_change = UserChange.objects.create(
            action=request.data["action"],
            admin=RareUser.objects.get(pk=request.data["admin"]),
            second_admin= RareUser.objects.get(pk=request.data["second_admin"]),
            modified_user=RareUser.objects.get(pk=request.data["modified_user"])
        )
        return Response(None, status=status.HTTP_204_NO_CONTENT)



    def destroy(self, request, pk):
        user_change = UserChange.objects.get(pk=pk)
        user_change.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserChangeSerializer(serializers.ModelSerializer):
    """JSON serializer for RareUsers"""
    class Meta:
        model = UserChange
        fields = ('id', 'admin', 'action', 'second_admin', 'modified_user')
        depth = 1
