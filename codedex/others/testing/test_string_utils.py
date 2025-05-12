# Assertions

import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized

# (Codedex)
# class TestStringUtils(unittest.TestCase):

#   def test_reverse_string(self):
#     self.assertEqual(reverse_string('mochi'), 'ihcom')
  
#   def test_capitalize_string(self):
#     self.assertEqual(capitalize_string('mochi'), 'Mochi')

#   def test_is_capitalized(self):
#     self.assertTrue(is_capitalized('mochi'))


class TestStringUtils(unittest.TestCase):
   # Test methods
  def Test_reverse_string(self):
    self.assertEqual(reverse_string('pizza'), 'azzip')
    self.assertEqual(reverse_string('donut'), 'tunod')
    self.assertEqual(reverse_string(''), '')

  def Test_capitalize_string(self):
    self.assertEqual(capitalize_string('Bacon', 'Bacon'))
    self.assertEqual(capitalize_string('cake', 'Cake'))
    self.assertEqual(capitalize_string('123abc', '123abc'))

    
  def Test_string_is_capitalized(self):
    self.assertTrue(is_capitalized('Tower'))
    self.assertFalse(is_capitalized('tower'))
    self.assertFalse(is_capitalized(''))


if __name__ == '__main__':
  unittest.main()