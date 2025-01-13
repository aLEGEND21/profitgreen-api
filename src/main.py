from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from scalar_fastapi import get_scalar_api_reference

from api import actions_router, notes_router, portfolio_router

app = FastAPI(title="ProfitGreen API", version="0.1.0")

# Set up static files
app.mount("/static", StaticFiles(directory="src/static"), name="static")

# Add routers
app.include_router(actions_router, prefix="/actions")
app.include_router(notes_router, prefix="/notes")
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
    {
        "title": "API Notes",
        "description": "View and add notes about the ProfitGreen API HTTP requests. Notes are viewable by all users.",
        "icon": "fa-solid fa-pencil-alt",
        "active": True,
    },
]


@app.get("/", include_in_schema=False, response_class=HTMLResponse)
async def root(request: Request):
    """
    Render the homepage with the features that will be displayed.
    """
    return templates.TemplateResponse(
        request=request, name="index.html", context={"features": features}
    )


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )
