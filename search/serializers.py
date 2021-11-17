from rest_framework import serializers
from .models import Meibo

class MeiboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meibo
        exclude = ('id',)
