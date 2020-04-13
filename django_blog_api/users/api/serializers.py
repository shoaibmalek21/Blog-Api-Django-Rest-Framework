from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
from django.contrib.auth import get_user_model
from rest_framework.serializers import CharField, EmailField, ValidationError
from django.db.models import Q

User = get_user_model()

class UserCreationSerializer(ModelSerializer):
	email = EmailField(label='Email Address')
	email2 = EmailField(label='Confirm Email')
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',
		]

		extra_kwargs = {
			'password':{'write_only': True}
		}


	def validate(self, data):
		# email = data['email']
		# user_email = User.objects.filter(email=email)
		# if user_email.exists():
		# 	raise ValidationError('This user has Already Registered.')
		return data

	def validate_email(self, value):
		data = self.get_initial()
		email1 = data.get('email2')
		email2 = value
		if email1 != email2:
			raise ValidationError('Emails Must Match')

		user_email = User.objects.filter(email=email2)
		if user_email.exists():
			raise ValidationError('This user email has Already Registered.')
		
		return value

	def validate_email2(self, value):
		data = self.get_initial()
		email1 = data.get('email')
		email2 = value
		if email1 != email2:
			raise ValidationError('Emails Must Match')
		return value

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user_data = User(
				username = username,
				email = email
			) 
		user_data.set_password(password)
		user_data.save()
		return validated_data


class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField(allow_blank=True, required=False)
	email = EmailField(label='Email Address', allow_blank=True, required=False)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'token',
		]

		extra_kwargs = {
			'password':{'write_only': True}
		}


	def validate(self, data):
		user_data = None
		email = data.get('email', None)
		username = data.get('username', None)
		password = data['password']

		if not email and not username:
			raise ValidationError('Username or Email is required to Login.')

		user = User.objects.filter(
				Q(email=email)|
				Q(username=username)
			).distinct()
		user = user.exclude(email__isnull=True).exclude(email__iexact='')

		if user.exists() and user.count() == 1:
			user_data = user.first()
		else:
			raise ValidationError("This username/email is not valid.")

		if user_data:
			if not user_data.check_password(password):
				raise ValidationError('Incorrect password please try Again.')

		data["token"] = 'Some Random Token'
		return data

