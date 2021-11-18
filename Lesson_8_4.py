from abc import ABC, abstractclassmethod


class OwnError(Exception):

    def __init__(self, txt_error):
        self.text_error = txt_error


class StorageOfOfficeAppliances:

    storage = {}

    @staticmethod
    def to_take(equipment, quantity, place):
        try:
            if type(quantity) == int:
                StorageOfOfficeAppliances.storage.setdefault(place, []).append((equipment, quantity))
            else:
                raise OwnError(f"Количество закупаемого оборудования введите числом!")
        except OwnError as e:
            print(e)
        finally:
            return StorageOfOfficeAppliances.storage


class OfficeAppliances(ABC):

    def __init__(self, cost, day_of_purchase, warranty_period, multiple_users = False):
        self.cost = int(cost)
        self.day_of_purchase = day_of_purchase
        self.warranty_period = warranty_period
        self.multiple_users = multiple_users

    @abstractclassmethod
    def ammortization_per_month(self):
        pass


class Printer(OfficeAppliances):

    def __init__(self, cost, day_of_purchase, warranty_period, multiple_users, capacity, sheet_size):
        OfficeAppliances.__init__(self, cost, day_of_purchase, warranty_period, multiple_users=False)
        self.capacity = int(capacity)
        self.sheet_size = sheet_size

    @property
    def ammortization_per_month(self):
        return round(self.cost/(self.warranty_period * 1.1)/12, 2)


class Scaner(OfficeAppliances):

    def __init__(self, cost, day_of_purchase, warranty_period, multiple_users,
                 capacity, sheet_size, dual_scan = False ):
        OfficeAppliances.__init__(self, cost, day_of_purchase, warranty_period, multiple_users = False)
        self.capacity = int(capacity)
        self.sheet_size = sheet_size
        self.dual_scan = dual_scan

    @property
    def ammortization_per_month(self):
        return round(self.cost / (self.warranty_period * 1.4) / 12, 2)


new_scanner = Scaner(4500,'12-01-2021', 2, False, 40000, 'A3')
new_printer = Printer(9000, '19-10-2021', 3, True, 90000, 'A4')
StorageOfOfficeAppliances.to_take('scanner', 2, 'office')
StorageOfOfficeAppliances.to_take('scanner', 1, 'accountancy')
StorageOfOfficeAppliances.to_take('printer', 1, 'office')
print(StorageOfOfficeAppliances.storage)
