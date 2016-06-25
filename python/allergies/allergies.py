# Passes the skipped test.


class Allergies:
    ALLERGY_LIST = ['eggs', 'peanuts', 'shellfish', 'strawberries',
                    'tomatoes', 'chocolate', 'pollen', 'cats']

    def __init__(self, allergy_code):
        self.lst = self._create_allergy_list(allergy_code)

    def _create_allergy_list(self, allergy_code):
        allergies_repr = (bin(allergy_code)[::-1])[:-2]
        return [a for a, toggle
                in zip(self.ALLERGY_LIST, allergies_repr)
                if toggle == '1'
                ]

    def is_allergic_to(self, allergen):
        return allergen in self.lst
