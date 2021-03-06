from rest_framework import serializers
from stuff.models import InItem


class InItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)

    class Meta:
        model = InItem
        fields = [
            "id",
            "description",
            "processed",
            "created_date",
            "updated_date"
        ]