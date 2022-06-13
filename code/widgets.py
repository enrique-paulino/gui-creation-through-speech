import tkinter as tk


def widget_button(window, text):
    newButton = tk.Button(window, text=text, padx=5, pady=5)
    newButton.pack()


def widget_check_button(window, text):
    newCheckButton = tk.Checkbutton(window, text=text, padx=5, pady=5)
    newCheckButton.pack()


def widget_radio_button(window, text):
    newRadioButton = tk.Radiobutton(window, text=text, padx=5, pady=5)
    newRadioButton.pack()


def widget_entry(window, text):
    newEntry = tk.Entry(window, text=text)
    newEntry.pack(padx=5, pady=5)


def widget_label(window, text):
    newLabel = tk.Label(window, text=text, padx=5, pady=5)
    newLabel.pack()
