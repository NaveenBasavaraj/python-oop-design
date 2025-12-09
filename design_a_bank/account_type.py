from __future__ import annotations
from account import Account


class SavingsAccount(Account):
    """
    Savings account with simple rule:
    - No overdraft allowed.
    """

    def can_withdraw(self, amount: float) -> bool:
        return self.balance >= amount  # must have enough balance


class CurrentAccount(Account):
    """
    Current (checking) account that supports overdraft up to a configured limit.
    """

    def __init__(
        self,
        account_number: str,
        owner_id: str,
        opening_balance: float = 0.0,
        overdraft_limit: float = 0.0,
    ) -> None:
        if overdraft_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")

        super().__init__(account_number, owner_id, opening_balance)
        self._overdraft_limit: float = overdraft_limit

    # ---------------------------
    # Properties
    # ---------------------------

    @property
    def overdraft_limit(self) -> float:
        return self._overdraft_limit

    def set_overdraft_limit(self, new_limit: float) -> None:
        if new_limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        self._overdraft_limit = new_limit

    def can_withdraw(self, amount: float) -> bool:
        """
        Allow withdrawal if resulting balance is not below -overdraft_limit.

        Example:
        - balance = 1000
        - overdraft_limit = 500
        - can withdraw up to 1500 (ending at -500)
        """
        projected_balance = self.balance - amount
        return projected_balance >= -self._overdraft_limit

    # ---------------------------
    # Debug / representation
    # ---------------------------

    def __repr__(self) -> str:
        return (
            f"<CurrentAccount {self.account_number} "
            f"balance={self.balance:.2f} "
            f"overdraft_limit={self._overdraft_limit:.2f}>"
        )