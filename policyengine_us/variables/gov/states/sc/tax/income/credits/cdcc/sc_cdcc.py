from policyengine_us.model_api import *


class sc_cdcc(Variable):
    value_type = float
    entity = TaxUnit
    label = "South Carolina CDCC"
    documentation = "South Carolina Child and Dependent Care Credit"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://dor.sc.gov/forms-site/Forms/IITPacket_2022.pdf#page=22"
    )
    defined_for = StateCode.SC

    def formula(tax_unit, period, parameters):
        # Get South Carolina CDCC rate.
        p = parameters(period).gov.states.sc.tax.income.credits.cdcc
        p2 = parameters(period).gov.irs.credits.cdcc

        # Get child care expenses.
        childcare_expenses = tax_unit("tax_unit_childcare_expenses", period)

        # Married filing separate are ineligible.
        filing_status = tax_unit("filing_status", period)
        eligible = filing_status != filing_status.possible_values.SEPARATE

        # Number of qualifying people
        count_cdcc_eligible = min_(
            tax_unit("count_cdcc_eligible", period), p2.eligibility.max
        )
        # Maximum value cannot exceed cap
        # Calculate total CDCC
        max_match = childcare_expenses * p.rate
        cap = p2.max *count_cdcc_eligible*p.rate
        return eligible * min_(max_match, cap)
