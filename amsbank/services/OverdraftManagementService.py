from abc import ABCMeta, abstractmethod
from typing import List
from amsbank.dto.OverdraftDto import *
from amsbank.models import Overdraft
from amsbank.repositories.OverdraftRepository import OverdraftRepository


class OverdraftManagementService(metaclass=ABCMeta):
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


class DefaultOverdraftManagementServices(OverdraftManagementService):
    repository = OverdraftRepository

    def __init__(self, repository: OverdraftRepository):
        self.repository = repository

    def get_overdraft(self, model: GetOverdraft):
        return self.repository.get_overdraft(model)

    def list_overdraft(self) -> List[ListOverdraft]:
        return self.repository.list_overdraft()

    def overdraft_details(self, overdraft_id: int) -> OverdraftDetails:
        return self.repository.overdraft_details(overdraft_id)

    def get_overdraft_by_account_number(self, account_number: int) -> OverdraftDetails:
        return self.repository.get_overdraft_by_account_number(account_number)

    def get_overdraft_details_by_account_number(self, account_number: int) -> OverdraftDetails:
        return self.repository.get_overdraft_details_by_account_number(account_number)
