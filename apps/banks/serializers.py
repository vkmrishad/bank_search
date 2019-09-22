
from .models import BankBranch

from rest_framework import serializers


class BankBranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = BankBranch
        fields = '__all__'
