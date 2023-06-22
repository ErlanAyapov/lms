from django.db import models
from django.contrib.auth import get_user_model
from members.models import UserCustomer, USER_ROLE_SELF
from django.core.exceptions import ValidationError


User = get_user_model()

TASK_TYPE_SELF = 'Test'

TASK_TYPE_CHOICES = (
	(TASK_TYPE_SELF, TASK_TYPE_SELF),
	('Question', 'Question')
)
# |==============================|
# |=		 Validators			=|
# |==============================|
def user_is_student(user):
	# print(user.usercustomer.user_role)

	if not isinstance(user, User):
		raise ValidationError("Invalid User object.")
	if not hasattr(user, 'usercustomer'):
		raise ValidationError("User is not associated with UserCustomer.")
	if not user.usercustomer.user_role:
		raise ValidationError("User role is required.")
	elif user.usercustomer.user_role == 'Student':
		print(user.usercustomer.user_role)
		return True
	else:
		raise ValidationError("User is not a student.")

def user_is_teacher(user):
	print(user.usercustomer.user_role)
	print(user.usercustomer) 

	if not isinstance(user, User):
		raise ValidationError("Invalid User object.")
	if not hasattr(user, 'usercustomer'):
		raise ValidationError("User is not associated with UserCustomer.")
	if not user.usercustomer.user_role:
		raise ValidationError("User role is required.")
	elif user.usercustomer.user_role == 'Teacher':
		print(user.usercustomer.user_role)
		return True
	else:
		raise ValidationError("User is not a teacher.")



# |==============================|
# |=		 Models				=|
# |==============================|
class Course(models.Model):
	id 			= models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	teachers 	= models.ManyToManyField(User, verbose_name = 'Преподаватель', related_name = 'teacher')
	students 	= models.ManyToManyField(User, verbose_name = 'Студенты', blank = True, related_name = 'student')
	title 		= models.CharField('Название курса', max_length = 1000)
	description = models.TextField(verbose_name = 'Описание курса')
	start_time 	= models.DateTimeField(verbose_name = 'Начинается')
	end_time 	= models.DateTimeField(verbose_name = 'Завершается')
	price 		= models.IntegerField(verbose_name = 'Цена курса')

	def __str__(self):
		return self.title

	# def clean(self):
	# 	for teacher in self.teachers.all():
	# 		user_is_teacher(teacher)
	# 	for student in self.students.all():
	# 		user_is_student(student)

	# def save(self, *args, **kwargs):
	# 	self.full_clean()  # Run full validation before saving
	# 	super().save(*args, **kwargs)

	class Meta:
		verbose_name 		= 'Курс'
		verbose_name_plural = 'Курсы'


class Lesson(models.Model):
	course 		= models.ForeignKey(Course, verbose_name = 'Курс', on_delete = models.CASCADE)
	start_time 	= models.DateTimeField(verbose_name = 'Начинается')
	end_time 	= models.DateTimeField(verbose_name = 'Завершается')
	title 		= models.CharField('Тема урока', max_length = 200) 

	def __str__(self):
		return self.title

	class Meta:
		verbose_name 		= 'Урок'
		verbose_name_plural = 'Уроки' 


class Lecture(models.Model):
	lesson 		= models.ForeignKey(Lesson, verbose_name = 'Урок', on_delete = models.CASCADE)
	title 		= models.CharField(verbose_name = 'Тема', max_length = 250)
	description = models.TextField(verbose_name = 'Содержимое')

	def __str__(self):
		return self.title

	class Meta:
		verbose_name 		= 'Лекция'
		verbose_name_plural = 'Лекций'


class Task(models.Model):
	lesson 		= models.ForeignKey(Lesson, verbose_name = 'Урок', on_delete = models.CASCADE)
	question	= models.CharField(verbose_name = 'Вопрос', max_length = 1000)
	type_t		= models.CharField(verbose_name = 'Тип заданий', choices = TASK_TYPE_CHOICES, default = TASK_TYPE_SELF, max_length = 1000)

	# Тип заданий ТЕСТ
	true_answer 	= models.CharField(verbose_name = 'Правильный вариант', max_length = 200, blank = True)
	false_answer_1 	= models.CharField(verbose_name = 'Дополнительный вариант 1', max_length = 200, blank = True)
	false_answer_2 	= models.CharField(verbose_name = 'Дополнительный вариант 2', max_length = 200, blank = True)
	false_answer_3 	= models.CharField(verbose_name = 'Дополнительный вариант 3', max_length = 200, blank = True)

	# Тип заданий ВОПРОС
	answer 			= models.CharField(verbose_name = 'Правильный ответ', max_length = 200, blank = True)

	def __str__(self):
		return f'{self.type_t} | {self.question}'

	class Meta:
		verbose_name 		= 'Задание'
		verbose_name_plural = 'Заданий'