from django.contrib.auth import get_user_model
from rest_framework import exceptions
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email', 'role', 'first_name',
                  'last_name', 'username', 'bio')
        model = User


class TokenSerializer(serializers.Serializer):
    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        email = attrs.get('email', '')
        confirmation_code = attrs.get('confirmation_code', '')

        users = User.objects.filter(
            email=email,
            confirmation_code=confirmation_code
        )

        validated_data = {}
        if users.exists():
            curr_user = users.first()
            refresh = self.get_token(curr_user)

            validated_data['refresh'] = str(refresh)
            validated_data['access'] = str(refresh.access_token)
            return validated_data

        raise exceptions.AuthenticationFailed('Failed to authenticate')
