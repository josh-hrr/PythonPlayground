import requests 
import asyncio

base_url = 'https://api.escuelajs.co/api/v1'
endpoint = '/categories'

def get_categories():
    response = requests.get(f'{base_url}{endpoint}')  
    categories = response.json() 
    for category in categories:
        print(category['name']) 
 