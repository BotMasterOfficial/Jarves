from telegram.ext import run_async

from Jarves import dispatcher
from Jarves.modules.disable import DisableAbleCommandHandler
from Jarves.modules.helper_funcs.alternate import send_message
from Jarves.modules.helper_funcs.chat_status import user_admin

@run_async
@user_admin
def send(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message(update.effective_message, creply)


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("reply", send)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["reply"]
__handlers__ = [ADD_CCHAT_HANDLER]
