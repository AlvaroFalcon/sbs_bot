my_str = """\
First line
Second line
Third line
"""

result = " ".join(line.strip() for line in my_str.splitlines())

print(eval(repr(result)))