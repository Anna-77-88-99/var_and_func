import pytest

from string_utils import StringUtils

string_util = StringUtils()

#Тест-кейс 1 - capitilize делает первую букву заглавной и возвращает этот же текст

@pytest.mark.parametrize('string, result', [
    #Позитивные
    ("собака","Собака"),
    ("skyPro","Skypro"),
    ("sky Pro","Sky pro"),
    ("123","123"),
    ("пёс и кот","Пёс и кот"),
    ("урок-4","Урок-4"),
    #Негативные
    ("",""),
    ("123abc","123abc"),
    (" dog"," dog")
    ])

def test_capitilize(string, result):
    string_util = StringUtils()
    print(f"Строка:{string}")
    print(f"Ожидаемый результат:{result}")
    res = string_util.capitilize(string)
    print(f"Результат:{res}")
    assert res == result

#Тест-кейс 2 - trim удаляет пробелы в начале, если они есть

@pytest.mark.parametrize('string, result', [
    #Позитивные
    (" собака","собака"),
    (" SKYPRO","SKYPRO"),
    (" 123","123"),
    (" урок-4","урок-4"),
    #Негативные
    ("",""),
    ("SKYP RO","SKYP RO"),
    ("собака","собака"),
    ("1 ","1 ")
])

def test_trim(string, result):
    string_util = StringUtils()
    print(f"Строка:{string}")
    print(f"Ожидаемый результат:{result}")
    res = string_util.trim(string)
    print(f"Результат:{res}")
    assert res == result

#Тест-кейс 3 - to_list принимает на вход текст с разделителем и возвращает список строк

@pytest.mark.parametrize('string, div, result', [
    #Позитивные
    ("пёс,кот,свинка", ",", ["пёс", "кот", "свинка"]),
    ("пёс;кот;свинка", ";", ["пёс", "кот", "свинка"]),
    ("@,$,&", None, ["@", "$", "&"]),
    #Негативные
    ("", None, []),
    ("1,2,3,4 5", None, ["1", "2", "3","4 5"])
])

def test_to_list(string, div, result):
    string_util = StringUtils()
    print(f"Строка:{string}")
    print(f"Результат:{result}")
    if div is None:
        res = string_util.to_list(string)
    else:
        res = string_util.to_list(string, div)
    print(f"Результат:{res}")
    assert res == result

#Тест-кейс 4 - contains возвращает `True`, если строка содержит искомый символ и `False` - если нет

@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные
    ("пёс", "п", True),
    ("урок-4", "-", True),
    ("", "", True),
    #Негативные
    ("SkyPro", "s", False),
    ("Привет", "!", False),
    ("Привет", "H", False)
])

def test_contains(string, symbol, result):
    string_util = StringUtils()
    print(f"Строка:{string}")
    print(f"Символ:{symbol}")
    print(f"Ожидаемый результат:{result}")
    res = string_util.contains(string, symbol)
    print(f"Результат:{res}")
    assert res == result

#Тест-кейс 5 - delete_symbol удаляет все подстроки из переданной строки

@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные
    ("торт", "т", "ор"),
    ("123", "1", "23"),
    ("торт", "ор", "тт"),
    #Негативные
    ("", "", ""),
    ("торт", "!", "торт"),
    ("торт  ", "", "торт  ")
])

def test_delete_symbol(string, symbol, result):
    string_util = StringUtils()
    print(f"Строка:{string}")
    print(f"Символ:{symbol}")
    print(f"Ожидаемый результат:{result}")
    res = string_util.delete_symbol(string, symbol)
    print(f"Результат:{res}")
    assert res == result

#Тест-кейс 6 - starts_with возвращает `True`, если строка начинается с заданного символа и `False` - если нет

@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные
    ("торт", "т", True),
    ("123", "1", True),
    (" торт", "", True),
    #Негативные
    ("торт", "Т", False),
    ("торт", "!", False),
    ("", "т", False)
])

def test_starts_with(string, symbol, result):
    string_util = StringUtils()
    print(f"Строка:{string}")
    print(f"Символ:{symbol}")
    print(f"Ожидаемый результат:{result}")
    res = string_util.starts_with(string, symbol)
    print(f"Результат:{res}")
    assert res == result

#Тест-кейс 7 - end_with возвращает `True`, если строка заканчивается на заданный символ и `False` - если нет

@pytest.mark.parametrize('string, symbol, result', [
    #Позитивные
    ("торт", "т", True),
    ("123", "3", True),
    ("торт ", "", True),
    #Негативные
    ("торт", "Т", False),
    ("торт", "!", False),
    ("", "т", False)
])

def test_end_with(string, symbol, result):
    string_util = StringUtils()
    print(f"Строка:{string}")
    print(f"Символ:{symbol}")
    print(f"Ожидаемый результат:{result}")
    res = string_util.end_with(string, symbol)
    print(f"Результат:{res}")
    assert res == result

#Тест-кейс 8 - is_empty возвращает `True`, если строка пустая и `False` - если нет

@pytest.mark.parametrize('string, result', [
    #Позитивные
    ("", True),
    (" ", True),
    ("  ", True),
    #Негативные
    ("торт", False),
    (" торт", False),
    ("123", False)
])

def test_is_empty(string, result):
    string_util = StringUtils()
    print(f"Строка:{string}")
    print(f"Ожидаемый результат:{result}")
    res = string_util.is_empty(string)
    print(f"Результат:{res}")
    assert res == result

    #Тест-кейс 9 - list_to_string преобразует список элементов в строку с указанным разделителем

@pytest.mark.parametrize('lst, join, result', [
    #Позитивные
    (["т","о","р","т"], ",", "т,о,р,т"),
    (["1","2","3"], ";", "1;2;3"),
    (["@","$","&"], None, "@, $, &"),
    #Негативные
    ([], ",", ""),
    ([], None, "")
])

def test_list_to_string(lst, join, result):
    string_util = StringUtils()
    print(f"Коллекция:{lst}")
    print(f"Разделитель:{join}")
    print(f"Ожидаемый результат:{result}")
    if join is None:
        res = string_util.list_to_string(lst)
    else:
        res = string_util.list_to_string(lst, join)
    print(f"Результат:{res}")
    assert res == result