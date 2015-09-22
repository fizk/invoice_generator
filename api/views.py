from django.shortcuts import render
from generator.models import Invoice
from api.serializers import InvoiceSerializer
from django.http import HttpResponseForbidden, Http404
from django.db.models import Max
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ParseError
from rest_framework import status, permissions, serializers

class Invoice_generator(APIView):
	""" Create a new invoice for the invoice generator """

	def get(self, request, format=None):

		#
		# This makes sure ?id=n is the only valid query
		#

		for key in request.GET.keys():
			if key != "id":
				return Response("Error: I only accept 'id' as keyword")

		#
		# parse the query
		#

		try:
			ids_str = request.GET.get('id')
			ids = ids_str.split(',')
		except:
			raise ParseError('Could not parse id')

		try:
			for i in range(0, len(ids)):
				ids[i] = int(ids[i])
		except:
			raise ParseError('Could not convert id numbers to integers.')

		invoice_objs = Invoice.objects.filter(pk__in=ids)
		serializer = InvoiceSerializer(invoice_objs, many=True)

		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = InvoiceSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)
        	
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

