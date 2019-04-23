from unittest.mock import patch
import unittest
import juego_4_numeros as Juego

class OutputCollector(list):
    def __init__(self, *args, **kwargs):
        self.output_collector = []

    def __call__(self, output):
        self.output_collector.append(output)

class ControlInputValues(list):
    def __init__(self, *args, **kwargs):
        self.played = False
        self.prompts = 0
    def __call__(self, console_output):
        if "Cuántos" in console_output:
            # Computer is guessing
            inputs = [
                '4',
                '0'
            ]
        else:
            # Player is guessing
            pass
        
        self.prompts += 1
        return inputs[self.prompts - 1]


class TestGuessOutcomes(unittest.TestCase):
    # Test that each of the match combinations work correctly
    print("Testing Match Function...")
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

    print("Testing Shuffle...")
    # Two digit shuffles
    def test_shuffle_numero_first_second(self):
        result = Juego.shuffle_numero(1234, '0,1')

        self.assertEqual(int(result), 2134)
    
    def test_shuffle_numero_first_third(self):
        result = Juego.shuffle_numero(1234, '0,2')

        self.assertEqual(int(result), 3214)
    
    def test_shuffle_numero_first_last(self):
        result = Juego.shuffle_numero(1234, '0,3')

        self.assertEqual(int(result), 4231)
    
    def test_shuffle_numero_middle_two(self):
        result = Juego.shuffle_numero(1234, '1,2')

        self.assertEqual(int(result), 1324)
    
    def test_shuffle_numero_second_last(self):
        result = Juego.shuffle_numero(1234, '1,3')

        self.assertEqual(int(result), 1432)
    
    def test_shuffle_numero_last_two(self):
        result = Juego.shuffle_numero(1234, '2,3')

        self.assertEqual(int(result), 1243)
    
    # Three digit shuffles
    def test_shuffle_numero_first_three(self):
        result = Juego.shuffle_numero(1234, '0,1,2')

        self.assertEqual(int(result), 3124)

    def test_shuffle_numero_second_three(self):
        result = Juego.shuffle_numero(1234, '1,2,3')

        self.assertEqual(int(result), 1423)
    
    def test_shuffle_numero_first_second_last(self):
        result = Juego.shuffle_numero(1234, '0,1,3')

        self.assertEqual(int(result), 4132)
    
    def test_shuffle_numero_first_third_last(self):
        result = Juego.shuffle_numero(1234, '0,2,3')

        self.assertEqual(int(result), 4213)

    # Four Digit Shuffles
    # TODO
    
    

    def test_generar_numero(self):
        print("Testing Number Generator...")
        dig_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        result = Juego.generar_numero(dig_list)

        # Ensure generated number is in the correct range
        self.assertLessEqual(int(result), 9876)
        self.assertGreaterEqual(int(result), 1234)

        # Ensure generated number has no repeated digits
        self.assertTrue(len(str(result)) == len(set(str(result))))
    
    print("Testing Number Verification...")
    def test_verify_numero_too_small(self):
        result = Juego.verify_numero('0123')
        self.assertEqual(result, False)
    
    def test_verify_numero_not_unique(self):
        result = Juego.verify_numero('9987')
        self.assertEqual(result, False)

class TestGamePlay(unittest.TestCase):
    print("Testing Feedback Functions...")
    def test_give_user_feedback(self):
        result = Juego.give_user_feedback('1234', '4839')
        self.assertEqual(result, [1,1])
    
    def test_get_user_feedback(self):
        with patch('juego_4_numeros.input', side_effect=['2', '1']):
            result = Juego.get_user_feedback('1245')
            self.assertEqual(result, [2,1])

    print("Testing Player Guess...")
    def test_player_guess(self):
        self.output_collector = OutputCollector()
        with \
                patch('juego_4_numeros.input', return_value='1234'), \
                patch('juego_4_numeros.output', side_effect=self.output_collector), \
                patch('juego_4_numeros.generar_numero', return_value='1234'):
            Juego.player_guess()
            self.assertEqual(self.output_collector.output_collector[-1], "You Win!")

    print("Testing Computer Guess...")
    def test_computer_guess(self):
        self.output_collector = OutputCollector()
        with \
                patch('juego_4_numeros.output', side_effect=self.output_collector), \
                patch('juego_4_numeros.generar_numero', return_value='1234'), \
                patch('juego_4_numeros.input', side_effect=ControlInputValues()):
            Juego.computer_guess()
            self.assertEqual(self.output_collector.output_collector[-1], "Thanks for playing!")
            

if __name__ == "__main__":
    unittest.main()
    