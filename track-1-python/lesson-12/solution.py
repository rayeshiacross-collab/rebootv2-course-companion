# Unit tests protect observable search behavior during refactoring.
import unittest
def find_name(query, names):
    key = query.strip().casefold()
    return next((n for n in names if key and n.casefold() == key), None)
class SearchTests(unittest.TestCase):
    def test_exact(self): self.assertEqual(find_name('Nova', ['Nova']), 'Nova')
    def test_normalized(self): self.assertEqual(find_name(' NOVA ', ['Nova']), 'Nova')
    def test_blank(self): self.assertIsNone(find_name(' ', ['Nova']))
    def test_missing(self): self.assertIsNone(find_name('Orion', ['Nova']))
if __name__ == '__main__':
    unittest.main()
