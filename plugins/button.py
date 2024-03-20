# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="â€¢ á´›á´‡É´á´›á´€É´É¢ sá´€Êá´€ â€¢", callback_data="about"),
                InlineKeyboardButton(text="â€¢ á´›á´œá´›á´œá´˜ â€¢", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="É¢Ê€á´á´œá´˜", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="â€¢ á´›á´‡É´á´›á´€É´É¢ sá´€Êá´€ â€¢", callback_data="about"),
                InlineKeyboardButton(text="â€¢ á´›á´œá´›á´œá´˜ â€¢", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="á´„Êœá´€É´É´á´‡ÊŸ", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="â€¢ á´›á´‡É´á´›á´€É´É¢ sá´€Êá´€ â€¢", callback_data="about"),
                InlineKeyboardButton(text="â€¢ á´›á´œá´›á´œá´˜ â€¢", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="â€¢ á´›á´‡É´á´›á´€É´É¢ sá´€Êá´€ â€¢", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="á´„Êœá´€É´É´á´‡ÊŸ", url=client.invitelink),
                InlineKeyboardButton(text="É¢Ê€á´á´œá´˜", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="â€¢ á´›á´œá´›á´œá´˜ â€¢", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="á´Šá´ÉªÉ´ É¢Ê€á´á´œá´˜", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="á´„á´Ê™á´€ ÊŸá´€É¢Éª",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="á´Šá´ÉªÉ´ á´„Êœá´€É´É´á´‡ÊŸ", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="á´„á´Ê™á´€ ÊŸá´€É¢Éª",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="á´Šá´ÉªÉ´ á´„Êœá´€É´É´á´‡ÊŸ", url=client.invitelink),
                InlineKeyboardButton(text="á´Šá´ÉªÉ´ É¢Ê€á´á´œá´˜", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="á´„á´Ê™á´€ ÊŸá´€É¢Éª",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
