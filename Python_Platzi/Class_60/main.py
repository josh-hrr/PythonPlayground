#importing the functions from the modules within the ecommerce package

from packages.ecommerce.inventory.inventory import add_product, remove_product
from packages.ecommerce.sales.sales import process_sale

add_product('Laptop', 50)
remove_product('Laptop')
process_sale('Laptop', 2)