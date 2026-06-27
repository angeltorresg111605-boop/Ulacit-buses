from motor.motor_asyncio import AsyncIOMotorClient
from config import settings

client: AsyncIOMotorClient = None


def get_db():
    return client[settings.MONGO_DB]


async def connect_db():
    global client
    client = AsyncIOMotorClient(settings.MONGO_URI)
    print(f"MongoDB conectado → {settings.MONGO_DB}")


async def close_db():
    global client
    if client:
        client.close()
        print("MongoDB desconectado")
