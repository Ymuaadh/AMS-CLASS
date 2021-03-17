from datetime import date


class GetOverdraft:
    account_id: int
    account_number: int
    account_pin: int
    overdraft_amount: float
    overdraft_balance: float
    overdraft_status: str
    date_updated: date
    date_created: date


class ListOverdraft:
    overdraft_balance: float
    overdraft_amount: float
    date_created: date
    date_updated: date


class OverdraftDetails:
    id: int
    overdraft_balance: float
    overdraft_amount: float
    overdraft_status: str
    account_number: int
    date_created: date
    date_updated: date
