from reFree.models import User,Follow,Company,Projects,Like,Component,FinalDesign,SocialLinks
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        #fields = ['user', 'name','link']
        fields = '__all__'

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class ComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Component
        fields = '__all__'

class FinalDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalDesign
        fields = '__all__'

