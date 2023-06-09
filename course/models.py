from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

TASK_TYPE_SELF = 'Test'

TASK_TYPE_CHOICES = (
	(TASK_TYPE_SELF, TASK_TYPE_SELF),
	('Question', 'Question')
)


class Course(models.Model):
	teacher 	= models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = 'Преподаватель', related_name = 'teacher')
	students 	= models.ManyToManyField(User, verbose_name = 'Студенты', blank = True, related_name = 'student')
	title 		= models.CharField('Название курса', max_length = 1000)
	description = models.TextField(verbose_name = 'Описание курса')
	start_time 	= models.DateTimeField(verbose_name = 'Начинается')
	end_time 	= models.DateTimeField(verbose_name = 'Завершается') 

	def __str__(self):
		return self.title

	class Meta:
		verbose_name 		= 'Курс'
		verbose_name_plural = 'Курсы'


class Lesson(models.Model):
	course 		= models.ForeignKey(Course, verbose_name = 'Курс', on_delete = models.CASCADE)
	start_time 	= models.DateTimeField(verbose_name = 'Начинается')
	end_time 	= models.DateTimeField(verbose_name = 'Завершается')
	title 		= models.CharField('Тема урока', max_length = 1000) 

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
	question 		= models.CharField(verbose_name = 'Вопрос', max_length = 1000)
	type_t  			= models.CharField(verbose_name = 'Тип заданий', choices = TASK_TYPE_CHOICES, default = TASK_TYPE_SELF, max_length = 1000)

	# Тип заданий ТЕСТ
	true_answer 	= models.CharField(verbose_name = 'Правильный вариант', max_length = 200, blank = True)
	false_answer_1 	= models.CharField(verbose_name = 'Дополнительный вариант 1', max_length = 200, blank = True)
	false_answer_2 	= models.CharField(verbose_name = 'Дополнительный вариант 2', max_length = 200, blank = True)
	false_answer_3 	= models.CharField(verbose_name = 'Дополнительный вариант 3', max_length = 200, blank = True)

	# Тип заданий ВОПРОС
	answer 			= models.CharField(verbose_name = 'Правильный ответ', max_length = 200, blank = True)

	def __str__(self):
		return f'{self.type_} | {self.question}'

	class Meta:
		verbose_name 		= 'Задание'
		verbose_name_plural = 'Заданий'