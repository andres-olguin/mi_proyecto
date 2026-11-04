import unittest
from src.brief2scope import parse_brief

class Brief2ScopeTests(unittest.TestCase):
    def test_requirements_with_accents_and_line_numbers(self):
        text = "Objetivo: Entregar valor\nRequisito: Inicio\nRequisito: Cierre\nRestricción: Plazo sujeto a validación"
        result = parse_brief(text)
        self.assertEqual([r["id"] for r in result["requirements"]], ["REQ-001", "REQ-002"])
        self.assertEqual(result["requirements"][0]["source_line"], 2)
        self.assertEqual(result["constraints"][0]["text"], "Plazo sujeto a validación")

    def test_unlabelled_lines_are_notes(self):
        result = parse_brief("Idea de prueba sin formato")
        self.assertEqual(len(result["notes"]), 1)
        self.assertTrue(result["warnings"])

    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError):
            parse_brief("   ")

    def test_long_input_rejected(self):
        with self.assertRaises(ValueError):
            parse_brief("x" * 100001)

if __name__ == "__main__":
    unittest.main()
