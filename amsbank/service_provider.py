from dependency_injector import containers, providers
from amsbank.repositories.AccountHolderRepository import AccountHolderRepository, DjangoORMAccountHolderRepository
from amsbank.services.AccountHolderManagementService import AccountHolderManagementService, \
    DefaultAccountHolderManagementService
from amsbank.repositories.AccountRepository import AccountRepository, DjangoORMAccountRepository
from amsbank.services.AccountManagementService import AccountManagementService, DefaultAccountManagementService
from amsbank.repositories.LoanRepository import LoanRepository, DjangoORMLoanRepository
from amsbank.services.LoanManagementService import LoanManagementServices, DefaultLoanManagementServices
from amsbank.repositories.OverdraftRepository import OverdraftRepository, DjangoORMOverdraftRepository
from amsbank.services.OverdraftManagementService import OverdraftManagementService, DefaultOverdraftManagementServices
from typing import Callable


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    account_holder_repository: Callable[[], AccountHolderRepository] = providers.Factory(
        DjangoORMAccountHolderRepository
    )

    account_holder_management_service: Callable[[], AccountHolderManagementService] = providers.Factory(
        DefaultAccountHolderManagementService,
        repository=account_holder_repository
    )

    account_repository: Callable[[], AccountRepository] = providers.Factory(
        DjangoORMAccountRepository
    )

    account_management_service: Callable[[], AccountManagementService] = providers.Factory(
        DefaultAccountManagementService, repository=account_repository
    )

    loan_repository: Callable[[], LoanManagementServices] = providers.Factory(
        DjangoORMLoanRepository
    )
    loan_management_service: Callable[[], LoanManagementServices] = providers.Factory(
        DefaultLoanManagementServices, repository=loan_repository
    )
    # overdraft_repository: Callable[[], OverdraftRepository] = providers.Factory(
    #     DjangoORMLoanRepository
    # )
    # overdraft_management_service: Callable[[], OverdraftManagementService] = providers.Factory(
    #     DefaultOverdraftManagementServices, repository=overdraft_repository
    # )


ams_service_provider = Container()
