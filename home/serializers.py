from rest_framework import serializers

class StudentSerializers(serializers.Serializer):

    name = serializers.CharField(max_length=50)
    roll = serializers.IntegerField()
    distict = serializers.CharField(max_length=50)