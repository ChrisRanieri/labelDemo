"""
Program: labelDemo.py
Page: 263
Author: Chris
Simple python GUI window illustrating the input and output fields
"""
from breezypythongui import EasyFrame

class TextFieldDemo(EasyFrame):
	"""Converts an input string to uppercase and displays the result"""	
	def __init__(self):
		"""Sets up the window and the label"""
		EasyFrame.__init__(self, title = "Text Field Demo")		

		# Label and field for input
		self.addLabel(text = "Input", row = 0, column = 0)
		self.inputField = self.addTextField(text = "", row = 0, column = 1)		

		# Label and field for the output
		self.addLabel(text = "Output", row = 1, column = 0)
		self.outputField = self.addTextField(text = "", row = 1, column = 1, state = "readonly")		

		# the command button
		self.addButton(text = "Convert", row = 2, column = 0, columnspan = 2, command = self.convert)	

		# Event handling method for the button
	def convert(self):
		""" Inputs the string, converts it to uppercase and outputs the result"""
		text = self.inputField.getText()
		result = text.upper()
		self.outputField.setText(result)


	def main():
		"""initiates and pops up the window"""	
		TextFieldDemo().mainloop()

	# Global call to the main() function
	main()