from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rareapi.models import Demotion
from rareapi.models import RareUser

class DemotionView(ViewSet):

    def list(self, request):

        demotion = Demotion.objects.all()
        # uid = request.query_params.get('type', None)
        # if uid is not None:
        #     posts = posts.filter(user_id=uid)
        serializer = DemotionSerializer(demotion, many = True)
        return Response(serializer.data)

    def create(self, request):

        demotion = Demotion.objects.create(
            action=request.data["action"],
            admin=RareUser.objects.get(pk=request.data["admin"]),
            approval= RareUser.objects.get(pk=request.data["approval"]),
            modified_user=RareUser.objects.get(pk=request.data["modified_user"])
        )
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class DemotionSerializer(serializers.ModelSerializer):
    """JSON serializer for RareUsers"""
    class Meta:
        model = Demotion
        fields = ('id', 'admin', 'action', 'approval', 'modified_user')
