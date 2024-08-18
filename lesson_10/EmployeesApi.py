import allure
import requests

class EmployeesApi:
    def __init__(self, url):
        self.url = url
    
    @allure.step("api.Создать компанию {comp}:{desc}")
    def new_company(self, comp: str, desc: str):
        """
        Создаём компанию с названием comp(str) и описанием desc(str)
        """
        company = {
            "name" : comp,
            "description" : desc
        }
        data_headers = {}
        data_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json = company, headers=data_headers)
        return resp.json()

    @allure.step("API.Получить токен авторизации для авторизации {user}:{password}")
    def get_token(self, user='bloom', password='fire-fairy'):
        """
        Получить токен авторизации
        :params user(str): логин пользователя
        :params password(str): пароль пользователя

        :return: str: token
        """
        creds = {
            "username": user,
            "password": password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    @allure.step("api.Получить компанию по {id}")
    def get_company(self, id):
        """
        С помощью id находит компанию и возвращает данные этой компании
        """
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()
    
    @allure.step("api.Получить сотрудника по {id}")
    def get_employee(self, id):
        """
        С помощью id находит сотрудника и возвращает данные этого сотрудника
        """
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    @allure.step("api.Получить список сотрудников по id компании {comp_id}")
    def get_employees_list(self, comp_id):
        """
        С помощью id компании находит всех сотрудников и возвращает данные этих сотрудников
        """
        data = { "company": comp_id }
        resp = requests.get(self.url + '/employee/', params=data)
        return resp.json()
    
    @allure.step("api.Добавить нового сотрудника {firstName}:{lastName}:{middleName}:{companyId}:{email}:{url}:{phone}:{birthdate}:{isActive}")
    def add_employee(self, firstName: str, lastName: str, middleName: str, companyId: int, email: str, url: str, phone: str, birthdate: str, isActive: bool):
        """
        В этом методе передаём данные сотрудника и создаём его для соответствующей компании по id
        """
        employee_data = {
            "firstName": firstName,
            "lastName": lastName,
            "middleName": middleName,
            "companyId": companyId,
            "email": email,
            "url": url,
            "phone": phone,
            "birthdate": birthdate,
            "isActive": isActive
        }
        data_headers = {}
        data_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json = employee_data, headers = data_headers)
        return resp.json()
    
    @allure.step("api.Редактировать данные сотрудника {id}:{lastName}:{email}:{url}:{phone}:{isActive}")
    def path_employee(self, id: int, lastName: str, email: str, url: str, phone: str, isActive: bool):
        """
        В этом методе передаём новые данные сотрудника и изменяем их для сотрудника с соответствующим id
        """
        edit_data = {
            "lastName": lastName,
            "email": email,
            "url": url,
            "phone": phone,
            "isActive": isActive
        }
        data_headers = {}
        data_headers["x-client-token"] = self.get_token()
        resp = requests.patch(self.url + '/employee/' + str(id), json = edit_data, headers = data_headers)
        return resp.json()