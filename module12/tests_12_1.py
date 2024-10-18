import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner1 = runner.Runner('Халк')
        for i in range(10):
            runner1.walk()
        self.assertEqual(runner1.distance, 50)

    def test_run(self):
        runner1 = runner.Runner('Халк')
        for i in range(10):
            runner1.run()
        self.assertEqual(runner1.distance, 100)

    def test_challenge(self):
        runner1 = runner.Runner('Халк')
        runner2 = runner.Runner('Тор')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
