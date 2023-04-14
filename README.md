# Telegram arXivUpdates bot

This Telegram bot sends updates on new articles in selected areas of physics from arxiv.org. 
It allows users to select their preferred branch and area of interest, and receive updates on new research in those fields.

## Usage

Here is an example of use. 

### Start

![](https://github.com/julieprokasheva/telegram-arxivUpdates-bot/blob/master/screenshots/start.jpg)

### Set preferences

The bot, being in the "saving preferences" state, prompts the user to select a branch, and then an area of physics, if any. User can quit state any time using 'cancel'.
- choosing branch
  - ![](https://github.com/julieprokasheva/telegram-arxivUpdates-bot/blob/master/screenshots/set.jpg)

- choosing area
  - ![](https://github.com/julieprokasheva/telegram-arxivUpdates-bot/blob/master/screenshots/areas.jpg)

Once you have selected your preferences, the bot will ask you to check the correctness of the data.

### Send update 

To receive updates on new articles in your selected field, use the 'send update' command.

![](https://github.com/julieprokasheva/telegram-arxivUpdates-bot/blob/master/screenshots/send_updates.jpg)

## Limitations

   1. The bot currently only supports physics-related areas on arxiv.org.
   2. The bot may occasionally experience downtime or delays in updating its database.
