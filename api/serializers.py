from django.forms import widgets
from rest_framework import serializers
from generator.models import Invoice, Item
from pprint import pprint

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('description', 'amount')

class InvoiceSerializer(serializers.ModelSerializer):
	id = serializers.IntegerField(read_only=True)
	items = ItemSerializer(many=True)

	class Meta:
		model = Invoice
		fields = ('id', 'first_name', 'last_name', 'address', 'country', 'email', 'date', 'currency', 'items', 'closed', 'success')

	def create(self, validated_data):
		items_data = validated_data.pop('items')
		invoice = Invoice.objects.create(**validated_data)

		for item_data in items_data:
			Item.objects.create(invoice=invoice, **item_data)
		return invoice