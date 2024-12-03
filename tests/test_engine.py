import pytest
from rules_engine.engine import RulesEngine

def test_eligibility_single_no_children():
    data = {
        "id": "1",
        "numberOfChildren": 0,
        "familyComposition": "single",
        "familyUnitInPayForDecember": True,
    }
    result = RulesEngine.calculate_supplement(data)
    assert result["isEligible"] is True
    assert result["baseAmount"] == 60.0
    assert result["childrenAmount"] == 0.0
    assert result["supplementAmount"] == 60.0

def test_ineligible_family_unit():
    data = {
        "id": "2",
        "numberOfChildren": 2,
        "familyComposition": "couple",
        "familyUnitInPayForDecember": False,
    }
    result = RulesEngine.calculate_supplement(data)
    assert result["isEligible"] is False
    assert result["baseAmount"] == 0.0
    assert result["childrenAmount"] == 0.0
    assert result["supplementAmount"] == 0.0

def test_couple_no_children():
    data = {
        "id": "3",
        "numberOfChildren": 0,
        "familyComposition": "couple",
        "familyUnitInPayForDecember": True,
    }
    result = RulesEngine.calculate_supplement(data)
    assert result["isEligible"] is True
    assert result["baseAmount"] == 120.0
    assert result["childrenAmount"] == 0.0
    assert result["supplementAmount"] == 120.0

def test_single_parent_with_children():
    data = {
        "id": "4",
        "numberOfChildren": 3,
        "familyComposition": "single",
        "familyUnitInPayForDecember": True,
    }
    result = RulesEngine.calculate_supplement(data)
    assert result["isEligible"] is True
    assert result["baseAmount"] == 60.0
    assert result["childrenAmount"] == 60.0  # 3 * 20
    assert result["supplementAmount"] == 120.0