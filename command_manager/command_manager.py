commands = ["warn"]
custom_commands = []

def manage_command(command, message):
    if command in commands:
        return
    if command in custom_commands:
        return
    return

def is_command(text: str):
    return text.split(" ")[0].startswith("!") in commands