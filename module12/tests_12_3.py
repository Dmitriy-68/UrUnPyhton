import unittest
import runner
import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner1 = runner.Runner('Халк')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner1 = runner.Runner('Халк')
        for i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner1 = runner.Runner('Халк')
        runner2 = runner.Runner('Тор')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усейн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        self.turn1 = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        TournamentTest.all_results[1] = self.turn1.start()
        last_key = max(list(TournamentTest.all_results[1].keys()))
        for k, v in TournamentTest.all_results[1].items():
            TournamentTest.all_results[1][k] = v.name
        self.assertTrue(TournamentTest.all_results[1][last_key] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        self.turn2 = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        TournamentTest.all_results[2] = self.turn2.start()
        last_key = max(list(TournamentTest.all_results[2].keys()))
        for k, v in TournamentTest.all_results[2].items():
            TournamentTest.all_results[2][k] = v.name
        self.assertTrue(TournamentTest.all_results[2][last_key] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
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
