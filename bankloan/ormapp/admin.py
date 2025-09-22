from django.contrib import admin 
from.models import Loan
class LoanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Loan,LoanAdmin)