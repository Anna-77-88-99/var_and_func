import allure
from EmployeesApi import EmployeesApi
from EmployeesDB import EmployeesDB

api = EmployeesApi("https://x-clients-be.onrender.com")
db = EmployeesDB("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

@allure.id("XCLIENTS-1")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Получение списка сотрудников")
@allure.feature("READ")
@allure.title("Получение полного списка сотрудников")
def test_len():
    with allure.step("Создать новую организацию"):
        db.create_new_company("EAGames", "games")
    max_comp_id = db.get_max_id_company()
    with allure.step("Создать нового сотрудника"):
        db.create_new_employee("Иван", "Иванов", "Иванович", "88005553535", "art@gmail.com", "2001-01-01", "www.url.com", max_comp_id, True)
    max_emp_id = db.get_max_id_employee()
    len_api = len(api.get_employees_list(max_comp_id))
    len_db = len(db.select_all_employees(max_comp_id))
    db.delete_employee(max_emp_id)
    db.delete_company(max_comp_id)
    with allure.step("Проверить разницу"):
        with allure.step("Проверить, что список API = списку DB"):
            assert len_api == len_db

@allure.id("XCLIENTS-2")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Добавление нового сотрудника")
@allure.feature("CREATE")
@allure.title("Создание нового сотрудника")
def test_add_employee():
    with allure.step("Cоздать новую организацию"):
        db.create_new_company("EAGames", "games")
    max_comp_id = db.get_max_id_company()
    with allure.step("Создать нового сотрудника"):
        db.create_new_employee("Иван", "Иванов", "Иванович", "88005553535", "art@gmail.com", "2001-01-01", "www.url.com", max_comp_id, True)
    max_emp_id = db.get_max_id_employee()
    employee_data = api.get_employee(max_emp_id)
    db.delete_employee(max_emp_id)
    db.delete_company(max_comp_id)
    with allure.step("Проверить, что поля нового сотрудника корректно заполнены"):
        assert employee_data["firstName"] == "Иван"
        assert employee_data["lastName"] == "Иванов"
        assert employee_data["middleName"] == "Иванович"
        assert employee_data["companyId"] == max_comp_id
        assert employee_data["email"] == "art@gmail.com"
        assert employee_data["avatar_url"] == "www.url.com"
        assert employee_data["phone"] == "88005553535"
        assert employee_data["birthdate"] == "2001-01-01"
        assert employee_data["isActive"] == True
        assert employee_data["id"] == max_emp_id

@allure.id("XCLIENTS-3")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Получение сотрудника по id")
@allure.feature("READ")
@allure.title("Получить сотрудника по id")
def test_get_employee_by_id():
    with allure.step("Cоздать новую организацию"):
        db.create_new_company("CDProjectRed", "red engine")
    max_comp_id = db.get_max_id_company()
    with allure.step("Создать нового сотрудника"):
        db.create_new_employee("Иван", "Иванов", "Иванович", "88005553535", "art@gmail.com", "2001-01-01", "www.url.com", max_comp_id, True)
    max_emp_id = db.get_max_id_employee()
    get_employee = api.get_employee(max_emp_id)
    db.delete_employee(max_emp_id)
    db.delete_company(max_comp_id)
    with allure.step("Проверить, что поля нового сотрудника корректно заполнены"):
        assert get_employee["firstName"] == "Иван"
        assert get_employee["lastName"] == "Иванов"
        assert get_employee["middleName"] == "Иванович"
        assert get_employee["companyId"] == max_comp_id
        assert get_employee["phone"] == "88005553535"
        assert get_employee["birthdate"] == "2001-01-01"
        assert get_employee["isActive"] == True
        assert get_employee["id"] == max_emp_id

@allure.id("XCLIENTS-4")
@allure.epic("Сотрудники")
@allure.severity("blocker")
@allure.story("Изменение нового сотрудника")
@allure.feature("UPDATE")
@allure.title("Редактирование данных сотрудника")
def test_edit_employee():
    with allure.step("Cоздать новую организацию"):
        db.create_new_company("HoYoverse", "tech otakus save the world")
    max_comp_id = db.get_max_id_company()
    with allure.step("Создать нового сотрудника"):
        db.create_new_employee("Иван", "Иванов", "Иванович", "88005553535", "art@gmail.com", "2001-01-01", "www.url.com", max_comp_id, True)
    max_emp_id = db.get_max_id_employee()
    with allure.step("Изменить данные нового сотрудника"):
        db.edit_employee(max_emp_id, "Сидоров", "hoyo@gmail.com", "www.url.ru", "123456789", False)
    edit_employee = api.get_employee(max_emp_id)
    db.delete_employee(max_emp_id)
    db.delete_company(max_comp_id)
    with allure.step("Проверить, что данные нового сотрудника корректно изменены"):
        assert edit_employee["lastName"] == "Сидоров"
        assert edit_employee["email"] == "hoyo@gmail.com"
        assert edit_employee["avatar_url"] == "www.url.ru"
        assert edit_employee["phone"] == "123456789"
        assert edit_employee["isActive"] == False
    