import os
from urllib.parse import quote_plus

import mongoengine
from dotenv import load_dotenv

from utils import logger


def connect():
    load_dotenv()

    username = quote_plus(str(os.getenv('MONGODB_USERNAME')))
    password = quote_plus(str(os.getenv('MONGODB_PASSWORD')))

    uri = \
        f"mongodb+srv://{username}:{password}@xandergpt.hf1wkfq.mongodb.net/?retryWrites=true&w=majority"

    try:
        mongoengine.register_connection(alias="default", name="xandergpt")
        mongoengine.connect(host=uri)
    except mongoengine.connection.ConnectionFailure:
        logger.error("MongoDB connection failed")

        return

    logger.info("MongoDB connection successful")
