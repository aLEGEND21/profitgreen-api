# profitgreen-api

## Description

A simple API to retrieve data about the popular Discord bot ProfitGreen. This API was built as part of the RaspAPI program within the HackClub High Seas challenge.

## Features

- **Real-Time Data:** View the latest data about the ProfitGreen Discord bot, including portfolios, actions, and bot statistics.
- **Portfolio Statistics:** Retrieve valuable portfolio data, such as holdings and trade history, with ease.
- **Pending Actions:** View pending actions, such as limit order and price alerts, without opening the Discord app.
- **Bot Statistics (_Soon_):** Analyze the bot's performance, including the number of commands executed and the number of guilds.
- **Server Configurations (_Soon_)**: Retrieve guilds' configurations, including existing price streams that have been subscribed to.
- **API Notes**: View and add notes about the ProfitGreen API HTTP requests. Notes are viewable by all users.

## Implemented Functionality

- **GET Requests:** GET requests are used primarily for retrieving data, including portfolio statistics, pending actions, and API notes.
- **POST Requests:** POST requests have been implemented for all routes involving data being updated, including when creating, updating, and deleting API notes.
- **Documentation:** Navigate to `/scalar` to view the API documentation, which includes information about the available routes and their respective parameters.
