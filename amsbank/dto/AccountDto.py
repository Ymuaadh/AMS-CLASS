from datetime import date


class RegisterAccount:
    account_holder_id: int
    account_number: str
    account_pin: int
    account_balance: float
    account_status: str


class BlockAndUnblock:
    account_number: str
    account_status: str
    date_updated: date


class DepositAndWithdraw:
    account_number: str
    account_balance: str
    account_pin: int
    amount: float
    date_updated: date


class ListAccount:
    id: int
    account_number: str
    account_status: str
    date_created: date


class AccountDetails:
    id: int
    account_number: str
    account_pin: int
    account_balance: float
    account_status: str
    date_created: date


class Transfer:
    id: int
    account_holder_id: int
    account_status: str
    account_number: int
    account_pin: int
    amount: float
    account_balance: int
    receiver_account_number: int
    receiver_account_balance: int

class Loan:
    id: int
    account_status: str
    account_number: int
    account_pin: int
    amount: float
    loan_type: str
