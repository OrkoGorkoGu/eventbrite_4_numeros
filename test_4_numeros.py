from unittest.mock import patch
import unittest
import juego_4_numeros as Juego

class TestGuessOutcomes(unittest.TestCase):
    
    def test_0b_0r(self):
        result = Juego.match('1234', '5678')
        self.assertEqual(result, [0, 0])
    
    def test_0b_1r(self):
        result = Juego.match('1234', '8901')
        self.assertEqual(result, [0, 1])
    
    def test_0b_2r(self):
        result = Juego.match('1234', '9012')
        self.assertEqual(result, [0, 2])
    
    def test_0b_3r(self):
        result = Juego.match('1234', '0123')
        self.assertEqual(result, [0, 3])
    
    def test_0b_4r(self):
        result = Juego.match('1234', '4321')
        self.assertEqual(result, [0, 4])
    
    def test_1b_0r(self):
        result = Juego.match('1234', '1567')
        self.assertEqual(result, [1, 0])
    
    def test_1b_1r(self):
        result = Juego.match('1234', '1526')
        self.assertEqual(result, [1, 1])
    
    def test_1b_2r(self):
        result = Juego.match('1234', '1523')
        self.assertEqual(result, [1, 2])
    
    def test_1b_3r(self):
        result = Juego.match('1234', '1423')
        self.assertEqual(result, [1, 3])
    
    def test_2b_0r(self):
        result = Juego.match('1234', '1256')
        self.assertEqual(result, [2, 0])
    
    def test_2b_1r(self):
        result = Juego.match('1234', '1246')
        self.assertEqual(result, [2, 1])
    
    def test_2b_2r(self):
        result = Juego.match('1234', '1243')
        self.assertEqual(result, [2, 2])
    
    def test_3b_0r(self):
        result = Juego.match('1234', '1235')
        self.assertEqual(result, [3, 0])
    
    def test_4b_0r(self):
        result = Juego.match('1234', '1234')
        self.assertEqual(result, [4, 0])

class TestFunctions(unittest.TestCase):
    def test_generar_numero(self):
        dig_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        result = Juego.generar_numero(dig_list)

        # Ensure generated number is in the correct range
        self.assertLessEqual(int(result), 9876)
        self.assertGreaterEqual(int(result), 1234)

        # Ensure generated number has no repeated digits
        self.assertTrue(len(str(result)) == len(set(str(result))))
    
    def test_verify_numero_too_small(self):
        result = Juego.verify_numero('0123')
        self.assertEqual(result, False)
    
    def test_verify_numero_not_unique(self):
        result = Juego.verify_numero('9987')
        self.assertEqual(result, False)

class TestGamePlay(unittest.TestCase):
    def test_give_user_feedback(self):
        result = Juego.give_user_feedback('1234', '4839')
        self.assertEqual(result, [1,1])
    
    def test_get_user_feedback(self):
        with patch('juego_4_numeros.input', side_effect=['2', '1']):
            result = Juego.get_user_feedback('1245')
            self.assertEqual(result, [2,1])

    def test_player_guess(self):
        with patch('juego_4_numeros.input', return_value='1234'):
            pass
    

if __name__ == "__main__":
    unittest.main()
    