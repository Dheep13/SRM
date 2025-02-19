import pdfkit
input_file = "ML.ipynb"
output_file = "cheatsheet.pdf"
pdfkit.from_file(input_file, output_file)
