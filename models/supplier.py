class Supplier:

    def __init__(self, product_id, manufacturer_id, deleted, id = None):
      self.product_id = product_id
      self.manufacturer_id = manufacturer_id
      self.deleted = deleted
      self.id = id