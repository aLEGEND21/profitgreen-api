from motor.motor_asyncio import AsyncIOMotorClient

from config import Config


client = AsyncIOMotorClient(Config.MONGODB_URI)
db = client["ProfitGreen"]
notes_col = db["API-Notes"]
logs_col = db["Logs"]
portfolio_col = db["Portfolio"]
tasks_col = db["Tasks"]


def get_notes():
    return notes_col


def get_logs():
    return logs_col


def get_portfolio():
    return portfolio_col


def get_tasks():
    return tasks_col
