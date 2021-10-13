from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


from stuff.models import InItem
from stuff.serializers import InItemSerializer

class InItemDetailApiView(APIView):

    def get_object(self, pk):
        return get_object_or_404(InItem, pk=pk)
    
    def get(self, request, pk):
        in_item = self.get_object(pk=pk)
        serializer = InItemSerializer(in_item)
        return Response(serializer.data)