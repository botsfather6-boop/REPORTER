from __future__ import annotations

"""Configuration helpers for the Reaction Reporter Bot.

Fill the values below with your BOT TOKEN, API ID, API HASH, and MONGO URI
before deploying. This avoids mistakes with environment variables.
"""

from typing import Final

# -----------------------------------------------------------
#  🔴 FILL THESE VALUES CAREFULLY BEFORE DEPLOYMENT
# -----------------------------------------------------------

BOT_TOKEN: Final[str] = "8541624692:AAHqY-fw48MThEszRudWJNrkkq5Z7xzIrCw"

API_ID: Final[int] = 34443234        # ← Enter your API ID (integer)
API_HASH: Final[str] = "bfe1f64706e9303b69a21d6f461ea141"

MONGO_URI: Final[str] = "mongodb+srv://annieregain:firstowner8v@anniere.ht2en.mongodb.net/?retryWrites=true&w=majority&appName=AnnieRE"

# -----------------------------------------------------------
#  (Optional) Author Verification — keep or remove as needed
# -----------------------------------------------------------

AUTHOR_NAME: Final[str] = "EUreagulation"
AUTHOR_HASH: Final[str] = "bfe1f64706e9303b69a21d6f461ea141"
