from django.contrib import admin
from.models import Account, Customer,Currency, Notification, Receipt, Reward, Transaction, Wallet,Card,Thirdparty,Loan

class CustomerAdmin(admin.ModelAdmin):
    list_display=("firstname","lastname","email","gender","address")
    search_fields=("fistname","lastname","gender","address","email")
admin.site.register(Customer,CustomerAdmin)
class CurrencyAdmin(admin.ModelAdmin):
    list_display=("amount","symbol","country_of_origin")
    search_fields=("amount","country_of_origin")
admin.site.register(Currency,CurrencyAdmin)
class WalletAdmin(admin.ModelAdmin):
    list_display=('pin','status','date','amount','customer','balance')
    search_fields=('status','date','amount','balance')
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=('account_name','account_type','balance','wallet')
    search_fields=('account_name','balance','wallet')
admin.site.register(Account,AccountAdmin)
class TransactionAdmin(admin.ModelAdmin):
    list_display=('wallet','transaction_amount','transaction_type','transaction_charge')
    search_fields=('wallet','transaction_amount','transaction_charge')
admin.site.register(Transaction,TransactionAdmin)
class CardAdmin(admin.ModelAdmin):
    list_display=('date_issued','card_name','card_type')
    search_fields=(" issuer",'card_name')
admin.site.register(Card,CardAdmin)
class ThirdpartyAdmin(admin.ModelAdmin):
    list_display=('account','name','thirdparty_id','phone_number',)
    search_fields=("account",'name')
admin.site.register(Thirdparty,ThirdpartyAdmin)
class NotificationsAdmin(admin.ModelAdmin):
    list_display=('notifications_id','name','date_and_time')
    search_fields=("receipt",'notifications_id')
admin.site.register(Notification,NotificationsAdmin)
class ReceiptAdmin(admin.ModelAdmin):
    list_display=('receipt_type','receipt_date','receipt_file','total_amount','transaction',)
    search_fields=("transaction",'receipt_type')
admin.site.register(Receipt,ReceiptAdmin)
class LoanAdmin(admin.ModelAdmin):
    list_display=('loan_number','loan_type','date_and_time','interest_rate')
    search_fields=("loan_number",'loan_type')
admin.site.register(Loan,LoanAdmin)
class RewardAdmin(admin.ModelAdmin):
    list_display=('transaction','date_and_time','customer_id','gender','bonus',)
    search_fields=("bonus",'date_and_time')
admin.site.register(Reward,RewardAdmin)