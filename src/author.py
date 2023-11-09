from enum import Enum

class Gender(Enum):
    
    MALE = 1
    FEMALE = 2
    NONE_BINARY = 3


class Author():
    
    def __init__(self, name:str, email:str, gender:Gender) -> None:
        self.__name = name
        self.__email = email
        self.__gender = gender
    
    @property
    def get_name(self):
        return self.__name
    
    @get_name.setter
    def get_name(self, name):
        if len(name) == 0:
            raise TypeError('Name should contain letter.')
        self.__name = name
    
    @property
    def get_email(self):
        return self.__email
    
    @get_email.setter
    def set_email(self, email):
        if len(email) == 0:
            raise TypeError('E-smail should contain letter.')
        self.__email = email
        
        
    @property
    def get_gender(self):
        return self.__gender

    def __str__(self):
        return f'Author: [name={self.__name}, email={self.__email}, gender={self.__gender}]'


a = Author('James', 'abc@email.com', Gender.MALE.name)

