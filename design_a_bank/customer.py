from __future__ import annotations
from dataclasses import dataclass, field
from typing import List
from account import Account  # assuming your Account base class is in account.py


@dataclass
class Customer:
    customer_id: str
    name: str
    email: str | None = None
    _accounts: List[Account] = field(default_factory=list, repr=False)

    # ------------- Public API -------------

    @property
    def accounts(self) -> List[Account]:
        # return a copy to avoid external mutation
        return list(self._accounts)

    def add_account(self, account: Account) -> None:
        """
        Typically called by Bank when it opens an account.
        """
        self._accounts.append(account)

    def get_total_balance(self) -> float:
        return sum(acc.balance for acc in self._accounts)

    def __repr__(self) -> str:
        return (
            f"<Customer id={self.customer_id} name={self.name!r} "
            f"accounts={len(self._accounts)}>"
        )
