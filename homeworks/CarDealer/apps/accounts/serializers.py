from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from apps.accounts.models import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['username'], )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
        username = serializers.CharField()
        password = serializers.CharField()

        def validate(self, data):
            user = authenticate(**data)
            if user and user.is_active:
                return user
            raise serializers.ValidationError("Incorrect Credentials")




    # class CommentSerializer(serializers.Serializer):
    #     email = serializers.EmailField()
    #     content = serializers.CharField(max_length=200)
    #     created = serializers.DateTimeField()
    #
    #     def create(self, validated_data):
    #         return Comment(**validated_data)
    #
    #     def update(self, instance, validated_data):
    #         instance.email = validated_data.get('email', instance.email)
    #         instance.content = validated_data.get('content', instance.content)
    #         instance.created = validated_data.get('created', instance.created)
    #         return instance






# class UserDetailsSerializer(serializers.ModelSerializer):
#     """
#     User model w/o password
#     """
#     class Meta:
#         model = UserModel
#         fields = ('pk', 'username', 'email', 'first_name', 'last_name')
#         read_only_fields = ('email', )