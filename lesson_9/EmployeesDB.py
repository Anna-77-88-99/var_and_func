from sqlalchemy import create_engine
from sqlalchemy.sql import text

class EmployeesDB:
    all_scripts = {
        "create company": text("insert into company (\"name\", \"description\") values (:new_name, :new_descr)"),
        "get max id company": text("select MAX(\"id\") from company where deleted_at is null"),
        "delete company by id": text("delete from company where id = :max_id"),
        "select all employees": text("select * from employee where company_id = :company_id"),
        "select employee by id": text("select * from employee where id = :max_emp_id"),
        "create employee": text("insert into employee (first_name, last_name, middle_name, phone, email, birthdate, avatar_url, is_active, company_id) values (:first_name, :last_name, :middle_name, :phone, :email, :birthdate, :avatar_url, :is_active, :company_id)"),
        "get max id employee": text("select MAX(id) from employee"),
        'edit employee': text("update employee set last_name = :new_lastName, email = :new_email, avatar_url = :new_url, phone = :new_phone, is_active = :new_isActive where id = :employeeId"),
        'delete employee by id': text("delete from employee where id = :max_id_employee")
    }
    
    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def create_new_company(self, name, desc):
        self.__db.execute(self.all_scripts['create company'], new_name = name, new_descr = desc)

    def get_max_id_company(self):
        query_db = self.__db.execute(self.all_scripts['get max id company'])
        return query_db.fetchall()[0][0]

    def delete_company(self, max_id_value):
        self.__db.execute(self.all_scripts['delete company by id'], max_id = max_id_value)

    def create_new_employee(self,  first_name, last_name, middle_name, phone, email, birthdate, avatar_url, company_id, is_active):
        self.__db.execute(self.all_scripts['create employee'], first_name = first_name, last_name = last_name, middle_name = middle_name, phone = phone, email = email, birthdate = birthdate, avatar_url = avatar_url, company_id = company_id, is_active = is_active)
    
    def select_all_employees(self, max_id_comp):
        query_db = self.__db.execute(self.all_scripts['select all employees'], company_id = max_id_comp)
        return query_db.fetchall()
    
    def get_max_id_employee(self):
        query_db = self.__db.execute(self.all_scripts['get max id employee'])
        return query_db.fetchall()[0][0]    
    
    def edit_employee(self, employeeId, new_lastName, new_email, new_url, new_phone, new_isActive):
        self.__db.execute(self.all_scripts['edit employee'], employeeId = employeeId, new_lastName = new_lastName, new_email = new_email, new_url = new_url, new_phone = new_phone, new_isActive = new_isActive)

    def delete_employee(self, id):
        self.__db.execute(self.all_scripts['delete employee by id'], max_id_employee = id)