import unittest
import function as app
class TestMyApp(unittest.TestCase):
   def setUp(self):
      app.items.clear()
      app.next_id = 1
   def test_add_item(self):
      app.add_item("Телефон", "Іван", 5000)
      self.assertEqual(len(app.items), 1)
      self.assertEqual(app.items[0]["name"], "Телефон")
      self.assertEqual(app.items[0]["owner"], "Іван")
      self.assertEqual(app.items[0]["value"], 5000)

      app.add_item("Телефон", "Іван", 5000)
      self.assertEqual(len(app.items), 1)
   def test_remove_item_by_id(self):
      app.add_item("Телефон", "Іван", 5000)
      app.add_item("Ноутбук", "Оксана", 12000)

      app.remove_item_by_id(1)
      self.assertEqual(len(app.items), 1)
      self.assertEqual(app.items[0]["name"], "Ноутбук")
      
      with self.assertRaisesRegex(ValueError, "не знайдена"):
            app.remove_item_by_id(10)
            
   @unittest.expectedFailure
   def test_remove_exeption(self):
      app.add_item("Телефон", "Іван", 5000)
      app.add_item("Ноутбук", "Оксана", 12000)
      self.assertEqual(app.items[2]["name"], "Ноутбук")
   
   def test_show_items(self):
      
      with self.assertRaisesRegex(ValueError, "порожній"):
            app.show_items()
                  
   def test_search_item(self):
      app.add_item("Телефон", "Іван", 5000)
      app.add_item("Ноутбук", "Оксана", 12000)

      results = [item for item in app.items if "телефон".lower() in item["name"].lower()]
      self.assertEqual(len(results), 1)
      self.assertEqual(results[0]["owner"], "Іван")

      results = [item for item in app.items if str(item["id"]) == "2"]
      self.assertEqual(results[0]["name"], "Ноутбук")
         
      with self.assertRaisesRegex(ValueError, "не знайдена"):
            app.search_item("Планшет")
            
   def test_total_value(self):
      total = app.total_value()
      self.assertEqual(total, 0)
      
      app.add_item("Телефон", "Іван", 5000)
      app.add_item("Ноутбук", "Оксана", 12000)
      total = app.total_value()
      self.assertEqual(total, 17000)
      
if __name__ == "__main__":
   import xmlrunner
   runner = xmlrunner.XMLTestRunner(output="test-reports")
   unittest.main(testRunner=runner)
   unittest.main()