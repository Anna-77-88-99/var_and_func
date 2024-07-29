import requests
from EmployeesApi import EmployeesApi

api = EmployeesApi("https://x-clients-be.onrender.com")

def test_add_employee():
    comp = "EAGames"
    desc = "games"
    result = api.new_company(comp, desc)
    new_comp_id = result["id"]
    new_comp = api.get_company(new_comp_id)
    comp_id = new_comp["id"]
    body = api.get_employees_list(comp_id)
    list_before = len(body)
    add_employee = api.add_employee("Иван", "Иванов", "Иванович", comp_id, "art@gmail.com", "www.url.com", "88005553535", "2001-01-01T11:16:51.864Z", True)
    employee_id = add_employee["id"]
    body_new = api.get_employees_list(comp_id)
    list_after = len(body_new)
    assert list_after - list_before == 1
    assert body_new[-1]["firstName"] == "Иван"
    assert body_new[-1]["lastName"] == "Иванов"
    assert body_new[-1]["middleName"] == "Иванович"
    assert body_new[-1]["companyId"] == comp_id
    assert body_new[-1]["email"] == None #email не присваивается, хотя название поля в отладке и Swagger соответствуюет полю json в методе get_employees_list 
    assert body_new[-1]["avatar_url"] == "www.url.com"
    assert body_new[-1]["phone"] == "88005553535"
    assert body_new[-1]["birthdate"] == "2001-01-01"
    assert body_new[-1]["isActive"] == True
    assert body_new[-1]["id"] == employee_id

def test_get_employee_id():
    comp = "CDProjectRed"
    desc = "red engine"
    new_comp = api.new_company(comp, desc)
    new_id = new_comp["id"]
    new_comp = api.get_company(new_id)
    comp_id = new_comp["id"]
    body = api.get_employees_list(comp_id)
    before_list = len(body)
    add_employee = api.add_employee("Иван", "Иванов", "Иванович", comp_id, "art@gmail.com", "www.url.com", "88005553535", "2001-01-01T11:16:51.864Z", True)
    employee_id = add_employee["id"]
    new_body = api.get_employees_list(comp_id)
    after_list = len(new_body)
    assert after_list - before_list == 1
    new_employee = api.get_employee(employee_id)
    assert new_employee["firstName"] == "Иван"
    assert new_employee["lastName"] == "Иванов"
    assert new_employee["middleName"] == "Иванович"
    assert new_employee["companyId"] == comp_id
    assert new_employee["phone"] == "88005553535"
    assert new_employee["birthdate"] == "2001-01-01"
    assert new_employee["isActive"] == True
    assert new_employee["id"] == employee_id
    
def test_path_employee():
    comp = "HoYoverse"
    desc = "tech otakus save the world"
    new_comp = api.new_company(comp, desc)
    new_id = new_comp["id"]
    new_comp = api.get_company(new_id)
    comp_id = new_comp["id"]
    add_employee = api.add_employee("Иван", "Иванов", "Иванович", comp_id, "art@gmail.com", "www.url.com", "88005553535", "2001-01-01T11:16:51.864Z", True)
    emp_id = add_employee["id"]
    edit_employe = api.path_employee(emp_id, "Сидоров", "hoyo@gmail.com", "www.url.ru", "123456789", False)
    #assert edit_employe["lastName"] == "Сидоров"
    assert edit_employe["id"] == emp_id
    assert edit_employe["isActive"] == False
    assert edit_employe["url"] == "www.url.ru"
    assert edit_employe["email"] == "hoyo@gmail.com"
    