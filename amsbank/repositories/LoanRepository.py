from abc import ABCMeta, abstractmethod
from typing import List
from amsbank.dto.LoanDto import *
from amsbank.models import Loan

class LoanRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_loan(self, model: GetLoan):
        """Get Loan Object"""
        raise NotImplementedError

    @abstractmethod
    def list_loan(self) -> List[ListLoan]:
        """List Loan Objects"""
        raise NotImplementedError

    @abstractmethod
    def loan_details(self, loan_id: int) -> LoanDetails:
        """Loan Details Object"""
        raise NotImplementedError

    @abstractmethod
    def loan_details_by_account_number(self, account_number: int) -> LoanDetails:
        """Loan Details Object"""
        raise NotImplementedError

    @abstractmethod
    def get_loan_by_account_number(self, account_number: int) -> LoanDetails:
        """loan by account number"""
        raise NotImplementedError

    @abstractmethod
    def pay_loan(self, model: PayLoan):
        """Pay Loan"""
        raise NotImplementedError

    @abstractmethod
    def list_loan_by_account_number(self, account_number: int) -> LoanDetails:
        """Loan Details Object"""
        raise NotImplementedError

    # @abstractmethod
    # def get_amount_by_loan_type(self, account_number: int) -> LoanDetails:
    #     """Loan Amount"""4
    #     raise NotImplementedError

class DjangoORMLoanRepository(LoanRepository):
    def get_loan(self, model: GetLoan):
        loan = Loan()
        loan.account_id = model.account_id
        loan.loan_type = model.loan_type
        loan.loan_amount = model.loan_amount
        loan.loan_balance = model.loan_balance
        loan.loan_status = model.loan_status
        loan.save()

    def list_loan(self) -> List[ListLoan]:
        loans = list(Loan.objects.values('loan_type', 'loan_amount', 'loan_balance', 'loan_status'))
        results: List[ListLoan] = []

        for loan in loans:
            item = ListLoan()
            item.loan_type = loan['loan_type']
            item.loan_amount = loan['loan_amount']
            item.loan_balance = loan['loan_balance']
            item.loan_status = loan['loan_status']
            results.append(item)
        return results

    def loan_details(self, loan_id: int) -> LoanDetails:
        loan = Loan.objects.get(id=loan_id)
        item = LoanDetails()
        item.id = loan.id
        item.loan_type = loan.loan_type
        item.loan_amount = loan.loan_amount
        item.loan_balance = loan.loan_balance
        item.loan_status = loan.loan_status
        return  item

    def loan_details_by_account_number(self, account_number: int) -> List[ListLoan]:
        loan = Loan.objects.values('id', "loan_type", "account__account_number", 'loan_amount', 'loan_balance', 'loan_status', 'account__account_balance').get(account__account_number=account_number)
        item = LoanDetails()
        item.id = loan['id']
        item.loan_type = loan['loan_type']
        item.loan_amount = loan['loan_amount']
        item.loan_balance = loan['loan_balance']
        item.loan_status = loan['loan_status']
        item.account_number = loan['account__account_number']
        item.account_balance = loan['account__account_balance']
        return item

    def get_loan_by_account_number(self, account_number: int) -> LoanDetails:
        loan = loan.objects.values(account_number=model.account_number)
        loan.save()

    def pay_loan(self, model: PayLoan):
        loan = Loan.objects.get(acount_number=model.account_number)
        loan.loan_balance = model.loan_balance
        loan.loan_status = model.loan_status
        loan.loan_amount = model.loan_amount
        loan.save()

    def list_loan_by_account_number(self, account_number: int) -> List[ListLoan]:
        loans = list(Loan.objects.values('loan_type', 'loan_amount', 'loan_balance', 'loan_status', 'account__account_pin').filter(account__account_number=account_number))
        results: List[ListLoan] = []

        for loan in loans:
            item = ListLoan()
            item.loan_type = loan['loan_type']
            item.loan_amount = loan['loan_amount']
            item.loan_balance = loan['loan_balance']
            item.loan_status = loan['loan_status']
            item.account_pin = loan['account__account_pin']
            results.append(item)
        return results

    # def get_amount_by_loan_type(self, account_number: int) -> LoanDetails:
    #     loan = Loan.objects.get(loan_type=model.loan_type)
    #     loan.save()









