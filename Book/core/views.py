from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,BookSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.


@api_view(['GET','POST'])
def index(request):
	if request.method == 'GET':
		book = Book.objects.all()
		book_serializer = BookSerializer(book,many = True)
		print(book_serializer)
		return Response(book_serializer.data)

	elif request.method == 'POST':
		book_serializer_post = BookSerializer(data = request.data)
		if book_serializer_post.is_valid():
			book_serializer_post.save()
			return Response(book_serializer.data)
		else:
			return Response(book_serializer.errors)



@api_view(['GET','PUT','DELETE'])
def BookDetails(request,key):
	try:
		books = Book.objects.get(id = key)
	except:
		return Response(status = status.HTTP_404_NOT_FOUND)

	# see all the books
	if request.method == 'GET':
		book_serializer = BookSerializer(books)
		return Response(book_serializer.data)

	# Update 
	if request.method == 'PUT':
		bookSerializers = BookSerializer(books,data = request.data)
		if bookSerializers.is_valid():
			bookSerializers.save()
			return Response(bookSerializers.data)
		else:
			return Response(bookSerializers.errors)

	# Delete
	if request.method == 'DELTE':
		books.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)





