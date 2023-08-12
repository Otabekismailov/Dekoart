from rest_framework import serializers
from .models import User
import re

pattern = r'^\+998[0-9]{9}$'


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, max_length=8, style={"input_type": "password"}, write_only=True)
    phone = serializers.CharField(min_length=13, max_length=13)

    class Meta:
        model = User
        fields = ['phone', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(phone=self.validated_data['phone'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        phone = self.validated_data['phone']
        is_matched = re.match(pattern, phone)

        if is_matched:
            if phone.startswith("+"):
                demo = phone.strip('+')
                if demo.isdigit():
                    pass
                else:
                    raise serializers.ValidationError(
                        'phone', "There is a character or letter inside the number"
                    )

            else:
                raise serializers.ValidationError(
                    'phone', "The number is not prefixed with +"
                )
        else:
            raise serializers.ValidationError(
                'phone', "The phone number does not match the format"
            )

        if password != password2:
            raise serializers.ValidationError('Passwords must match.')
        user.set_password(password)
        user.save()

        return user


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("phone", "password")
