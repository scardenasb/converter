def length(model_instance):
    if model_instance.unit_types_from == "millimeter" and model_instance.unit_types_to == "millimeter":
        to_unit = model_instance.from_unit

    elif model_instance.unit_types_from == "millimeter" and model_instance.unit_types_to == "centimeter":
        to_unit = model_instance.from_unit / 10
    elif model_instance.unit_types_from == "centimeter" and model_instance.unit_types_to == "millimeter":
        to_unit = model_instance.from_unit * 10

    elif model_instance.unit_types_from == "millimeter" and model_instance.unit_types_to == "meter":
        to_unit = model_instance.from_unit / 1000
    elif model_instance.unit_types_from == "meter" and model_instance.unit_types_to == "millimeter":
        to_unit = model_instance.from_unit * 1000

    elif model_instance.unit_types_from == "millimeter" and model_instance.unit_types_to == "kilometer":
        to_unit = model_instance.from_unit / 1000000
    elif model_instance.unit_types_from == "kilometer" and model_instance.unit_types_to == "millimeter":
        to_unit = model_instance.from_unit / 1000000

    elif model_instance.unit_types_from == "centimeter" and model_instance.unit_types_to == "centimeter":
        to_unit = model_instance.from_unit

    elif model_instance.unit_types_from == "centimeter" and model_instance.unit_types_to == "meter":
        to_unit = model_instance.from_unit / 100
    elif model_instance.unit_types_from == "meter" and model_instance.unit_types_to == "centimeter":
        to_unit = model_instance.from_unit * 100

    elif model_instance.unit_types_from == "centimeter" and model_instance.unit_types_to == "kilometer":
        to_unit = model_instance.from_unit / 100000
    elif model_instance.unit_types_from == "kilometer" and model_instance.unit_types_to == "centimeter":
        to_unit = model_instance.from_unit * 100000

    elif model_instance.unit_types_from == "meter" and model_instance.unit_types_to == "meter":
        to_unit = model_instance.from_unit

    elif model_instance.unit_types_from == "meter" and model_instance.unit_types_to == "kilometer":
        to_unit = model_instance.from_unit / 1000
    elif model_instance.unit_types_from == "kilometer" and model_instance.unit_types_to == "meter":
        to_unit = model_instance.from_unit * 1000

    elif model_instance.unit_types_from == "kilometer" and model_instance.unit_types_to == "kilometer":
        to_unit = model_instance.from_unit

    return to_unit


#TODO: fill with correct pressure and system types units after implement ajax stuff
def pressure(model_instance):
    if model_instance.unit_types_from == "psi" and model_instance.unit_types_to == "pascal":
        return model_instance.from_unit * 6894.76
    elif model_instance.unit_types_from == "psi" and model_instance.unit_types_to == "atmosphere":
        return model_instance.from_unit / 6894.76


def parse(model_instance):
    if model_instance.types == "Length":
        to_unit = length(model_instance)
        return to_unit
    elif model_instance.types == "Pressure":
        to_unit = pressure(model_instance)
        return to_unit
