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
            inputs = [
                '1235',
                '1234'
            ]
        
        self.prompts += 1
        return inputs[self.prompts - 1]

class TestMatchOutcomes(unittest.TestCase):
    # Test that each of the match combinations work correctly
    def test_match_0b_0r(self):
        result = Juego.match('1234', '5678')
        self.assertEqual(result, [0, 0])
    
    def test_match_0b_1r(self):
        result = Juego.match('1234', '8901')
        self.assertEqual(result, [0, 1])
    
    def test_match_0b_2r(self):
        result = Juego.match('1234', '9012')
        self.assertEqual(result, [0, 2])
    
    def test_match_0b_3r(self):
        result = Juego.match('1234', '0123')
        self.assertEqual(result, [0, 3])
    
    def test_match_0b_4r(self):
        result = Juego.match('1234', '4321')
        self.assertEqual(result, [0, 4])
    
    def test_match_1b_0r(self):
        result = Juego.match('1234', '1567')
        self.assertEqual(result, [1, 0])
    
    def test_match_1b_1r(self):
        result = Juego.match('1234', '1526')
        self.assertEqual(result, [1, 1])
    
    def test_match_1b_2r(self):
        result = Juego.match('1234', '1523')
        self.assertEqual(result, [1, 2])
    
    def test_match_1b_3r(self):
        result = Juego.match('1234', '1423')
        self.assertEqual(result, [1, 3])
    
    def test_match_2b_0r(self):
        result = Juego.match('1234', '1256')
        self.assertEqual(result, [2, 0])
    
    def test_match_2b_1r(self):
        result = Juego.match('1234', '1246')
        self.assertEqual(result, [2, 1])
    
    def test_match_2b_2r(self):
        result = Juego.match('1234', '1243')
        self.assertEqual(result, [2, 2])
    
    def test_match_3b_0r(self):
        result = Juego.match('1234', '1235')
        self.assertEqual(result, [3, 0])
    
    def test_match_4b_0r(self):
        result = Juego.match('1234', '1234')
        self.assertEqual(result, [4, 0])

class TestAlgorithmProgression(unittest.TestCase):
    guessList = [1234, 1234]

    def test_progress_algorithm_0b_0r(self):
        fbList = [[0,0], [0,0]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 5067)
    
    def test_progress_algorithm_0b_1r(self):
        fbList = [[0,1], [0,1]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 2056)
    
    def test_progress_algorithm_0b_2r(self):
        fbList = [[0,2], [0,2]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 2015)
    
    def test_progress_algorithm_0b_3r(self):
        fbList = [[0,3], [0,3]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 2013)
    
    def test_progress_algorithm_0b_4r(self):
        fbList = [[0,4], [0,4]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 2143)
    
    def test_progress_algorithm_1b_0r(self):
        fbList = [[1,0], [1,0]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 1506)
    
    def test_progress_algorithm_1b_1r(self):
        fbList = [[1,1], [1,1]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 1305)
    
    def test_progress_algorithm_1b_2r(self):
        fbList = [[1,2], [1,2]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 1302)
    
    def test_progress_algorithm_1b_3r(self):
        fbList = [[1,3], [1,3]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 1342)
    
    def test_progress_algorithm_2b_0r(self):
        fbList = [[2,0], [2,0]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 1250)
    
    def test_progress_algorithm_2b_1r(self):
        fbList = [[2,1], [2,1]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 1240)
    
    def test_progress_algorithm_2b_2r(self):
        fbList = [[2,2], [2,2]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 1243)
    
    def test_progress_algorithm_3b_0r(self):
        fbList = [[3,0], [3,0]]
        result = Juego.progress_algorithm(self.guessList, fbList)
        self.assertEqual(result, 1235)
    
class TestNumberFunctions(unittest.TestCase):
    def test_generar_numero(self):        
        result = Juego.generar_numero()

        # Ensure generated number has no repeated digits
        self.assertTrue(len(str(result)) == len(set(str(result))) == 4)
        
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
    
    def test_player_guess_win(self):
        self.output_collector = OutputCollector()
        with \
                patch('juego_4_numeros.input', return_value='1234'), \
                patch('juego_4_numeros.output', side_effect=self.output_collector):
            game = Juego.PlayerGuess()
            game.num = 1234
            while game.is_playing:
                game.turn()
            self.assertEqual(self.output_collector.output_collector[-1], "You Win!")
    
    def test_player_guess_not_win(self):
        self.output_collector = OutputCollector()
        with \
                patch('juego_4_numeros.output', side_effect=self.output_collector), \
                patch('juego_4_numeros.input', side_effect=ControlInputValues()):
            game = Juego.PlayerGuess()
            game.num = 1234
            while game.is_playing:
                game.turn()
            self.assertEqual(self.output_collector.output_collector[0], "Bien: 3\nRegular: 0")
    
    def test_computer_guess_win(self):
        self.output_collector = OutputCollector()
        with \
                patch('juego_4_numeros.output', side_effect=self.output_collector), \
                patch('juego_4_numeros.input', side_effect=ControlInputValues()):
            game = Juego.ComputerGuess()
            game.guess = 1234
            while game.is_playing:
                game.turn()
            self.assertEqual(self.output_collector.output_collector[-1], "Thanks for playing!")
            
if __name__ == "__main__":
    unittest.main()