import unittest
import runner_and_tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усейн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    def test_run1(self):
        self.turn1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results[1] = self.turn1.start()
        last_key = max(list(TournamentTest.all_results[1].keys()))
        for k, v in TournamentTest.all_results[1].items():
            TournamentTest.all_results[1][k] = v.name
        self.assertTrue(TournamentTest.all_results[1][last_key] == 'Ник')

    def test_run2(self):
        self.turn2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results[2] = self.turn2.start()
        last_key = max(list(TournamentTest.all_results[2].keys()))
        for k, v in TournamentTest.all_results[2].items():
            TournamentTest.all_results[2][k] = v.name
        self.assertTrue(TournamentTest.all_results[2][last_key] == 'Ник')

    def test_run3(self):
        self.turn3 = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        TournamentTest.all_results[3] = self.turn3.start()
        last_key = max(list(TournamentTest.all_results[3].keys()))
        for k, v in TournamentTest.all_results[3].items():
            TournamentTest.all_results[3][k] = v.name
        self.assertTrue(TournamentTest.all_results[3][last_key] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for k, v in cls.all_results.items():
            print(v)


if __name__ == '__main__':
    unittest.main()
