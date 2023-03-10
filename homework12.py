from abc import ABC, abstractmethod


class Gadget(ABC):
    def __init__(self, brand: str, modal: str, ram: int):
        self.brand = brand
        self.modal = modal
        self.ram = ram

    @abstractmethod
    def get_additional_info(self):
        pass


class Mobile(Gadget):
    def __init__(self, brand: str, modal: str, ram: int):
        super().__init__(brand=brand, modal=modal, ram=ram)
        self.price = None

    def get_additional_info(self):
        return f'Brand: {self.brand}, model: {self.modal}, RAM: {self.ram}'

    @property
    def get_mobile_price(self):
        if self.ram > 6:
            self.price = 100
            return self.price
        else:
            self.price = 10
            return self.price


class Laptop(Gadget):
    def __init__(self, brand: str, modal: str, ram: int, transformer_laptop: bool = False):
        super().__init__(brand=brand, modal=modal, ram=ram)
        self.transformer_laptop = transformer_laptop

    def get_additional_info(self):
        return f'Brand: {self.brand}, model: {self.modal}, RAM: {self.ram}'

    def get_transformer_info(self):
        return f'Transformer laptop: {self.transformer_laptop}'
