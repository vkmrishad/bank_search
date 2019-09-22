from django.contrib import admin
from .models import BankBranch

from import_export.admin import ImportExportModelAdmin
from import_export import resources


class BankBranchResource(resources.ModelResource):

    class Meta:
        model = BankBranch
        exclude = ('id',)
        import_id_fields = ('ifsc',)


class BankBranchAdmin(ImportExportModelAdmin):
    resource_class = BankBranchResource


admin.site.register(BankBranch, BankBranchAdmin)
