"""
    Bundeshaushalt API

    Mit unserem Tool „Bundeshaushalt digital“ können Sie sich eine visualisierte Darstellung der Haushaltsdaten der letzten Jahre anzeigen lassen. Sie können sowohl Ausgaben und Einnahmen als auch Soll- und Ist-Werte abrufen und mithilfe des Jahresvergleichs gegenüberstellen. Zudem steht Ihnen eine Vielzahl weiterer Filteroptionen zur Verfügung.<br>  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: anetz@gmx.net
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

from deutschland.bundeshaushalt.model.labeled_element import LabeledElement

from deutschland import bundeshaushalt

globals()["LabeledElement"] = LabeledElement
from deutschland.bundeshaushalt.model.budget_data_response_related import (
    BudgetDataResponseRelated,
)


class TestBudgetDataResponseRelated(unittest.TestCase):
    """BudgetDataResponseRelated unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBudgetDataResponseRelated(self):
        """Test BudgetDataResponseRelated"""
        # FIXME: construct object with mandatory attributes with example values
        # model = BudgetDataResponseRelated()  # noqa: E501
        pass


if __name__ == "__main__":
    unittest.main()
