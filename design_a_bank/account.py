from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List


# Defining Transaction Dataclass
@dataclass
class Transaction:
    timestamp: datetime
    amount: float
    transaction_type: str  # deposit or withdrawal
    description: str


# Defining Insufficient Error
class InsufficientFundsError(Exception):
    "raised when a withdrawal is NOT allowed due to low balance"

    pass


class Account(ABC):
    def __init__(
        self, account_nbr: str, owner_id: str, opening_balance: float = 0.0
    ) -> None:
        if opening_balance < 0:
            raise ValueError("opening balance cannot be negative")
        self._account_nbr: str = account_nbr
        self._owner_id: str = owner_id
        self._balance: float = opening_balance
        self._passbook_transactions: str = List[Transaction]

    @property
    def account_nbr(self) -> str:
        return self._account_nbr

    @property
    def balance(self) -> float:
        return self._balance

    @property
    def passbook_transactions(self) -> List[Transaction]:
        return list(self._passbook_transactions)

    ##  Account Actions

    def _add_transaction(self, amount: float, type: str, description: str) -> None:
        tx = Transaction(
            timestamp=datetime.now(),
            amount=amount,
            type=type,
            description=description,
        )
        self._passbook_transactions.append(tx)

    def deposit(self, amount: float, description: str) -> None:
        if amount <= 0:
            raise ValueError("amount must be greater than 0")

        self._balance += amount
        self._add_transaction(
            amount=amount, transaction_type="deposit", description="deposit"
        )

    @abstractmethod
    def can_withdraw(self, amount: float) -> bool:
        raise NotImplementedError

    def withdraw(self, amount: str, description: str = "withdraw"):
        if amount <= 0:
            raise ValueError("Cannot withdraw negative amount")

        if not self.can_withdraw(amount=amount):
            raise InsufficientFundsError(
                f"Cannot withdraw {amount:.2f} from account {self._account_number}."
            )
        self._balance -= amount
        self._add_transaction(amount=amount, type="WITHDRAWAL", description=description)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self._account_number} balance={self._balance:.2f}>"
