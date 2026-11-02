import shutil

text = "yossy yossy"
width = shutil.get_terminal_size().columns
print(text.rjust(width))
