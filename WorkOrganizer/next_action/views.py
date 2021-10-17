from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from stuff.permissions import IsAuthorOrFuckOff
from rest_framework import status

from next_action.models import Project, Context, NextAction
from next_action.serializers import NextActionSerializer, ProjectSerializer, ContextSerializer





class NextActionDetailApiView(APIView):
    permission_classes = [IsAuthenticated, IsAuthorOrFuckOff]

    def get_object(self, pk):
        return get_object_or_404(NextAction, pk=pk)
    
    def get(self, request, pk):
        next_action = self.get_object(pk=pk)
        serializer = NextActionSerializer(next_action)
        return Response(serializer.data)

    def put(self, request, pk):
        next_action = self.get_object(pk=pk)
        serializer = NextActionSerializer(next_action, data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NextActionListApiView(APIView):
    permission_classes = [IsAuthenticated, IsAuthorOrFuckOff]
    
    def get(self, request):
        next_actions = NextAction.objects.filter(author=request.user)
        serializer = NextActionSerializer(next_actions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NextAction(data=request.data['content'])
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
