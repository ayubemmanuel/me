# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"{self.brand} {self.model}"


# Derived class (Inheritance)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call the parent constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"📞 Calling {number} from {self.device_info()}...")

    def charge(self):
        print(f"🔋 Charging {self.device_info()}... Battery at {self.battery}%.")


# Create objects with unique values
phone1 = Smartphone("Apple", "iPhone 15", "256GB", 85)
phone2 = Smartphone("Samsung", "Galaxy S24", "512GB", 80)

phone1.make_call("0715849721")
phone2.charge()
