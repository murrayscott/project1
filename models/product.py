class Product:

    def __init__(self, name, description, part_number, category, stock_qty, reorder_level, unit_multiple, cost, selling_price, deleted, id = None):
      self.name = name
      self.description = description
      self.part_number = part_number
      self.category = category
      self.stock_qty = stock_qty
      self.reorder_level = reorder_level
      self.unit_multiple = unit_multiple
      self.cost = cost
      self.selling_price = selling_price
      self.deleted = deleted
      self.id = id