from django.db import models


class Feedback(models.Model):
	id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	full_name = models.CharField(max_length=100, verbose_name = 'ФИО')
	email = models.EmailField(verbose_name = 'Адрес почты')
	send_datetime = models.DateTimeField(auto_now_add=True)
	phone_number = models.CharField(max_length=15, verbose_name = 'Номер телефона')

	def __str__(self):
		return self.full_name
