from pyexpat import model
from rest_framework import serializers
from api.models import Person, Update

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("id", "username", "stars")

