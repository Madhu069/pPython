# Duplicate checker

items =["apple", "Banana", "cherry","apple" ,"date","Mango"]

unique_items = set()

for items in items:
   if items in unique_items:
       print('Duplicate:', items)
       break    
   unique_items.add (items) 