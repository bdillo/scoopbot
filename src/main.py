import logging
from utils import load_creds
from bot import Scoopbot


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    creds = load_creds()
    bot = Scoopbot(creds)

    logger.info("Starting scoopbot...")
    bot.run()


if __name__ == "__main__":
    main()
