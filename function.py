items = []
next_id = 1 

def add_item(name, owner, value):
   global next_id
   for item in items:
      if item["name"] == name and item["owner"] == owner and item["value"] == value:
            print("Така річ вже існує")
            return
   item = {"id": next_id, "name": name, "owner": owner, "value": value}
   items.append(item)
   next_id += 1
   print(f" Додано: {item}")

def remove_item_by_id(item_id):
   for item in items:
      if item["id"] == item_id:
            items.remove(item)
            print(f" Видалено: {item}")
            return
   raise ValueError(f"Річ з ID {item_id} не знайдена")

def show_items():
   if not items:
      raise ValueError("Список речей порожній")
   else:
      print("\n Список речей:")
      for item in items:
            print(f"ID: {item['id']}, Назва: {item['name']}, Власник: {item['owner']}, Вартість: {item['value']} грн")

def search_item(keyword):
   results = [item for item in items
               if keyword.lower() in item["name"].lower() or str(item["id"]) == str(keyword)]
   if results:
      print("\n Знайдено:")
      for item in results:
            print(f"ID: {item['id']}, {item['name']} ({item['value']} грн)")
   else:
      raise ValueError(f"Річ з ключовим словом '{keyword}' не знайдена")

def total_value():
   if not items:
      print(" Список порожній, загальна вартість = 0")
      return 0
   total = sum(item["value"] for item in items)
   print(f" Загальна оціночна вартість: {total} грн")
   return total