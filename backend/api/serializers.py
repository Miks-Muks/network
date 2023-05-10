from rest_framework import serializers

from network.models import TopicKaif, CommentTopic
from users.models import Profile, AddedPhoto, LinksProfile


class TopicKaifSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicKaif
        fields = '__all__'


class CommentTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentTopic
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class AddedPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddedPhoto
        fields = '__all__'


class LinksProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinksProfile
        fields = '__all__'
