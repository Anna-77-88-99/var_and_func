from smartphone import Smartphone

catalog = []

phone_one = Smartphone("Honor","70","+49415191959")
phone_two = Smartphone("Xiomi","Redmi Note 12 Pro","+49415191971")
phone_three = Smartphone("Apple","15 Pro Max","+49415191975")
phone_four = Smartphone("OnePlus","Nord N30","+49415191979")
phone_five = Smartphone("Samsung ","Galaxy S23 Ultra","+49415191990")

catalog.append(phone_one)
catalog.append(phone_two)
catalog.append(phone_three)
catalog.append(phone_four)
catalog.append(phone_five)

for phone in catalog:
    print(f"Название: {phone.bvalue}, модель: {phone.mvalue}, номер телефона: {phone.nvalue}.")