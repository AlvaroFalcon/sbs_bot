from . import waifu_manager

commands = ["!waifu", "!commands"]
custom_commands = []

def manage_command(command, splittedMessage, context, update):
    if command == "!waifu":
        waifu_manager.get_waifu_image(context, update)
    if command == "!commands":
        available_commmands(context, update)
    return

def is_command(text: str):
    command = text.strip().split(" ")[0]
    if not command.startswith("!"):
     return False
    return command in commands

def available_commmands(context, update):
    result = " ".join(line.strip() for line in commands)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str("Comandos disponibles: "+result))