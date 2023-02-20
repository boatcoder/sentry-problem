import logging

from email import message
from django.shortcuts import render

# Create your views here.
logger = logging.getLogger(__name__)

def boom(request):
    logger.error('This is before the boom')
    request.GET["foo"] = message
    logger.error('This is after the boom')
