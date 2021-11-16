from rest_framework import serializers
from next_action.models import NextAction, Project, Context

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "goal",
            "actions",
            "done",
            "created",
            "author"
        ]

class NextActionReadSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    author = serializers.StringRelatedField(read_only=True)
    project = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NextAction
        fields = [
            "id",
            "description",
            "done",
            "context",
            "created",
            "author",
            "project"
        ]

class NextActionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = NextAction
        fields = [
            "id",
            "description",
            "done",
            "context",
            "created",
            "author",
            "project"
        ]
        
class ContextSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Context
        fields = [
            "id",
            "name",
            "author",
            "created",
        ]

