from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
    
    @classmethod
    def save(cls, data):
        query='INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)'
        return connectToMySQL("users").query_db(query, data)

    @classmethod
    def get_by_email(cls, data):
        query='SELECT * FROM users where email = %(email)s'
        data=connectToMySQL("users").query_db(query, data)
        if data:
            return cls(data[0])
        return False

    @staticmethod
    def register_validator(data):
        is_valid= True
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters")
            is_valid=False
        if len(data['last_name']) < 2:
            flash("First name must be at least 2 characters")
            is_valid=False
        if len(data['password']) < 8:
            flash("First name must be at least 8 characters")
            is_valid=False
        if data['password'] == data['confirm_pw']:
            flash("Passwords must match")
            is_valid=False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if not User.get_by_email(data):
            flash("Email address already in use")
            is_valid = False

        return is_valid
    
        
        