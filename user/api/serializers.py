from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only = True,style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password' : {'write_only' :True}
        }
    
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'message' : 'Passwords don\'t match'})
        
        if len(password) < 8:
            raise serializers.ValidationError({'message' : 'Your password is too short'})
        
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise serializers.ValidationError({'message' : 'A email already exits'})
        

        account = User(email = self.validated_data['email'],username = self.validated_data['username'])

        account.set_password(password)
        account.save()
        return account