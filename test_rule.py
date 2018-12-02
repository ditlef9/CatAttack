from unittest import TestCase

import Rule


class TestRule(TestCase):
    def test_isLegalDogMove(self):
        # Legal step "blue dog move one step forward from default pos"
        self.assertTrue(self, Rule.isLegalDogMove([0, 2], [0, 3]))

        # Legal step "blue dog move one step left from default pos"
        self.assertTrue(self, Rule.isLegalDogMove([0, 2], [1, 2]))

        # Illegal step: "blue dog move two step left from default pos"
        self.assertTrue(self, Rule.isLegalDogMove([0, 2], [2, 2]) == False)

        # Illegal step: "blue dog move two step forward from default pos"
        self.assertTrue(self, Rule.isLegalDogMove([0, 2], [0, 4]) == False)

        # Illegal step: "blue dog move one step diagonally forward left from default pos"
        self.assertTrue(self, Rule.isLegalDogMove([0, 2], [1, 3]) == False)
