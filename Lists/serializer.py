"""
Serializers allow complex data types like querysets and model instances to be converted to native Python datatypes 
that can then be easily rendered into JSON, XML, or other content types.

After installing the required packages, we can start building the API endpoints in Django.
We will create a new Django app to handle the API requests. 
The API endpoint will return JSON data when we make HTTP requests to it. 
We can use Django Rest Framework to build the API endpoints.

"""

from rest_framework import serializers
from .models import TList, Element


'''
Example of an Serializer that creates a JSON object for a 
database request from the model Post that returns title and content.
'''

class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=500)

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ['id', 'name', 'tlist']  

class ListSerializer(serializers.ModelSerializer):
    #include a nested ElementSerializer. This will allow to serialize the elements related to each list.
    #elements = ElementSerializer(many=True, read_only=True)

    class Meta:
        model = TList
        fields = ['id', 'name', 'author'] 