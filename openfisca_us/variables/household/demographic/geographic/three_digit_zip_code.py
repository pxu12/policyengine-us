from openfisca_us.model_api import *


class three_digit_zip_code(Variable):
    value_type = str
    entity = Household
    label = "Three-digit zipcode"
    definition_period = YEAR

    def formula(household, period, parameters):
        zip_code = household("zip_code", period).astype(int)
        return np.char.zfill((zip_code // 1e2).astype(int).astype(str), 3)
