# -*- coding: utf-8 -*-

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.core.urlresolvers import reverse
from generator.models import *
from rest_framework import status
from rest_framework.test import APITestCase

from datetime import date, datetime
import sys
from pprint import pprint

reload(sys)  
sys.setdefaultencoding('utf8')

def  _test_id():  
    ''' This is a helper function to test if id is a field in the JSON object returned'''
    try:
        Invoice.objects.get().id
        return True
    except AttributeError:
        return False

class InvoiceTests(APITestCase):
    def test_create_invoice_correct(self):
        """
        Ensure we can create a new invoice object.
        """

        url = '/v1/invoice/'

        data =  {
            "first_name": "Julia",
            "last_name": "Ilin",
            "address": "Madurastraat 93",
            "country": "The Netherlands",
            "email": "julia@julia.nl",
            "date": "2014-03-14",
            "currency": "BTC",
            "items": [
            {
                "description": "BTC",
                "amount": 2500
            },
            {
                "description": "BTC",
                "amount": 4500
            }
             ]
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) #General stuff
        self.assertEqual(Invoice.objects.count(), 1)
        
        self.assertTrue(_test_id())                                        #Check different fields
        self.assertEqual(Invoice.objects.get().first_name, 'Julia')
        self.assertEqual(Invoice.objects.get().last_name, 'Ilin')
        self.assertEqual(Invoice.objects.get().address, 'Madurastraat 93')
        self.assertEqual(Invoice.objects.get().country, 'The Netherlands')
        self.assertEqual(Invoice.objects.get().email, 'julia@julia.nl')
        self.assertEqual(Invoice.objects.get().currency, 'BTC')

        self.assertEqual(Invoice.objects.get().items.count(), 2) #Check that the items are correct. This code looks weird because we need to go deep to get the values
        self.assertEqual(Invoice.objects.get().items.all().values_list()[0][2], 'BTC') 
        self.assertEqual(Invoice.objects.get().items.all().values_list()[0][3], 2500)
        self.assertEqual(Invoice.objects.get().items.all().values_list()[1][2], 'BTC') 
        self.assertEqual(Invoice.objects.get().items.all().values_list()[1][3], 4500)

        self.assertEqual(Invoice.objects.get().date.year, 2014) #Check the date
        self.assertEqual(Invoice.objects.get().date.month, 3)
        self.assertEqual(Invoice.objects.get().date.day, 14)

        self.assertEqual(Invoice.objects.get().closed, False) #ensure the fields that are not sent by the user are generated correctly
        self.assertEqual(Invoice.objects.get().success, False)


    def test_create_invoice_no_date(self):
        """
        Ensure we can create a new invoice object with no date given. Should put in current date
        """

        url = '/v1/invoice/'

        data =  {
            "first_name": "Julia",
            "last_name": "Ilin",
            "address": "Madurastraat 93",
            "country": "The Netherlands",
            "email": "julia@julia.nl",
            "currency": "BTC",
            "items": [
            {
                "description": "BTC",
                "amount": 2500
            },
            {
                "description": "BTC",
                "amount": 4500
            }
             ]
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) #General stuff
        self.assertEqual(Invoice.objects.count(), 1)

        self.assertTrue(_test_id())                                 #Check different fields
        self.assertEqual(Invoice.objects.get().first_name, 'Julia') 
        self.assertEqual(Invoice.objects.get().last_name, 'Ilin')
        self.assertEqual(Invoice.objects.get().address, 'Madurastraat 93')
        self.assertEqual(Invoice.objects.get().country, 'The Netherlands')
        self.assertEqual(Invoice.objects.get().email, 'julia@julia.nl')
        self.assertEqual(Invoice.objects.get().currency, 'BTC')

        self.assertEqual(Invoice.objects.get().items.count(), 2) #Check that the items are correct. This code looks weird because we need to go deep to get the values
        self.assertEqual(Invoice.objects.get().items.all().values_list()[0][2], 'BTC') 
        self.assertEqual(Invoice.objects.get().items.all().values_list()[0][3], 2500)
        self.assertEqual(Invoice.objects.get().items.all().values_list()[1][2], 'BTC') 
        self.assertEqual(Invoice.objects.get().items.all().values_list()[1][3], 4500)

        self.assertEqual(Invoice.objects.get().date.year, datetime.now().year) #Check that the date is the current date
        self.assertEqual(Invoice.objects.get().date.month, datetime.now().month)
        self.assertEqual(Invoice.objects.get().date.day, datetime.now().day)

        self.assertEqual(Invoice.objects.get().closed, False) #ensure the fields that are not sent by the user are generated correctly
        self.assertEqual(Invoice.objects.get().success, False)

    def test_create_invoice_strange_letters(self):
        """
        Ensure we can create a new invoice object with strange alphabets, Chinese, Greek, Japanese, Icelandic and Russian.
        """

        url = '/v1/invoice/'

        data =  {
            "first_name": "正體字/繁體字",
            "last_name": "Πλἀτων",
            "address": "日本語",
            "country": "þæöðáó",
            "email": "русский язык",
            "date": "2014-03-14",
            "currency": "BTC",
            "items": [
            {
                "description": "BTC",
                "amount": 2500
            },
            {
                "description": "BTC",
                "amount": 4500
            }
             ]
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED) #General stuff
        self.assertEqual(Invoice.objects.count(), 1)

        self.assertTrue(_test_id())                                       #Check different fields 
        self.assertEqual(Invoice.objects.get().first_name, '正體字/繁體字') 
        self.assertEqual(Invoice.objects.get().last_name, 'Πλἀτων')
        self.assertEqual(Invoice.objects.get().address, '日本語')
        self.assertEqual(Invoice.objects.get().country, 'þæöðáó')
        self.assertEqual(Invoice.objects.get().email, 'русский язык')
        self.assertEqual(Invoice.objects.get().currency, 'BTC')

        self.assertEqual(Invoice.objects.get().items.count(), 2) #Check that the items are correct. This code looks weird because we need to go deep to get the values
        self.assertEqual(Invoice.objects.get().items.all().values_list()[0][2], 'BTC') 
        self.assertEqual(Invoice.objects.get().items.all().values_list()[0][3], 2500)
        self.assertEqual(Invoice.objects.get().items.all().values_list()[1][2], 'BTC') 
        self.assertEqual(Invoice.objects.get().items.all().values_list()[1][3], 4500)

        self.assertEqual(Invoice.objects.get().date.year, 2014) #Check the date
        self.assertEqual(Invoice.objects.get().date.month, 3)
        self.assertEqual(Invoice.objects.get().date.day, 14)

        self.assertEqual(Invoice.objects.get().closed, False) #ensure the fields that are not sent by the user are generated correctly
        self.assertEqual(Invoice.objects.get().success, False)

    def test_create_invoice_with_closed(self):
        """
        Ensure we can't send "closed" field'.
        """

        url = '/v1/invoice/'

        data =  {
            "first_name": "Julia",
            "last_name": "Ilin",
            "address": "Madurastraat 93",
            "country": "The Netherlands",
            "email": "julia@julia.nl",
            "date": "2014-03-14",
            "currency": "BTC",
            "items": [
            {
                "description": "BTC",
                "amount": 2500
            },
            {
                "description": "BTC",
                "amount": 4500
            }
             ],
             "closed": True
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["detail"], 'Error: JSON object contains an invalid field')

    def test_create_invoice_with_success(self):
        """
        Ensure we can't send "success" field'.
        """

        url = '/v1/invoice/'

        data =  {
            "first_name": "Julia",
            "last_name": "Ilin",
            "address": "Madurastraat 93",
            "country": "The Netherlands",
            "email": "julia@julia.nl",
            "date": "2014-03-14",
            "currency": "BTC",
            "items": [
            {
                "description": "BTC",
                "amount": 2500
            },
            {
                "description": "BTC",
                "amount": 4500
            }
             ],
             "success": True
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["detail"], 'Error: JSON object contains an invalid field')

    def test_create_invoice_missing_first_name(self):
        """
        Ensure we can't send a request with a missing field that is required. 
        """

        url = '/v1/invoice/'

        data =  { 
            "last_name": "Ilin",
            "address": "Madurastraat 93",
            "country": "The Netherlands",
            "email": "julia@julia.nl",
            "date": "2014-03-14",
            "currency": "BTC",
            "items": [
            {
                "description": "BTC",
                "amount": 2500
            },
            {
                "description": "BTC",
                "amount": 4500
            }
             ]
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['first_name'][0], 'This field is required.')


    def test_get_invoice(self):
        """
        Ensure we can get a new invoice object.
        """

        url = '/v1/invoice/'

        data =  {
            "first_name": "Julia",
            "last_name": "Ilin",
            "address": "Madurastraat 93",
            "country": "The Netherlands",
            "email": "julia@julia.nl",
            "date": "2014-03-14",
            "currency": "BTC",
            "items": [
            {
                "description": "BTC",
                "amount": 2500
            },
            {
                "description": "BTC",
                "amount": 4500
            }
             ]
        }

        post_response = self.client.post(url, data, format='json')
        response = self.client.get("/v1/invoice/?id=" + str(Invoice.objects.get().id)) 

        pprint(response.data)
        pprint(response.status_code)

        self.assertEqual(response.status_code, 200) #General stuff
        self.assertEqual(Invoice.objects.count(), 1)
        
        # self.assertTrue(_test_id())                                        #Check different fields
        # self.assertEqual(Invoice.objects.get().first_name, 'Julia')
        # self.assertEqual(Invoice.objects.get().last_name, 'Ilin')
        # self.assertEqual(Invoice.objects.get().address, 'Madurastraat 93')
        # self.assertEqual(Invoice.objects.get().country, 'The Netherlands')
        # self.assertEqual(Invoice.objects.get().email, 'julia@julia.nl')
        # self.assertEqual(Invoice.objects.get().currency, 'BTC')

        # self.assertEqual(Invoice.objects.get().items.count(), 2) #Check that the items are correct. This code looks weird because we need to go deep to get the values
        # self.assertEqual(Invoice.objects.get().items.all().values_list()[0][2], 'BTC') 
        # self.assertEqual(Invoice.objects.get().items.all().values_list()[0][3], 2500)
        # self.assertEqual(Invoice.objects.get().items.all().values_list()[1][2], 'BTC') 
        # self.assertEqual(Invoice.objects.get().items.all().values_list()[1][3], 4500)

        # self.assertEqual(Invoice.objects.get().date.year, 2014) #Check the date
        # self.assertEqual(Invoice.objects.get().date.month, 3)
        # self.assertEqual(Invoice.objects.get().date.day, 14)

        # self.assertEqual(Invoice.objects.get().closed, False) #ensure the fields that are not sent by the user are generated correctly
        # self.assertEqual(Invoice.objects.get().success, False)

