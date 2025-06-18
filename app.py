from tkinter import messagebox
from mysql.connector import Error
import customtkinter as ctk
from logic import (
    calculate_ohms_law, calculate_power, calculate_energy,
    kirchhoff_current_law, convert_units
)
from database import save_calculation_with_inputs, connect_to_database
import tkinter as tk

class OhmsLawFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.result_var = ctk.StringVar()

        ctk.CTkLabel(self, text="Ohm's Law").pack(pady=10)

        self.entry_voltage = ctk.CTkEntry(self, placeholder_text="Voltage (V)")
        self.entry_voltage.pack(pady=5)

        self.entry_current = ctk.CTkEntry(self, placeholder_text="Current (A)")
        self.entry_current.pack(pady=5)

        self.entry_resistance = ctk.CTkEntry(self, placeholder_text="Resistance (Ω)")
        self.entry_resistance.pack(pady=5)

        ctk.CTkButton(
            self, text="Calculate",
            command=lambda: calculate_ohms_law(
                self.entry_voltage, self.entry_current,
                self.entry_resistance, self.result_var
            )
        ).pack(pady=10)

        ctk.CTkButton(
            self, text="Save Result",
            command=lambda: save_calculation_with_inputs(
                "Ohm's Law",
                {
                    "voltage": self.entry_voltage.get(),
                    "current": self.entry_current.get(),
                    "resistance": self.entry_resistance.get()
                },
                self.result_var.get()
            )
        ).pack(pady=5)

        ctk.CTkLabel(self, textvariable=self.result_var).pack(pady=10)




class PowerFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.result_var = ctk.StringVar()

        ctk.CTkLabel(self, text="Power Calculation").pack(pady=10)

        self.entry_voltage = ctk.CTkEntry(self, placeholder_text="Voltage (V)")
        self.entry_voltage.pack(pady=5)

        self.entry_current = ctk.CTkEntry(self, placeholder_text="Current (A)")
        self.entry_current.pack(pady=5)

        self.entry_resistance = ctk.CTkEntry(self, placeholder_text="Resistance (Ω)")
        self.entry_resistance.pack(pady=5)

        ctk.CTkButton(
            self, text="Calculate Power",
            command=lambda: calculate_power(
                self.entry_voltage, self.entry_current,
                self.entry_resistance, self.result_var
            )
        ).pack(pady=10)

        ctk.CTkButton(
            self, text="Save Result",
            command=lambda: save_calculation_with_inputs(
                "Power Calculation",
                {
                    "voltage": self.entry_voltage.get(),
                    "current": self.entry_current.get(),
                    "resistance": self.entry_resistance.get()
                },
                self.result_var.get()
            )
        ).pack(pady=5)

        ctk.CTkLabel(self, textvariable=self.result_var).pack(pady=10)


class EnergyFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.result_var = ctk.StringVar()

        ctk.CTkLabel(self, text="Energy Calculation").pack(pady=10)

        self.entry_power = ctk.CTkEntry(self, placeholder_text="Power (W)")
        self.entry_power.pack(pady=5)

        self.entry_time = ctk.CTkEntry(self, placeholder_text="Time (h)")
        self.entry_time.pack(pady=5)

        ctk.CTkButton(
            self, text="Calculate Energy",
            command=lambda: calculate_energy(
                self.entry_power, self.entry_time, self.result_var
            )
        ).pack(pady=10)

        ctk.CTkButton(
            self, text="Save Result",
            command=lambda: save_calculation_with_inputs(
                "Energy Calculation",
                {
                    "power": self.entry_power.get(),
                    "time": self.entry_time.get()
                },
                self.result_var.get()
            )
        ).pack(pady=5)

        ctk.CTkLabel(self, textvariable=self.result_var).pack(pady=10)



class KirchhoffFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        self.result_var = ctk.StringVar()

        ctk.CTkLabel(self, text="Kirchhoff's Current Law (KCL)").pack(pady=10)

        self.entry_input_currents = ctk.CTkEntry(
            self, placeholder_text="Input Currents (comma-separated)"
        )
        self.entry_input_currents.pack(pady=5)

        self.entry_output_currents = ctk.CTkEntry(
            self, placeholder_text="Output Currents (comma-separated)"
        )
        self.entry_output_currents.pack(pady=5)

        ctk.CTkButton(
            self, text="Verify KCL",
            command=lambda: kirchhoff_current_law(
                self.entry_input_currents, self.entry_output_currents, self.result_var
            )
        ).pack(pady=10)

        ctk.CTkButton(
            self, text="Save Result",
            command=lambda: save_calculation_with_inputs(
                "Kirchhoff's Current Law",
                {
                    "input_currents": self.entry_input_currents.get(),
                    "output_currents": self.entry_output_currents.get()
                },
                self.result_var.get()
            )
        ).pack(pady=5)

        ctk.CTkLabel(self, textvariable=self.result_var).pack(pady=10)

class ConvertUnitsFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.result_var = ctk.StringVar()

        ctk.CTkLabel(self, text="Unit Conversion").pack(pady=10)

        self.entry_value = ctk.CTkEntry(self, placeholder_text="Value to Convert")
        self.entry_value.pack(pady=5)

        self.unit_from = ctk.StringVar(value="mA")  # Default starting unit
        self.unit_to = ctk.StringVar(value="A")  # Default target unit

        ctk.CTkLabel(self, text="From Unit").pack(pady=5)
        self.unit_from_menu = ctk.CTkOptionMenu(self, variable=self.unit_from, values=["mA", "A", "mV", "V"])
        self.unit_from_menu.pack(pady=5)

        ctk.CTkLabel(self, text="To Unit").pack(pady=5)
        self.unit_to_menu = ctk.CTkOptionMenu(self, variable=self.unit_to, values=["A", "mA", "V", "mV"])
        self.unit_to_menu.pack(pady=5)

        ctk.CTkButton(
            self, text="Convert",
            command=lambda: convert_units(self.entry_value, self.unit_from, self.unit_to, self.result_var)
        ).pack(pady=10)

        ctk.CTkButton(
            self, text="Save Result",
            command=lambda: save_calculation_with_inputs(
                "Unit Conversion",
                {
                    "value": self.entry_value.get(),
                    "from_unit": self.unit_from.get(),
                    "to_unit": self.unit_to.get()
                },
                self.result_var.get()
            )
        ).pack(pady=5)

        ctk.CTkLabel(self, textvariable=self.result_var).pack(pady=10)


class HistoryFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.history_list = ctk.CTkLabel(self, text="History of Calculations", font=("Arial", 16))
        self.history_list.pack(pady=10)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=5)

        self.refresh_button = ctk.CTkButton(self.button_frame, text="Refresh", command=self.load_history)
        self.refresh_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = ctk.CTkButton(self.button_frame, text="Clear History", command=self.clear_history)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.scrollable_frame = ctk.CTkScrollableFrame(self, height=400, width=800)
        self.scrollable_frame.pack(pady=10, fill=tk.BOTH, expand=True)

    def load_history(self):
        connection = connect_to_database()
        if connection is not None:
            try:
                cursor = connection.cursor()
                query = """
                    SELECT h.calculation_type, h.voltage, h.current, h.resistance, h.power,
                           h.time, h.result, h.calculation_date, h.input_currents, h.output_currents, h.value, 
                           h.from_unit, h.to_unit, c.category_name
                    FROM history h
                    LEFT JOIN calculation_category c ON h.category_id = c.category_id
                    ORDER BY h.history_id ASC
                """
                cursor.execute(query)
                records = cursor.fetchall()

                for widget in self.scrollable_frame.winfo_children():
                    widget.destroy()

                for row in records:
                    (calculation_type, voltage, current, resistance, power, time, result,
                     calculation_date, input_currents, output_currents, value, from_unit, to_unit, category_name) = row

                    entry_frame = ctk.CTkFrame(self.scrollable_frame, corner_radius=10, border_width=1,
                                               border_color="gray")
                    entry_frame.pack(fill=tk.X, padx=10, pady=5)

                    ctk.CTkLabel(entry_frame, text=f"Calculation Type: {calculation_type}",
                                 font=("Arial", 14, "bold")).pack(anchor=tk.W, padx=10, pady=5)

                    if calculation_type == "Kirchhoff's Current Law":
                        details = f"Input Currents: {input_currents}\nOutput Currents: {output_currents}"
                    elif calculation_type == "Unit Conversion":
                        details = f"Value: {value} {from_unit} → {to_unit}"
                    elif calculation_type == "Energy Calculation":
                        details = f"Power: {power} W\nTime: {time}"
                    else:
                        details = (f"Voltage: {voltage} V\n"
                                   f"Current: {current} A\n"
                                   f"Resistance: {resistance} Ω")

                    ctk.CTkLabel(entry_frame, text=details, justify="left").pack(anchor=tk.W, padx=10)

                    ctk.CTkLabel(entry_frame, text=f"Result: {result}", text_color="green").pack(anchor=tk.W, padx=10, pady=5)

                    if category_name == "Energy Calculation":
                        ctk.CTkLabel(entry_frame, text=f"Date & Time: {calculation_date}",
                                     text_color="light gray").pack(anchor=tk.W, padx=10, pady=2)
                    else:
                        ctk.CTkLabel(entry_frame, text=f"Date: {calculation_date}",
                                     text_color="light gray").pack(anchor=tk.W, padx=10, pady=2)

                    ctk.CTkLabel(entry_frame, text=f"Category: {category_name or 'Uncategorized'}",
                                 text_color="blue").pack(anchor=tk.W, padx=10, pady=2)

                cursor.close()
                connection.close()

            except Error as e:
                messagebox.showerror("Database Error", f"An error occurred: {e}")

    def clear_history(self):
        confirmation = messagebox.askyesno(
            "Clear History", "Are you sure you want to delete all history from the database?"
        )

        if confirmation:
            connection = connect_to_database()
            if connection is not None:
                try:
                    cursor = connection.cursor()

                    cursor.execute("""
                        DELETE FROM saved_calculation
                        WHERE history_id IN (SELECT history_id FROM history)
                    """)

                    cursor.execute("""
                        DELETE FROM calculation_category
                        WHERE category_id IN (SELECT category_id FROM history)
                    """)

                    cursor.execute("DELETE FROM history")
                    connection.commit()

                    for widget in self.scrollable_frame.winfo_children():
                        widget.destroy()

                    cursor.close()
                    connection.close()

                    messagebox.showinfo("Success", "All history has been deleted.")
                except Error as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")


class MainApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Electrical Calculator")
        self.geometry("800x600")

        tabs = ctk.CTkTabview(self)
        tabs.pack(fill="both", expand=True, padx=10, pady=10)

        ohms_tab = tabs.add("Ohm's Law")
        OhmsLawFrame(ohms_tab).pack(fill="both", expand=True)

        power_tab = tabs.add("Power Calculation")
        PowerFrame(power_tab).pack(fill="both", expand=True)

        energy_tab = tabs.add("Energy Calculation")
        EnergyFrame(energy_tab).pack(fill="both", expand=True)

        kirchhoff_tab = tabs.add("Kirchhoff's Current Law")
        KirchhoffFrame(kirchhoff_tab).pack(fill="both", expand=True)

        convert_tab = tabs.add("Convert Units")
        ConvertUnitsFrame(convert_tab).pack(fill="both", expand=True)

        history_tab = tabs.add("History")
        HistoryFrame(history_tab).pack(fill="both", expand=True)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
app = MainApp()
app.mainloop()