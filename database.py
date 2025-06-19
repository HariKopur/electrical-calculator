import mysql.connector
from mysql.connector import Error
from tkinter import messagebox


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rootpassword",
            database="electrical_calculator"
        )
        return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Failed to connect to the database: {e}")
        return None


def save_calculation_with_inputs(calculation_type, inputs, result, category_id=None):
    connection = connect_to_database()
    if connection is not None:
        try:
            cursor = connection.cursor()

            voltage = inputs.get("voltage")
            current = inputs.get("current")
            resistance = inputs.get("resistance")
            power = inputs.get("power")
            time = inputs.get("time")
            input_currents = inputs.get("input_currents")
            output_currents = inputs.get("output_currents")
            value = inputs.get("value")
            from_unit = inputs.get("from_unit")
            to_unit = inputs.get("to_unit")

            query_history = """
                INSERT INTO history (
                    calculation_type, voltage, current, resistance, power,
                    time, result, input_currents, output_currents, value,
                    from_unit, to_unit, calculation_date, category_id
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, NOW(), %s)
            """
            cursor.execute(
                query_history,
                (
                    calculation_type, voltage, current, resistance, power,
                    time, result, input_currents, output_currents, value,
                    from_unit, to_unit, category_id
                )
            )

            history_id = cursor.lastrowid
            query_saved = "INSERT INTO saved_calculation (history_id) VALUES (%s)"
            cursor.execute(query_saved, (history_id,))

            connection.commit()
            cursor.close()
            connection.close()

            messagebox.showinfo("Success", "Calculation and inputs saved to the database!")
        except Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
