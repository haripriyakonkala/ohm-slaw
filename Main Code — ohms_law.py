def calculate_current(voltage, resistance):
    if resistance == 0:
        raise ValueError("Resistance cannot be zero")
    return voltage / resistance


def calculate_voltage(current, resistance):
    return current * resistance


def calculate_resistance(voltage, current):
    if current == 0:
        raise ValueError("Current cannot be zero")
    return voltage / current


if __name__ == "__main__":
    V = 12
    R = 6

    I = calculate_current(V, R)

    print("Ohm's Law Calculator")
    print("--------------------")
    print(f"Voltage    : {V} V")
    print(f"Resistance : {R} Ω")
    print(f"Current    : {I} A")