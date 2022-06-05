import math as mt


# TODO: Looking how to use exponents as conversion factors (try to find the most accurate Logarithm's with base 10)
def length(model_instance):

    unit_dict = {1: "mm", 2: "cm", 3: "mt", 4: "km"}
    exp_dict= {1: 3, 2: 2, 3: 0, 4: -3}
    exp = exp_dict[model_instance.unit_to_id] - exp_dict[model_instance.unit_id]
    to_unit = round(model_instance.from_unit * 10**exp, 5)

    return f"{to_unit:,} {unit_dict[model_instance.unit_to_id]}'s"


def pressure(model_instance):

    unit_dict = {5: "Pa", 6: "torr", 7: "psi", 8: "bar", 9: "atm"}
    exp_dict = {5: 5, 6: mt.log10(750.062), 7: mt.log10(14.5038), 8: 0, 9: mt.log10(0.986923)}
    exp = exp_dict[model_instance.unit_to_id] - exp_dict[model_instance.unit_id]
    to_unit = round(model_instance.from_unit * 10**exp, 5)

    return f"{to_unit:,} {unit_dict[model_instance.unit_to_id]}'s"


def volume(model_instance):

    unit_dict = {10: "lt", 11: "m^3", 12: "cm^3", 13: "ml", 14: "ft^3", 15: "in^3"}
    exp_dict = {10: 0, 11: mt.log10(0.001), 12: 3, 13: 3, 14: mt.log10(0.0353147), 15: mt.log10(61.0237)}
    exp = exp_dict[model_instance.unit_to_id] - exp_dict[model_instance.unit_id]
    to_unit = round(model_instance.from_unit * 10**exp, 5)

    return f"{to_unit:,} {unit_dict[model_instance.unit_to_id]}'s"
