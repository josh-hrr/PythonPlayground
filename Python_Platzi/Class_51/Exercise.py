class Store:
  def checkout(self, *items, **options): 
    print(options)
    total_per_item = []  

    #validate the dict is received + correct datatypes, datakeys
    for item in items:
      if not isinstance(item, dict):
        raise ValueError("Each item must be a dictionary")
      
      required = ["name", "quantity", "price"]
      for key in required:
        if key not in item:
          raise ValueError(f"Missing key: {key}")
      
      if not isinstance(item["name"], str):
        raise ValueError("Name must be a string")
      if not isinstance(item["quantity"], int):
        raise ValueError("Quantity must be an integer")
      if not isinstance(item["price"], (int, float)):
        raise ValueError("Price must be numeric")
      if item["quantity"] < 0 or item["price"] < 0:
        raise ValueError("Quantity and price must be positive")
       
      #evaluating sum of price per item + discount by kwargs
      if "discount" and not "referral" in options:
        total = item["quantity"] * item["price"] 
        total_with_discount = total - options.get("discount")
        total_per_item.append(
          {
            "name": item["name"],
            "total": total_with_discount
          } 
        ) 
      elif "discount" and "referral" in options:
        total = item["quantity"] * item["price"] 
        total_with_discount_referral = total - options.get("discount") - options.get("referral")
        total_per_item.append(
          {
            "name": item["name"],
            "total": total_with_discount_referral
          } 
        )  
      else:
        total = item["quantity"] * item["price"] 
        total_per_item.append(
          {
            "name": item["name"],
            "total": total
          } 
        ) 
    print(total_per_item)   
      
inventory = [
    {
      'name': 'apple', 
      'quantity': 10,
      'price': 2
    }, 
    {
      'name': 'orange', 
      'quantity': 5,
      'price': 2
    },
    {
      'name': 'banana', 
      'quantity': 8,
      'price': 1
    }
  ]  

options =  {
    'discount': 5,
    'referral': 0.5,
    'test': 'testgoeshere'
  } 

#this is how unpacking a list works, it will pass each item in the list as a separate argument
#print("Unpacking a list:", *inventory)

#usage of *args, **kwargs
store1 = Store()
store1.checkout(*inventory, **options)
 
 