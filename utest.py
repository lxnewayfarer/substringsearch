import unittest
import main

class ProcTest(unittest.TestCase):
    def test_straight(self):
        self.assertEqual(main.StraightSearch('Hello SibSU', 'Sib'), 6)
        self.assertEqual(main.StraightSearch('Hello SibSU', 'Hell'), 0)
        self.assertEqual(main.StraightSearch('Hello SibSU', 'SFU'), -1)
        self.assertEqual(main.StraightSearch('Hello SibSU', 'fgsgsdgsdgsdgsdg'), -1)

    def test_KMP(self):
        self.assertEqual(main.KMPsearch('SibSU is the Best', 'Best'), 13)
        self.assertEqual(main.KMPsearch('SibSU is the Best', 'Sib'), 0)
        self.assertEqual(main.KMPsearch('SibSU is the Best', 'SFU'), -1)
        self.assertEqual(main.KMPsearch('SibSU is the Best', 'jkljhmvdkfsvmd'), -1)

    def test_RK(self):
        self.assertEqual(main.RKsearch('I love SibSU', 'Sib'), 7)
        self.assertEqual(main.RKsearch('I love SibSU', 'I'), 0)
        self.assertEqual(main.RKsearch('I love SibSU', 'SFU'), -1)
        self.assertEqual(main.RKsearch('I love SibSU', 'xxxxxxxxxxxxxxxx'), -1)


if __name__ == '__main__':
    unittest.main()
