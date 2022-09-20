
commands = ["!warn", "!waifu"]
custom_commands = []

def manage_command(command, message, update, context):
    if command in commands:
        return
    if command in custom_commands:
        return
    return

def is_command(text: str):
    command = text.strip().split(" ")[0]
    if not command.startswith("!"):
     return False
    return command in commands