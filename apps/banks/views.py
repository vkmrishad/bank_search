
from django.db.models import Q
from rest_framework import viewsets


from .models import BankBranch
from .serializers import BankBranchSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = BankBranch.objects.all()
    serializer_class = BankBranchSerializer

    def get_queryset(self):
        queryset = BankBranch.objects.all()
        ifsc = self.request.query_params.get('ifsc', None)

        if ifsc is not None:
            queryset = queryset.filter(ifsc__icontains=ifsc)
        else:
            return []

        return queryset


class BranchViewSet(viewsets.ModelViewSet):
    queryset = BankBranch.objects.all()
    serializer_class = BankBranchSerializer

    def get_queryset(self):
        queryset = BankBranch.objects.all()
        bank_name = self.request.query_params.get('bank_name', None)
        city = self.request.query_params.get('city', None)

        if bank_name is not None and city is not None:
            queryset = queryset.filter(
                Q(bank_name__icontains=bank_name) &
                Q(city__icontains=city),
            )
        else:
            return []

        return queryset
