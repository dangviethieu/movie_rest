from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Avg
from .models import Movie, Comment, Vote


class MovieSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()

    class Meta:
        model = Movie
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        representation['owner'] = UserSerializer(instance.owner).data
        representation['star'] = instance.votes.all().aggregate(star=Avg('start'))['star'] or 0
        return representation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ('id', 'text', 'created_at', 'updated_at', 'owner')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = UserSerializer(instance.owner).data
        return representation

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'
        read_only_fields = ('id', 'movie', 'owner')

    def create(self, validated_data):
        if Vote.objects.filter(owner=validated_data['owner'], movie_id=validated_data['movie_id']).exists():
            raise serializers.ValidationError('You can vote only once')
        return super().create(validated_data)
