import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from analyzer.LeagueAnalyzer import LeagueAnalyzer

if __name__ == '__main__':
    unittest.main()

class TestAnalyzer(unittest.TestCase):

    def test_get_league(self):
        self.assertEqual(LeagueAnalyzer(1360211).years, 5)

if __name__ == '__main__':
    unittest.main()