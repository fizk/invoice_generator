from django.conf.urls import include, url
from django.contrib import admin
from api.views import *

urlpatterns = [
	# Login stuff
	url('^auth/', include('rest_framework.urls', namespace='rest_framework')),

	# View list of invoices
	url('^invoice/$', Invoice_generator.as_view()),


]

