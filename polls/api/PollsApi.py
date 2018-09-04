# coding:utf-8
import logging
from rest_framework.response import Response
from rest_framework import status
from .. import models as m
from rest_framework import serializers, viewsets, decorators
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


class PollsSerializers(serializers.ModelSerializer):
    class Meta:
        module = m.Question
        exc