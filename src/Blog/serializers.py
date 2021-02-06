from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

    date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

 