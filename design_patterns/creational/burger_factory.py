from enum import Enum
from abc import ABC, abstractmethod


class BurgerType(Enum):
    CHEESEBURGER = 1
    DELUXECHEESEBURGER = 2
    VEGGIEBURGER = 3
    CHICKENBURGER = 4


class Burger(ABC):
    def __init__(self):
        self.burger_name = ""
        self.toppings = []
        self.sauce = ""
        self.price = 0

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass


class CheeseBurger(Burger):
    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class DeluxeCheeseBurger(Burger):
    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class VeggieBurger(Burger):
    def prepare(self):
        pass

    def cook(self):
        pass

    def serve(self):
        pass


class BurgerStoreFactory(ABC):
    @abstractmethod
    def create_burger(self, burger_type: BurgerType) -> Burger:
        pass

    def order_burger(self, burger_type: BurgerType) -> Burger:
        burger = self.create_burger(burger_type)
        burger.prepare()
        burger.cook()
        burger.serve()
        return burger


class CheeseBurgerStore(BurgerStoreFactory):
    def create_burger(self, burger_type: BurgerType) -> Burger:
        if burger_type == BurgerType.CHEESEBURGER:
            return CheeseBurger()
        elif burger_type == BurgerType.DELUXECHEESEBURGER:
            return DeluxeCheeseBurger()
        else:
            raise ValueError("Invalid burger type for CheeseBurgerStore")


class VeggieBurgerStore(BurgerStoreFactory):
    def create_burger(self, burger_type: BurgerType) -> Burger:
        if burger_type == BurgerType.VEGGIEBURGER:
            return VeggieBurger()
        else:
            raise ValueError("Invalid burger type for VeggieBurgerStore")


if __name__ == "__main__":
    cheese_burger_store = CheeseBurgerStore()
    veggie_burger_store = VeggieBurgerStore()

    burger1 = cheese_burger_store.order_burger(BurgerType.CHEESEBURGER)
    burger2 = veggie_burger_store.order_burger(BurgerType.VEGGIEBURGER)
