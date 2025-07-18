"""
Author: Alastair Harris
Class: IS 204
Description: This program calculates employee gross pay, including overtime (1.5x regular rate for hours over 40),
and saves the data to a file.  It provides a GUI interface with fields for first name,
last name, hours worked, and hourly wage.
"""

import tkinter as tk
from tkinter import filedialog
import os

class EmployeePayCalculator:
    """
    A class to create the GUI and handle the employee pay calculation and data saving.
    """
    def __init__(self, root):
        """
        Initializes the GUI window and its components.
        """
        self.root = root
        self.root.title("Employee Pay Calculator")
        self.root.geometry("400x350")

        # --- Variables ---
        self.first_name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.hours_worked = tk.StringVar()
        self.hourly_wage = tk.StringVar()
        self.gross_pay = tk.StringVar()
        self.filename = None

        # --- Labels ---
        first_name_label = tk.Label(root, text="First Name:")
        first_name_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        last_name_label = tk.Label(root, text="Last Name:")
        last_name_label.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        hours_worked_label = tk.Label(root, text="Hours Worked:")
        hours_worked_label.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        hourly_wage_label = tk.Label(root, text="Hourly Wage:")
        hourly_wage_label.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        gross_pay_label = tk.Label(root, text="Gross Pay:")
        gross_pay_label.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)
        self.result_label = tk.Label(root, textvariable=self.gross_pay)
        self.result_label.grid(row=4, column=1, sticky=tk.W, padx=10, pady=5)

        # --- Textboxes (Entries) ---
        self.first_name_entry = tk.Entry(root, textvariable=self.first_name)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=5)
        self.last_name_entry = tk.Entry(root, textvariable=self.last_name)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.hours_worked_entry = tk.Entry(root, textvariable=self.hours_worked)
        self.hours_worked_entry.grid(row=2, column=1, padx=10, pady=5)
        self.hourly_wage_entry = tk.Entry(root, textvariable=self.hourly_wage)
        self.hourly_wage_entry.grid(row=3, column=1, padx=10, pady=5)

        # --- Buttons ---
        self.calc_button = tk.Button(root, text="Calculate Pay", command=self.calculate_pay)
        self.calc_button.grid(row=5, column=0, columnspan=2, pady=10)
        self.save_button = tk.Button(root, text="Save Data", command=self.save_data)
        self.save_button.grid(row=6, column=0, columnspan=2, pady=10)
        self.clear_button = tk.Button(root, text="Clear Data", command=self.clear_data)
        self.clear_button.grid(row=7, column=0, columnspan=2, pady=10)
        self.close_button = tk.Button(root, text="Close File", command=self.close_file)
        self.close_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Make the window resizable
        for i in range(2):
            root.columnconfigure(i, weight=1)
        for i in range(9):
            root.rowconfigure(i, weight=1)

    def calculate_pay(self):
        """
        Calculates the gross pay, including overtime, and displays it.
        Handles potential errors in input data.
        """
        try:
            hours = float(self.hours_worked.get())
            wage = float(self.hourly_wage.get())
            if hours < 0 or wage < 0:
                self.gross_pay.set("Error: Invalid input")
                return
            overtime_hours = max(0, hours - 40)
            regular_hours = min(40, hours)
            overtime_rate = wage * 1.5
            gross_pay = (regular_hours * wage) + (overtime_hours * overtime_rate)
            self.gross_pay.set(f"${gross_pay:.2f}")
        except ValueError:
            self.gross_pay.set("Error: Invalid input")

    def save_data(self):
        """
        Saves the employee data and calculated gross pay to a file.
        Prompts the user for a filename if one hasn't been selected.
        Handles file opening errors.
        """
        first = self.first_name.get()
        last = self.last_name.get()
        hours = self.hours_worked.get()
        wage = self.hourly_wage.get()
        pay = self.gross_pay.get()
        if "Error:" in pay:
            tk.messagebox.showerror("Error", "Please calculate pay before saving.")
            return
        if not self.filename:
            self.filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
                title="Save Employee Data"
            )
            if not self.filename:
                return
        try:
            with open(self.filename, "a") as file:
                file.write(f"First Name: {first}, Last Name: {last}, Hours Worked: {hours}, Hourly Wage: {wage}, Gross Pay: {pay}\\n")
            tk.messagebox.showinfo("Success", "Data saved successfully!")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error saving data: {e}")

    def clear_data(self):
        """
        Clears the contents of the textboxes and the result label.
        """
        self.first_name.set("")
        self.last_name.set("")
        self.hours_worked.set("")
        self.hourly_wage.set("")
        self.gross_pay.set("")
        self.first_name_entry.focus_set()

    def close_file(self):
        """
        Closes the file.
        """
        if self.filename:
            self.filename = None
            tk.messagebox.showinfo("File Closed", "File is now closed.")
        else:
            tk.messagebox.showinfo("File Status", "No file is currently open.")

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeePayCalculator(root)
    root.mainloop()
