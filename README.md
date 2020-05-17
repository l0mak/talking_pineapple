#  talking_pineapple 

![logo](https://github.com/l0mak/talking_pineapple/blob/master/logo.png)

[Discord](https://discordapp.com/) Bot that can:





Command | Description
------------ | -------------
echo/say | -send the messages from users on his own behalf in both text and voice channels (anonymization of communication)
wt/wf/wq | -output various information from Blizzard API and [WoWhead] (wowhead.com) (web scrapping)
ml | -work with the list of WoW raiders (create, edit and clear by user commands; currently uses txt files will be changed to DB soon™)
userinfo/serverinfo | -submit information about users and server which it works on by gathering info from Discord API


in progress:

- SQLAlchemy ORM + PostgreSQL implementation for stats (commands used or events) and "raiders lists"
- Put whole BOT in Docker Container
- Remake TTS part of Voice module to generate audio file on server side (probably)