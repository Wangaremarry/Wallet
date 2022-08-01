from django.contrib import admin
from.models import Account, Customer,Currency, Notification, Receipt, Reward, Transaction, Wallet,Card,Thirdparty,Loan

class CustomerAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","email",)
    search_fields=("fistname","lastname")
admin.site.register(Customer)
admin.site.register(Currency)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Thirdparty)
admin.site.register(Notification)
admin.site.register(Loan)
admin.site.register(Reward)
admin.site.register(Receipt)