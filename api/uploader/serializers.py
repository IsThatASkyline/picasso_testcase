from rest_framework import serializers


class FileInputSerializer(serializers.Serializer):
    file = serializers.FileField()


class FileOutputSerializer(serializers.Serializer):
    id = serializers.CharField()
    file = serializers.FileField()
    processed = serializers.BooleanField()
