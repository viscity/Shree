import math
from typing import Union

from AnonXMusic import app
from pyrogram.types import InlineKeyboardButton
from pyrogram.enums import ButtonStyle

from AnonXMusic.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)

    if 0 < umm <= 10:
        bar = "𐙚—————————"
    elif 10 < umm < 20:
        bar = "—𐙚————————"
    elif 20 <= umm < 30:
        bar = "——𐙚———————"
    elif 30 <= umm < 40:
        bar = "———𐙚——————"
    elif 40 <= umm < 50:
        bar = "————𐙚—————"
    elif 50 <= umm < 60:
        bar = "—————𐙚————"
    elif 60 <= umm < 70:
        bar = "——————𐙚———"
    elif 70 <= umm < 80:
        bar = "———————𐙚——"
    elif 80 <= umm < 95:
        bar = "————————𐙚—"
    else:
        bar = "—————————𐙚"
    buttons = [
        
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
                style=ButtonStyle.SUCCESS
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
                style=ButtonStyle.SUCCESS
            ),
            InlineKeyboardButton(
                text="II",
                callback_data=f"ADMIN Pause|{chat_id}",
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text="↻",
                callback_data=f"ADMIN Replay|{chat_id}",
                style=ButtonStyle.DEFAULT
            ),
            InlineKeyboardButton(
                text="‣‣I",
                callback_data=f"ADMIN Skip|{chat_id}",
                style=ButtonStyle.DEFAULT
            ),
            InlineKeyboardButton(
                text="▢",
                callback_data=f"ADMIN Stop|{chat_id}",
                style=ButtonStyle.DANGER
            ),
        ],
    [ InlineKeyboardButton(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true")],
        
    ]

    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
                style=ButtonStyle.SUCCESS
            ),
            InlineKeyboardButton(
                text="II",
                callback_data=f"ADMIN Pause|{chat_id}",
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text="↻",
                callback_data=f"ADMIN Replay|{chat_id}",
                style=ButtonStyle.DEFAULT
            ),
            InlineKeyboardButton(
                text="‣‣I",
                callback_data=f"ADMIN Skip|{chat_id}",
                style=ButtonStyle.DEFAULT
            ),
            InlineKeyboardButton(
                text="▢",
                callback_data=f"ADMIN Stop|{chat_id}",
                style=ButtonStyle.DANGER
            ),
        ],
    [ InlineKeyboardButton(text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true")],
        
    ]

    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
                style=ButtonStyle.SUCCESS
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                style=ButtonStyle.DANGER
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                style=ButtonStyle.PRIMARY
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                style=ButtonStyle.DEFAULT
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
                style=ButtonStyle.DANGER
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                style=ButtonStyle.DEFAULT
            ),
        ],
    ]
    return buttons
