from . import waifu_manager

commands = ["!waifu", "!commands","!neko","!shinobu","!megumin","!bully","!cuddle","!cry","!hug","!awoo","!kiss","!lick","!pat","!smug","!bonk","!yeet","!blush","!smile","!wave","!highfive","!handhold","!kick","!kill","!happy","!wink","!dance","!cringe", "!inmersion", "!inmersión"]
custom_commands = []

def manage_command(command, splittedMessage, context, update):
    if command == "!waifu":
        waifu_manager.get_waifu_image(context, update)
    if command == "!neko":
        waifu_manager.get_neko(context, update)
    if command == "!shinobu":
      waifu_manager.get_shinobu(context, update)
    if command == "!megumin":
      waifu_manager.get_megumin(context, update)
    if command == "!bully":
      waifu_manager.get_bully(context, update)
    if command == "!cuddle":
      waifu_manager.get_cuddle(context, update)
    if command == "!cry":
      waifu_manager.get_cry(context, update)
    if command == "!hug":
      waifu_manager.get_hug(context, update)
    if command == "!awoo":
      waifu_manager.get_awoo(context, update)
    if command == "!kiss":
      waifu_manager.get_kiss(context, update)
    if command == "!lick":
      waifu_manager.get_lick(context, update)
    if command == "!pat":
      waifu_manager.get_pat(context, update)
    if command == "!smug":
      waifu_manager.get_smug(context, update)
    if command == "!bonk":
      waifu_manager.get_bonk(context, update)
    if command == "!yeet":
      waifu_manager.get_yeet(context, update)
    if command == "!blush":
      waifu_manager.get_blush(context, update)
    if command == "!smile":
      waifu_manager.get_smile(context, update)
    if command == "!wave":
      waifu_manager.get_wave(context, update)
    if command == "!highfive":
      waifu_manager.get_highfive(context, update)
    if command == "!handhold":
      waifu_manager.get_handhold(context, update)
    if command == "!kick":
      waifu_manager.get_kick(context, update)
    if command == "!kill":
      waifu_manager.get_kill(context, update)
    if command == "!happy":
      waifu_manager.get_happy(context, update)
    if command == "!wink":
      waifu_manager.get_wink(context, update)
    if command == "!dance":
      waifu_manager.get_dance(context, update)
    if command == "!cringe":
      waifu_manager.get_cringe(context, update)      
    if command == "!commands":
        available_commmands(context, update)
    if command == "!inmersion" or command == "!inmersión":
        print(command)
        context.bot.send_photo(update.message.chat_id, photo=open('inmersion.jpg', 'rb'))
    return

def is_command(text: str):
    command = text.strip().split(" ")[0]
    if not command.startswith("!"):
     return False
    return command in commands

def available_commmands(context, update):
    result = "\n".join(line.strip() for line in commands)
    context.bot.send_message(chat_id=update.effective_chat.id, text=str("Comandos disponibles: "+result))