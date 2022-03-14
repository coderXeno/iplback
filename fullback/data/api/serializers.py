from rest_framework import serializers
from data.models import Ipldata, Iplmatcheswondata, Iplmatchesplayedvswon, Ipltopeconomicalbowlers, Iplextrarunsconcededperseason

class IpldataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipldata
        fields = '__all__'

class IplmatcheswondataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iplmatcheswondata
        fields = '__all__'

class IplmatchesplayedvswonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iplmatchesplayedvswon
        fields = '__all__'

class IpltopeconomicalbowlersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ipltopeconomicalbowlers
        fields = '__all__'

class IplextrarunsconcededperseasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Iplextrarunsconcededperseason
        fields = '__all__'