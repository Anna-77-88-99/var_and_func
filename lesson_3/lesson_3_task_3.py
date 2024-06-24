from address import Address
from mailing import Mailing

to_address = Address(213188, "Круглое", "Партизанская", 1, 1)
from_address = Address(249038, "Обнинск", "Ленина", 88, 88)

sending = Mailing(to_address, from_address, 1000, 13572468)

print(f"Отправление {sending.tck} из {from_address.ivalue}, {from_address.cvalue}, {from_address.svalue}, {from_address.hvalue} - {from_address.avalue} в {to_address.ivalue}, {to_address.cvalue}, {to_address.svalue}, {to_address.hvalue} -{to_address.avalue}. Стоимость {sending.ct} рублей.")