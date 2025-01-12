from motor.motor_asyncio import AsyncIOMotorClient

from config import Config


client = AsyncIOMotorClient(Config.MONGODB_URI)
db = client["ProfitGreen"]
portfolio_col = db["Portfolio"]
tasks_col = db["Tasks"]


def get_portfolio():
    return portfolio_col


def get_tasks():
    return tasks_col
