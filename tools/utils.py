def convert_temp(value, units = "k"):
    match units:
        case "c":
            return round(value - 273.15)
        case "f":
            return round(((value - 273.15) * 1.8) + 32)
        case "k":
            return value
        case _:
            return value


