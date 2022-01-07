from rest_framework import serializers
from .models import File, Work

class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = ['id', 'proprietary_id', 'iswc', 'source', 'title', 'contributors']
