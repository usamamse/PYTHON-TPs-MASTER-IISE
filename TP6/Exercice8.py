import unittest
import logging

def safe_division(a, b):
    try:
        if b != 0:
            resultat = a / b
            
            logging.basicConfig(level=logging.INFO)  
            logging.info("La division a été effectuée avec succes")
            return resultat
        else:
            raise ZeroDivisionError("Erreur arithmétique : échec d'opération (b est nul)")
    except ZeroDivisionError as e:
        logging.error(e)
        raise 
    finally:
        logging.info("La fonction est terminée")


class TestSafetyDivision(unittest.TestCase):
    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            safe_division(5,0)
    
    def test_valid_division(self):
        with self.assertLogs(level='INFO') as log:
            safe_division(4,2)
            self.assertIn("La division a été effectuée avec succes", log.output[0])

if __name__ == "__main__":
    unittest.main()