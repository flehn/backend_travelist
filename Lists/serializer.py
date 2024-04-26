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



class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = ['id', 'name']  # Remove 'tlist' from fields if it is currently listed

    def create(self, validated_data):
        # Assume `tlist` is handled externally in the ListSerializer
        return Element.objects.create(**validated_data)




class ListSerializer(serializers.ModelSerializer):
    elements = ElementSerializer(many=True)

    class Meta:
        model = TList
        fields = ['id', 'name', 'author', 'is_public', 'elements', 'likes']
        #read_only_fields = ['author']

    def create(self, validated_data):
        elements_data = validated_data.pop('elements', [])
        list_instance = TList.objects.create(**validated_data)

        for element_data in elements_data:
            # Set 'tlist' explicitly here
            Element.objects.create(tlist=list_instance, **element_data)

        return list_instance


    def get_likes_count(self, obj):
        # This method returns the count of likes if likes is a ManyToManyField with User
        return obj.likes.count()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['elements'] = ElementSerializer(instance.elements.all(), many=True).data
        return representation


