

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from handlers.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>โจ **welcome sir, i am {query.message.from_user.mention}** \n
**[{BOT_NAME}](https://t.me/{BOT_USERNAME}) ๐ฎ๐น๐น๐ผ๐ ๐๐ผ๐ ๐๐ผ ๐ฝ๐น๐ฎ๐ ๐บ๐๐๐ถ๐ฐ ๐ผ๐ป ๐ด๐ฟ๐ผ๐๐ฝ๐ ๐๐ต๐ฟ๐ผ๐๐ด๐ต ๐๐ต๐ฒ ๐ป๐ฒ๐ ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ'๐ ๐๐ผ๐ถ๐ฐ๐ฒ ๐ฐ๐ต๐ฎ๐๐ ๐ฉ๐จ๐ฐ๐๐ซ๐๐ ๐๐ฒ ๐บ๐ผ๐ป๐๐๐ฎ๐ฟ !**

**๐๐ถ๐ป๐ฑ ๐ผ๐๐ ๐ฎ๐น๐น ๐๐ต๐ฒ ๐๐ผ๐'๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฎ๐ป๐ฑ ๐ต๐ผ๐ ๐๐ต๐ฒ๐ ๐๐ผ๐ฟ๐ธ ๐ฏ๐ ๐ฐ๐น๐ถ๐ฐ๐ธ๐ถ๐ป๐ด ๐ผ๐ป ๐๐ต๐ฒ ยป ๐ ๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฏ๐๐๐๐ผ๐ป !**

**๐๐ผ๐ฟ ๐ถ๐ป๐ณ๐ผ๐ฟ๐บ๐ฎ๐๐ถ๐ผ๐ป ๐ฎ๐ฏ๐ผ๐๐ ๐ฎ๐น๐น ๐ณ๐ฒ๐ฎ๐๐๐ฟ๐ฒ ๐ผ๐ณ ๐๐ต๐ถ๐ ๐ฏ๐ผ๐, ๐ท๐๐๐ ๐๐๐ฝ๐ฒ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Add Me to Your Chat", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "Learn Instructions", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "Commands", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "Owner", url=f"https://t.me/Tithonus")
                ],[
                    InlineKeyboardButton(
                        "Support", url=f"https://t.me/StylishUser"
                    ),
                    InlineKeyboardButton(
                        "Updates", url=f"https://t.me/monstar_0")
                ],[
                    InlineKeyboardButton(
                        "Chatting Group", url="https://t.me/EnglishChatting_Club")
                ],[
                    InlineKeyboardButton(
                        "๐ฅ Source Code ๐ซ", url="https://github.com/mohsinhsn/popcorn-music2"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Hello there, welcome to the help menu Powered by @stylishuser !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

__Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Basic Cmdns", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "Advance Cmnds", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Admin Cmnds", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "Sudo Cmnds", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Owner Cmnds", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> here is the basic commands</b>

๐ง [ Xplayer group commands ]

/play (song name) - play song from youtube directly.
/aplay (reply to audio) - play song using audio file
/splay (song name) - play song from youtube by selecting number of results
/playlist - show the list song in queue
/song (song name) - download song from youtube
/search (video name)ย?- search video from youtube detailed
/video (video name)ย?- download video from youtube detailed
/lyric - (song name) lyrics scrapper
/vk (song name) - download song from inline mode

๐ง [ Xplayer channel commands ]

/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel

__Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/cache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status

__Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/unauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group

__Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic

__Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

๐ note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

__Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:

1.) **first, add me to your group**.
2.) **then promote me as admin and give all permissions except anonymous admin**.
3.) **add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her**.
4.) **turn on the voice chat first before start to play music**.

__Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " Commands list", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
@cb_admin_check
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "** here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โธ แดแดแด๊ฑแด", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "โถ๏ธ สแด๊ฑแดแดแด", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฉ ๊ฑแดษชแด", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "โน แดษดแด", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ anti cmnd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ ษขสแด แดแดแดส๊ฑ", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ แดสแด๊ฑแด", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

 **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

โ **usage:**

1๏ธโฃ ban & temporarily ban user from your group:
   ยป type `/b username/reply to message` ban permanently
   ยป type `/tb username/reply to message/duration` temporarily ban user
   ยป type `/ub username/reply to message` to unban user

2๏ธโฃ mute & temporarily mute user in your group:
   ยป type `/m username/reply to message` mute permanently
   ยป type `/tm username/reply to message/duration` temporarily mute user
   ยป type `/um username/reply to message` to unmute user

๐ note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.

__Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " สแดแดแด", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
** Feature:** delete every commands sent by users to avoid spam in groups !

โ usage:**

 1๏ธโฃ to turn on feature:
     ยป type `/delcmd on`
    
 2๏ธโฃ to turn off feature:
     ยป type `/delcmd off`
      
โก __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " สแดแดแด", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

 __Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "สแด๊ฑษชแด แดแดแด๊ฑ", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "แดแดแด?แดแดแดแด แดแดแด๊ฑ", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "แดแดแดษชษด แดแดแด๊ฑ", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๊ฑแดแดแด แดแดแด๊ฑ", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "แดแดกษดแดส แดแดแด๊ฑ", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "สแดแดแด", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""โ HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

__Powered by {BOT_NAME} __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " สแดแดแด", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
