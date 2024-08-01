import requests

class EmployeesApi:
    def __init__(self, url):
        self.url = url
    
    def new_company(self, comp, desc):
        company = {
            "name" : comp,
            "description" : desc
        }
        data_headers = {}
        data_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json = company, headers=data_headers)
        return resp.json()

    def get_token(self, user='bloom', password='fire-fairy'):
        creds = {
            "username": user,
            "password": password
        } 
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()
    
    def get_employee(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()

    def get_employees_list(self, comp_id):
        data = { "company": comp_id }
        resp = requests.get(self.url + '/employee/', params=data)
        return resp.json()
    
    def add_employee(self, firstName, lastName, middleName, companyId, email, url, phone, birthdate, isActive):
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
    
    def path_employee(self, id, lastName, email, url, phone, isActive):
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