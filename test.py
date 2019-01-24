from app import app
import unittest

class Test(unittest.TestCase):
  
  def setUp(self):
    self.app = app.test_client()
    
  def test_requisicao(self):
    result = self.app.get('/')