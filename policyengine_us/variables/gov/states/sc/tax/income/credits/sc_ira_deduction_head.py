from policyengine_us.model_api import *


class sc_ira_deduction_head(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina ira deduction of head"
    defined_for = StateCode.SC
    unit = USD
    definition_period = YEAR
