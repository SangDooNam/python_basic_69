from author import Author, Gender

class Book:
    
    
    def __init__(self, name:str, author:Author, price:float, qty:int):
        self.__name = name
        self.__author = author
        self.__price = price
        self.__qty = qty
    
    
    @property
    def get_name(self) -> str:
        return self.__name
    
    
    @property
    def get_author(self) -> Author:
        return self.__author
    
    @property
    def get_price(self) -> float:
        return self.__price
    
    @get_price.setter
    def set_price(self, price:float) -> None:
        if price <= 0:
            raise ValueError('Price should have Value greater than 0.')
        self.__price = price
        
        
    @property
    def get_qty(self) -> int:
        
        return self.__qty
    
    @get_qty.setter
    def set_qty(self, qty:int) -> None:
        if qty <= 0:
            raise ValueError('Quantity should have Value greater than 0.')
        self.__qty = qty
    
    
    def __str__(self) -> str:
        author_str = str(self.__author)
        return f'Book: [name={self.__name}, Author[{author_str}], price={self.__price}, qty={self.__qty}] '
    
    def get_author_name(self):
        return self.__author.get_name
    
    def get_author_email(self):
        return self.__author.get_email
    

a = Book('Basic Python', Author('James', 'abc@email.com', Gender.MALE.name).get_name, 20.00, 60)



