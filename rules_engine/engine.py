import json

class RulesEngine:
    @staticmethod
    def calculate_supplement(data_input):
        try:
            # extract the input data
            print(data_input)
            input_id = data_input["id"]
            children_count = data_input["numberOfChildren"]
            family_composition = data_input["familyComposition"]
            family_unit_in_pay_december = data_input["familyUnitInPayForDecember"]
            # throw error if a key is missing
        except KeyError as e:
            raise ValueError(f"Missing key: {e}")

        # Make sure family compostion value is only either single or couple
        if family_composition not in ["single", "couple"]:
            raise ValueError(f"Invalid familyComposition: {family_composition}. Must be 'single' or 'couple'.")

        # Check if eligible
        is_eligible = family_unit_in_pay_december
        
        if not is_eligible:
            resp_ineligible = {
                "id": input_id,
                "isEligible": False,
                "baseAmount": 0.0,
                "childrenAmount": 0.0,
                "supplementAmount": 0.0,
            }

            return resp_ineligible

        # Calculate amounts
        base_amount = 60.0 if family_composition == "single" else 120.0
        children_amount = 20.0 * children_count
        supplement_amount = base_amount + children_amount

        data_output = {
            "id": input_id,
            "isEligible": True,
            "baseAmount": base_amount,
            "childrenAmount": children_amount,
            "supplementAmount": supplement_amount,
        }
        
        print(data_output)

        return data_output

