import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, BaseHandler, ContextTypes, CommandHandler
from typing import List


logger = logging.getLogger(__name__)


class Scoopbot:
    def __init__(self, creds: str) -> None:
        self._app = ApplicationBuilder().token(creds).build()
        self._app.add_handlers(Scoopbot._build_handlers())


    @staticmethod
    async def _start(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
        logger.info("Running command: start")
        await ctx.bot.send_message(chat_id=update.effective_chat.id, text="hello!")

    @staticmethod
    def _build_handlers() -> List[BaseHandler]:
        return [CommandHandler("start", Scoopbot._start)]

    def run(self) -> None:
        self._app.run_polling()
