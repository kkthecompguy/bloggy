from .models import Account
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    password2 = serializers.CharField(style={'input_type: password'}, write_only=True)
    model = Account
    fields = ['email', 'username', 'password']
    extra_kwargs = {
      'password': {'write_only':True}
    }

  def save(self):
    user = Account(
      email=self.validated_data['email'],
      username=self.validated_data['username']
    )
    password = self.validated_data['password']

    user.set_password(password)
    user.save()
    return user


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = ['id', 'email', 'username', 'password'] 