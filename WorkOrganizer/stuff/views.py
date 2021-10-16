from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from stuff.permissions import IsAuthorOrFuckOff


from stuff.models import InItem
from stuff.serializers import InItemSerializer

class InItemDetailApiView(APIView):
    permission_classes = [IsAuthenticated, IsAuthorOrFuckOff]

    def get_object(self, pk):
        return get_object_or_404(InItem, pk=pk)
    
    def get(self, request, pk):
        in_item = self.get_object(pk=pk)
        serializer = InItemSerializer(in_item)
        return Response(serializer.data)

class InItemListApiView(APIView):
    permission_classes = [IsAuthenticated, IsAuthorOrFuckOff]
    
    def get(self, request):
        in_items = InItem.objects.filter(author=request.user)
        serializer = InItemSerializer(in_items, manu=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InItem(data=request.data['content'])
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=Http404)
