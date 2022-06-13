import tkinter as tk


def widget_button(window, text):
    newButton = tk.Button(window, text=text)
    newButton.pack()


def widget_check_button(window, text):
    newCheckButton = tk.Checkbutton(window, text=text)
    newCheckButton.pack()


def widget_radio_button(window, text):
    newRadioButton = tk.Radiobutton(window, text=text)
    newRadioButton.pack()


def widget_entry(window, text):
    newEntry = tk.Entry(window, text=text)
    newEntry.pack()


def widget_label(window, text):
    newLabel = tk.Label(window, text=text)
    newLabel.pack()
