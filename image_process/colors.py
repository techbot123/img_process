import tkinter as tk
from tkinter.colorchooser import askcolor


def get_bg_color():
	return askcolor(title = "Choose Background Color")

def get_text_color():
	return askcolor(title = "Choose text Color")

