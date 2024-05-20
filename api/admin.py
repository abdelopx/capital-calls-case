from django.contrib import admin
from .models import Bill, CapitalCall, Investor
# Register your models here.

admin.site.register(Investor)
admin.site.register(Bill)
admin.site.register(CapitalCall)