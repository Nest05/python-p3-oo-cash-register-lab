#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.prices = {}
  
  def add_item(self, title, price, quantity = 1):
    item_total = price * quantity
    self.total += item_total
    item = (title,price, quantity)
    self.items.append(item)
    self.prices[title] = price

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount
      print(f"After the discount, the total comes to ${self.total:.0f}.")

  def void_last_transaction(self):
    if len(self.items) > 0:
      last_item = self.items[-1]
      last_item_price = last_item[1]
      last_item_quantity = last_item[2]
      self.total -= last_item_price * last_item_quantity
      self.items.pop()

    if all(quantity == 0 for _, _, quantity in self.items):
      self.total = 0.0