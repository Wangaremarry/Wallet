from django.urls import path
from .views import register_account, register_card, register_currency, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_transaction, register_wallet

urlpatterns = [
    path("register/",register_customer, name="registration"),
]
urlpatterns = [
    path("currency/",register_currency, name="registration"),
]
urlpatterns = [
    path("wallet/",register_wallet, name="register_wallet"),
]
urlpatterns = [
    path("account/",register_account, name="registration"),
]
urlpatterns = [
    path("receipt/",register_receipt, name="registration"),
]
urlpatterns = [
    path("reward/",register_reward, name="registration"),
]
urlpatterns = [
    path("notification/",register_notification, name="registration"),
]
urlpatterns = [
    path("thirdparty/",register_thirdparty, name="registration"),
]
urlpatterns = [
    path("card/",register_card, name="registration"),
]
urlpatterns = [
    path("transaction/",register_transaction, name="registration"),
]
urlpatterns = [
    path("loan/",register_loan, name="registration"),
]