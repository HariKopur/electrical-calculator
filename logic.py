def calculate_ohms_law(entry_voltage, entry_current, entry_resistance, result_var):
    try:
        voltage = float(entry_voltage.get()) if entry_voltage.get() else None
        current = float(entry_current.get()) if entry_current.get() else None
        resistance = float(entry_resistance.get()) if entry_resistance.get() else None

        if voltage and current:
            resistance = voltage / current
            result_var.set(f"Resistance: {resistance:.2f} Ω")
        elif current and resistance:
            voltage = current * resistance
            result_var.set(f"Voltage: {voltage:.2f} V")
        elif voltage and resistance:
            current = voltage / resistance
            result_var.set(f"Current: {current:.2f} A")
        else:
            result_var.set("Error: Provide at least two values.")
    except ValueError:
        result_var.set("Error: Invalid input!")


def calculate_power(entry_voltage, entry_current, entry_resistance, result_var):
    try:
        voltage = float(entry_voltage.get()) if entry_voltage.get() else None
        current = float(entry_current.get()) if entry_current.get() else None
        resistance = float(entry_resistance.get()) if entry_resistance.get() else None

        if voltage and current:
            power = voltage * current
            result_var.set(f"Power: {power:.2f} W")
        elif current and resistance:
            power = (current ** 2) * resistance
            result_var.set(f"Power: {power:.2f} W")
        elif voltage and resistance:
            power = (voltage ** 2) / resistance
            result_var.set(f"Power: {power:.2f} W")
        else:
            result_var.set("Error: Provide at least two values.")
    except ValueError:
        result_var.set("Error: Invalid input!")


def calculate_energy(entry_power, entry_time, result_var):
    try:
        power = float(entry_power.get())
        time = float(entry_time.get())
        energy = power * time
        result_var.set(f"Energy: {energy:.2f} Wh")
    except ValueError:
        result_var.set("Error: Invalid input!")


def kirchhoff_current_law(entry_input_currents, entry_output_currents, result_var):
    try:
        input_currents = [float(i) for i in entry_input_currents.get().split(",")]
        output_currents = [float(i) for i in entry_output_currents.get().split(",")]

        if sum(input_currents) == sum(output_currents):
            result_var.set("Kirchhoff's Law Verified: ΣI(in) = I(out)")
        else:
            result_var.set("Kirchhoff's Law Not Verified!")
    except ValueError:
        result_var.set("Error: Invalid input!")


def convert_units(entry_value, from_unit, to_unit, result_var):
    try:
        value = float(entry_value.get())
        if from_unit.get() == "mA" and to_unit.get() == "A":
            result_var.set(f"{value} mA = {value / 1000:.4f} A")
        elif from_unit.get() == "A" and to_unit.get() == "mA":
            result_var.set(f"{value} A = {value * 1000:.2f} mA")
        elif from_unit.get() == "mV" and to_unit.get() == "V":
            result_var.set(f"{value} mV = {value / 1000:.4f} V")
        elif from_unit.get() == "V" and to_unit.get() == "mV":
            result_var.set(f"{value} V = {value * 1000:.2f} mV")
        else:
            result_var.set("Invalid Conversion!")
    except ValueError:
        result_var.set("Error: Invalid input!")
