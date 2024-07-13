import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),
                       (quote['stock'],
                              quote['top_bid']['price'],
                              quote['top_ask']['price'],
                              (quote['top_ask']['price']+quote['top_bid']['price'])/2))


  def test_getDataPoint_calculateRatio(self):
    price_a = 1.5
    price_b = 1.2
    ratio = getRatio(price_a, price_b)
    self.assertEqual(1.5/1.2, ratio)

  def test_getDataPoint_calculateRatio_with_second_price_zero(self):
    price_a = 1.5
    price_b = 0
    ratio = getRatio(price_a, price_b)
    self.assertIsNone(ratio)

  def test_getDataPoint_calculateRatio_with_first_price_zero(self):
    price_a = 0
    price_b = 1.2
    ratio = getRatio(price_a, price_b)
    self.assertEqual(0,ratio)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote),
                       (quote['stock'],
                              quote['top_bid']['price'],
                              quote['top_ask']['price'],
                              (quote['top_ask']['price']+quote['top_bid']['price'])/2))



  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
