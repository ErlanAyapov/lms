from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


USER_ROLE_SELF = 'Guest'

USER_GENDER_SELF = 'Other'

USER_ROLE_CHOICES = (
	(USER_ROLE_SELF, USER_ROLE_SELF),
	('Student', 'Student'),
	('Teacher', 'Teacher'),
	('Super admin', 'Super admin'),
	('Admin', 'Admin')
)

USER_GENDER_CHOICES = (
	(USER_GENDER_SELF, USER_GENDER_SELF),
	('Man', 'Man'),
	('Woman', 'Woman'),
)

User = get_user_model()


def validate_phone_number(value):
	value = str(value)
	if value[0:2] != '+7' or value[0:2] != '87':
		raise ValidationError('Код страны не соответствует!')

	elif len(value) < 10 and len(value) > 13:
		raise ValidationError('Заполнено не корректно!')


class UserCustomer(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	image = models.ImageField(upload_to ='uploads/user/', verbose_name = 'Изоброжение', blank = True)
	phone_number = models.IntegerField()
	user_role 	 = models.CharField(verbose_name='Статус пользователья', choices = USER_ROLE_CHOICES, default=USER_ROLE_SELF, max_length=15, null=True)
	birth_day 	 = models.DateTimeField(verbose_name = 'Дата рождение')
	age 		 = models.IntegerField(verbose_name = 'Возрасть', null=True)
	gender 		 = models.CharField(verbose_name = 'Пол', choices = USER_GENDER_CHOICES, default = USER_GENDER_SELF, max_length = 7, null=True)
	# Не обьязательные
	resume 		= models.FileField(upload_to="uploads/user/resume", blank = True, null = True)
	biography	= models.CharField(verbose_name = 'О себе', max_length=250, blank = True)
	user_ip		= models.CharField(verbose_name = 'IP', max_length = 100, blank = True)
	address		= models.CharField(verbose_name = 'Адрес', max_length = 90, blank = True)
	mail_index	= models.CharField(verbose_name = 'Индекс почты', max_length=15, blank = True)
	# active_course
	# notactive_course
	# university



	def __str__(self):
		return self.user.username
