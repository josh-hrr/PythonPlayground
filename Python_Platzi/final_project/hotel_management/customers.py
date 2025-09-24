class Customer:
    def __init__(self, consumer_id, name, email):
        self.consumer_id = consumer_id
        self.name = name
        self.email = email

class CustomerManagement: 
    '''
    consumer_list = [
        {
            "id": 1,
            "name": "test1",
            "email": "test@test1.com"
        },
        {
            "id": 2,
            "name": "test2",
            "email": "test@test2.com"
        }
    ]
    '''
    consumer_list = []
    
    def __init__(self): 
        print("CustomerManagement class!")

    def add_customer(self, customer):
        """Agrega un nuevo cliente al sistema."""
        self.consumer_list.append(customer)  

    def get_customer(self, customer_id):
       """Obtiene la información de un cliente por ID."""
       return {
        "id": self.consumer_list[customer_id - 1].consumer_id,
        "name": self.consumer_list[customer_id - 1].name,
        "email": self.consumer_list[customer_id - 1].email
       }
