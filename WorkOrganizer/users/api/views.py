from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import userDisplaySerializer

class CurrentUserApi(APIView):
    
    def get(self, request):
        serializer = userDisplaySerializer(request.user)
        return Response(serializer.data)