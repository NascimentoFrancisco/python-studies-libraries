from unittest import TestCase
from function_emojis import filter_emojis_in_phrase

class TestEmojis(TestCase):
    
    def setUp(self):
        self.phrase = 'Parabéns a todos 👏👏👏🎉🎉'
    
    def test_phrase_correct(self):
        expected_phrase = 'Parabéns a todos mãos aplaudindo mãos aplaudindo mãos aplaudindo cone de festa cone de festa '
        self.assertEqual(filter_emojis_in_phrase(self.phrase),expected_phrase)