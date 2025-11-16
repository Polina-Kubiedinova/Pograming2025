import function as func
func.add_item("Телефон", "Іван", 5000)
func.add_item("Ноутбук", "Оксана", 12000)
func.add_item("Телефон", "Петро", 7000)

func.show_items()

func.search_item("телефон")
func.remove_item_by_id(2) 
func.show_items()

func.total_value()
