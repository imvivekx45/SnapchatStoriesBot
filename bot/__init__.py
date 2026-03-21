import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "30277268
"))
    API_HASH = os.environ.get("API_HASH", "aac3007d32018dc2d1c963975896b85b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "AAHBbRWFhPBSJM2ngMcSRiwRNTWydscZ05U")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "vivek_autobot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
