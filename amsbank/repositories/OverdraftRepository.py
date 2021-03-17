from abc import ABCMeta, abstractmethod
from pyexpat import model
from typing import List

from amsbank.dto.OverdraftDto import *
from amsbank.models import Overdraft


class OverdraftRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_overdraft(self, model: GetOverdraft):
        """Get Overdraft"""
        raise NotImplementedError

    @abstractmethod
    def list_overdraft(self) -> List[ListOverdraft]:
        """List Overdraft"""
        raise NotImplementedError

    @abstractmethod
    def overdraft_details(self, overdraft_id: int) -> OverdraftDetails:
        """Overdraft Details"""
        raise NotImplementedError

    @abstractmethod
    def get_overdraft_by_account_number(self, account_number: int) -> OverdraftDetails:
        """Get Overdraft By Account Number"""
        raise NotImplementedError

    @abstractmethod
    def get_overdraft_details_by_account_number(self, account_number: int) -> OverdraftDetails:
        """Get Overdraft Details By Account Number"""
        return NotImplementedError


class DjangoORMOverdraftRepository(OverdraftRepository):
    def get_overdraft(self, model: GetOverdraft):
        overdraft = Overdraft()
        overdraft.account_id = model.account_id
        overdraft.overdraft_amount = model.overdraft_amount
        overdraft.overdraft_balance = model.overdraft_balance
        overdraft.overdraft_status = model.overdraft_status
        overdraft.save()

    def list_overdraft(self) -> List[ListOverdraft]:
        overdrafts = list(Overdraft.objects.values('overdraft_status', 'overdraft_balance', 'overdraft_amount', ))
        results: List[ListOverdraft] = []

        for overdraft in overdrafts:
            item = ListOverdraft()
            item.overdraft_status = overdraft['overdraft_status']
            item.overdraft_balance = overdraft['overdraft_balance']
            item.overdraft_amount = overdraft['overdraft_amount']
            results.append(item)
        return results

    def overdraft_details(self, overdraft_id: int) -> OverdraftDetails:
        overdraft = Overdraft.objects.get(overdraft_id)
        item = OverdraftDetails()
        item.id = overdraft['id']
        item.overdraft_amount = overdraft['overdraft_amount']
        item.overdraft_balance = overdraft['overdraft_balance']
        item.overdraft_status = overdraft['overdraft_status']
        item.account_number = overdraft['account__number']
        return item

    def get_overdraft_by_account_number(self, account_number: int) -> OverdraftDetails:
        overdraft = Overdraft.objects.values(account_number=model.account_number)
        overdraft.save()

    def get_overdraft_details_by_account_number(self, account_number: int) -> OverdraftDetails:
        overdraft = Overdraft.objects.values('id', "account__account_number", 'overdraft_amount', 'overdraft_balance',
                                             'overdraft_status', ).get(
            account__account_number=account_number)
        item = OverdraftDetails()
        item.id = overdraft['id']
        item.overdraft_status = overdraft['overdraft_status']
        item.overdraft_amount = overdraft['overdraft_amount']
        item.overdraft_balance = overdraft['overdraft_balance']
        item.account_number = overdraft['account__account_number']
        return item
