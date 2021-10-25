import shop
import unittest
import datetime

class all_test(unittest.TestCase):
  def setUp(self):
    self.cart = shop.ShoppingCart()

  def test_add1_surfboards(self):
    message = self.cart.add_surfboards()
    self.assertEqual(message, 'Successfully added 1 surfboard to cart!')
    
  def test_add2_surfboards(self):
    message = self.cart.add_surfboards(2)
    self.assertEqual(message, 'Successfully added 2 surfboards to cart!')

  
  @unittest.skip
  def test_add5_surfboards(self):
    self.assertRaises(shop.TooManyBoardsError, self.cart.add_surfboards(5))

  # @unittest.expectedFailure
  # def test_apply_locals_discount(self):
  #   self.cart.apply_locals_discount()
  #   self.assertTrue(self.cart.locals_discount)
  
  def test_add_surfboards(self):
    for i in range(2, 5):
      with self.subTest(i=i):
        message = self.cart.add_surfboards(i)
        self.assertEqual(message, f'Successfully added {i} surfboards to cart!')
        self.cart = shop.ShoppingCart()
      
  def test_add_invalid_checkout_date(self):
    date = datetime.datetime.now()
    self.assertRaises(shop.CheckoutDateError, self.cart.set_checkout_date, date)

unittest.main()