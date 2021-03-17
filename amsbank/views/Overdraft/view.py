# from django.http import HttpRequest
# from django.shortcuts import redirect, render
#
# from amsbank.dto.OverdraftDto import *
# from amsbank.service_provider import ams_service_provider
# from  amsbank.dto.AccountDto import DepositAndWithdraw
#
#
# def get_overdraft(request):
#     context = {
#
#     }
#     pass
#
#
# def __create_if_post_method(request, context):
#     if request.method == 'POST':
#         try:
#             overdraft = __get_overdraft_attribute_from_request(request)
#             account = ams_service_provider.account_management_service().get_account_with_account_number(account_number=overdraft.account_number)
#             try:
#                 if account.account_pin == int(overdraft.account_pin):
#                    overdraft.overdraft_amount = overdraft.overdraft_amount
#                    overdraft.overdraft_balance = overdraft.overdraft_amount
#                    overdraft.overdraft_status = 'active'
#                    ams_service_provider.overdraft_management_service().get_overdraft(overdraft)
#                    __get_new_amount_for_overdraft(account.account_balance, account.account_number, overdraft.overdraft_amount)
#
#
# def __get_new_amount_for_overdraft(account_balance: float, account_number: int, amount: float):
#     transactions =  DepositAndWithdraw()
#     transactions.account_balance = __get_new_balance_on_overdraft(amount, account_balance)
#     ams_service_provider.account_management_service().deposit_or_withdrawal(transactions)
#
#
# def __get_new_balance_on_overdraft(amount: float, account_balance):
#     new_balance = account_balance - amount
#     return new_balance
#
# def __get_overdraft_attribute_from_request(request: HttpRequest):
#     get_overdraft_dto = GetOverdraft()
#     get_overdraft_dto.account_number = request.POST['account_number']
#     get_overdraft_dto.overdraft_amount = request.POST['overdraft_amount']
#     get_overdraft_dto.account_pin = request.POST['account_pin']
#     return get_overdraft_dto
