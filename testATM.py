import unittest
from atm_Modif import Cajero

class TestsATM_Deposito(unittest.TestCase):
    
    def test_deposito_Negativo(self):
        atm = Cajero()
        atm.depositar(-100)
        self.assertTrue(atm.ver()> 0)

    def test_deposito_Cero(self):
        atm = Cajero()
        atm.depositar(0)
        self.assertEqual(5000,atm.ver())
    
    def test_deposito_Float(self):
        atm = Cajero()
        atm.depositar(9.1)
        with self.assertRaises(ValueError):
            print("error in decimals")


class TestATM_Retiro(unittest.TestCase):
    
    def test_retirar_Super(self):
        atm = Cajero()
        atm.retiro(5001)
        self.assertEqual(5000,atm.ver())
    
    def test_retirar_Negativo(self):
        atm = Cajero()
        atm.retiro(-111)
        self.assertEqual(atm.ver(), 5000)

    def test_retirar_Cero(self):
        atm = Cajero()
        atm.retiro(0)
        self.assertEqual(atm.ver(), 5000)
    
    def test_retirar_Vacio(self):
        atm= Cajero()
        atm.retiro(5000)
        atm.retiro(1)
        self.assertNotEqual(-1, atm.ver())
    
    def test_retiro_Float(self):
        atm = Cajero()
        atm.retiro(9.1)
        with self.assertRaises(ValueError):
            print("error in decimals")

class TestsATM_Password(unittest.TestCase):
    def test_pass_incorrec(self):
        atm = Cajero()
        self.assertEquals(1234,atm.passw())
    

if __name__ == '__main__':
    unittest.main()