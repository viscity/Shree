from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.enums import ButtonStyle


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER
            ),
        ]
    ]

    dur_btn = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
                style=ButtonStyle.SUCCESS
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
                style=ButtonStyle.PRIMARY
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                style=ButtonStyle.DANGER
            ),
        ],
    ]

    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur_btn)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                    style=ButtonStyle.DEFAULT
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                    style=ButtonStyle.DANGER
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
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
    ]

    return buttons
