from policyengine_us.model_api import *


class mt_withheld_income_tax(Variable):
    value_type = float
    entity = Person
    label = "Montana withheld income tax"
    defined_for = StateCode.MT
    unit = USD
    definition_period = YEAR

    def formula(person, period, parameters):
        employment_income = person("irs_employment_income", period)
        p = parameters(period).gov.states.mt.tax.income
        # We apply the maximum standard deduction amount
        standard_deduction = p.deductions.standard.cap["SINGLE"]
        reduced_employment_income = max_(
            employment_income - standard_deduction, 0
        )
        return p.main.single.calc(reduced_employment_income)
