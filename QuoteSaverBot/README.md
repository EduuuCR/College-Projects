# Quote Saver Discord Bot

The **Quote Saver** Discord bot allows users to save, retrieve, list, and delete quotes in their Discord servers. It’s designed to provide an easy way to manage and interact with memorable quotes.

---

## Features

- **Add Quotes**: Save memorable quotes with the `!addquote` command.
- **Random Quotes**: Retrieve a random quote with the `!randomquote` command.
- **List Quotes**: Display all saved quotes with the `!listquotes` command.
- **Delete Quotes**: Remove a specific quote by its index using the `!deletequote` command.

---

## Commands

| Command          | Description                                | Example                          |
|-------------------|--------------------------------------------|----------------------------------|
| `!addquote`      | Save a new quote in the server.            | `!addquote This is a new quote!` |
| `!randomquote`   | Retrieve a random saved quote.             | `!randomquote`                   |
| `!listquotes`    | List all saved quotes in the server.       | `!listquotes`                    |
| `!deletequote`   | Delete a quote by its index.               | `!deletequote 1`                 |

---

## Setup Instructions

### Prerequisites

- Python 3.8 or higher installed.
- A Discord bot token. (Follow [this guide](https://discordpy.readthedocs.io/en/stable/discord.html) to create a bot.)

### Installation

1. Clone the repository or download the source code:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
