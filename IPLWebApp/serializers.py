from rest_framework import serializers
from .models import Banglore, chennai, mumbai, delhi, kolkata, punjab, rajasthan, hyderabad


class BangloreSerializer(serializers.ModelSerializer):
    class Meta:
        models = Banglore
        fields = [ 'id','player_name', 'role', 'price', 'status', 'team']


class ChennaiSerializer(serializers.ModelSerializer):
    class Meta:
        models = chennai
        fields = ['id', 'player_name', 'role', 'price', 'status', 'team']


class MumbaiSerializer(serializers.ModelSerializer):
    class Meta:
        models = mumbai
        fields = ['id', 'player_name', 'role', 'price', 'status', 'team']


class DelhiSerializer(serializers.ModelSerializer):
    class Meta:
        models = delhi
        fields = ['id', 'player_name', 'role', 'price', 'status', 'team']


class KolkataSerializer(serializers.ModelSerializer):
    class Meta:
        models = kolkata
        fields = ['id', 'player_name', 'role', 'price', 'status', 'team']


class RajasthanSerializer(serializers.ModelSerializer):
    class Meta:
        models = rajasthan
        fields = ['id', 'player_name', 'role', 'price', 'status', 'team']

class PunjabSerializer(serializers.ModelSerializer):
    class Meta:
        models = punjab
        fields = ['id', 'player_name', 'role', 'price', 'status', 'team']


class HyderabadSerializer(serializers.ModelSerializer):
    class Meta:
        models = hyderabad
        fields = ['id', 'player_name', 'role', 'price', 'status', 'team']