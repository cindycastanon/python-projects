import unittest
from city11p2 import location
class CitiesTestCase(unittest.TestCase):
  def test_city_country(self):
    tampa_us=location('santiago','chile')
    self.assertEqual(tampa_us, 'Santiago, Chile')
  def test_population(self):
    popul=location('santiago','chile',population='1000')
    self.assertEqual(popul, 'santiago, chile-1000')
if __name__=='__main__':
  unittest.main()