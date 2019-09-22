from django.db import models


class Bank(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField('Bank Name', max_length=49, null=True, blank=True)

    class Meta:
        verbose_name = 'Bank'
        verbose_name_plural = 'Banks'

    def __str__(self):
        return self.name


class Branch(models.Model):
    ifsc = models.CharField('IFSC', max_length=11)
    bank_id = models.IntegerField('Bank ID', null=True, blank=True)
    branch = models.CharField('Branch', max_length=74,  null=True, blank=True)
    address = models.CharField('Address', max_length=195, null=True,
                               blank=True)
    city = models.CharField('City', max_length=50, null=True, blank=True)
    district = models.CharField('District', max_length=50, null=True,
                                blank=True)
    state = models.CharField('State', max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.branch


class BankBranch(models.Model):
    ifsc = models.CharField('IFSC', max_length=11)
    bank_id = models.IntegerField('Bank ID', null=True, blank=True)
    branch = models.CharField('Branch', max_length=74,  null=True, blank=True)
    address = models.CharField('Address', max_length=195, null=True,
                               blank=True)
    city = models.CharField('City', max_length=50, null=True, blank=True)
    district = models.CharField('District', max_length=50, null=True,
                                blank=True)
    state = models.CharField('State', max_length=50, null=True, blank=True)
    bank_name = models.CharField('Bank Name', max_length=49, null=True,
                                 blank=True)

    class Meta:
        verbose_name = 'Bank Branch'
        verbose_name_plural = 'Bank Branches'

    def __str__(self):
        return self.bank_name
