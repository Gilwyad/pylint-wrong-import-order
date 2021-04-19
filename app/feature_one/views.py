from feature_one.models import Area
from django.shortcuts import render

from django.contrib.auth.models import Permission
from django.db.transaction import atomic
from django.db.utils import IntegrityError

# Create your views here.
