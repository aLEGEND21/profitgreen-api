from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import portfolio_router

app = FastAPI(title="ProfitGreen API", version="0.1.0")

# Set up static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Add routers
app.include_router(portfolio_router, prefix="/portfolio")

# Set up templates so HTML can be rendered
templates = Jinja2Templates(directory="src/templates")


# Declare the features that will be displayed on the homepage
features = [
    {
        "title": "Real-Time Data",
        "description": "View the latest data about the ProfitGreen Discord bot, including portfolios, actions, and bot statistics.",
        "icon": "fa-solid fa-satellite-dish",
        "active": True,
    },
    {
        "title": "Portfolio Statistics",
        "description": "Retrieve valuable portfolio data, such as holdings and trade history, with ease.",
        "icon": "fa-solid fa-chart-line",
        "active": True,
    },
    {
        "title": "Pending Actions",
        "description": "View pending actions, such as limit order and price alerts, without opening the Discord app.",
        "icon": "fa-solid fa-clock",
        "active": True,
    },
    {
        "title": "Bot Statistics",
        "description": "Analyze the bot's performance, including the number of commands executed and the number of guilds.",
        "icon": "fa-solid fa-chart-bar",
        "active": False,
    },
    {
        "title": "Server Configurations",
        "description": "Retrieve guilds' configurations, including existing price streams that have been subscribed to.",
        "icon": "fa-solid fa-cogs",
        "active": False,
    },
]


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    Render the homepage with the features that will be displayed.
    """
    return templates.TemplateResponse(
        request=request, name="index.html", context={"features": features}
    )
