from django.db import models
from rest_framework import serializers
# Create your models here.


class Book(models.Model):
	Book_Name = models.CharField(max_length  = 30)
	Author = models.CharField(max_length = 40)
	Price = models.IntegerField()
	Discount = models.IntegerField()
	Name_of_person = models.CharField(max_length = 30)
	Age = models.IntegerField()
	Rating = models.IntegerField()
	message = models.CharField(max_length = 200)

	def __str__(self):
		return self.Name_of_person




class BookSerializer(serializers.Serializer):
	Book_Name = serializers.CharField(max_length  = 30)
	Author = serializers.CharField(max_length = 40)
	Price = serializers.IntegerField()
	Discount = serializers.IntegerField()
	Name_of_person = serializers.CharField(max_length = 30)
	Age = serializers.IntegerField()
	Rating = serializers.IntegerField()
	message = serializers.CharField(max_length = 200)


	def create(self,validated_data):
		return Book.objects.create(**validated_data)

	def update(self,book,validated_data):
		newBook = Book(**validated_data)
		newBook.id = book.id
		newBook.save()
		return newBook




