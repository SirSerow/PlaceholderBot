
# Telegram Placeholder Bot

## Purpose

This repository contains a minimal **placeholder Telegram bot** that notifies users to switch to a new bot. It does this by replying to any incoming message with a set notification. This is especially useful when you want to deprecate an old bot but still show a friendly message to users.


## How It Works

1. **Reads the Bot Token and new bot name** from a `.env` file (using `python-dotenv`).
2. **Listens for any messages** (including `/start`) using `python-telegram-bot`.
3. **Replies with a placeholder notification** telling users to switch to the new bot.


## Project Layout

- **`bot.py`**  
  The main Python script containing the async handlers for commands and messages.

- **`.env`**  
  Contains the `TELEGRAM_TOKEN` environment variable and `NEW_BOT_NAME` (optional).

- **`requirements.txt`**  
  Python dependencies required to run this bot, such as `python-telegram-bot` and `python-dotenv`.

- **`Dockerfile`**  
  Used to build and run the bot inside a Docker container.


## Getting Started

### 1. Local Setup

1. Clone this repository.
2. Create a `.env` file in the project root containing the bot token:
   
   ```
   TELEGRAM_TOKEN=1234567890:YOUR_BOT_TOKEN_HERE
    NEW_BOT_NAME=YourNewBotName
   ```

3. Install the required dependencies:
   
   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot locally:
   
   ```bash
   python bot.py
   ```
   
   The bot will start polling. Check your Telegram client by sending a message to your bot; it should respond with the placeholder notification.


### 2. Docker Setup

#### 2.1 Build the Image

From the project root, run:

```
docker build -t placeholder-bot .
```

This will create a Docker image named **placeholder-bot** using the instructions in the `Dockerfile`.

#### 2.2 Run the Container

Run docker compose to start the container:

```
docker compose up --build -d
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).
