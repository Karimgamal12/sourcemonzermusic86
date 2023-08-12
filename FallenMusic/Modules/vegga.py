import asyncio

import os
import time
import requests
from config import START_IMG
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from FallenMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين افاتار","المطورين","مطورين"])
  
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/cde2b51203fbdab57fac5.jpg",
        caption=f"""**⩹━★⊷⌯.〝𝘼𝙑⍢⃝𝙎𝙊𝙐𝙍𝘾𝞝〞.⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين افـاتار ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷⌯.〝𝘼𝙑⍢⃝𝙎𝙊𝙐𝙍𝘾𝞝〞.⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "₍ 𝑘 𝑖 𝑛 𝑔 || كـ ٖ ـيـنــج ⁾ ↺", url=f"https://t.me/TR_E2S_ON_MY_MOoN"), 
                 ],[
                    InlineKeyboardButton(
                        "₍ 𝙳𝙴𝚅 || 𝚖𝚘𝚗𝚣𝚎𝚛 ⁾ ↺", url=f"https://t.me/Z_X_Z_B"),
                ],[
                    InlineKeyboardButton(
                        "سورس ⤶ .〝𝘼𝙑⍢⃝𝙎𝙊𝙐𝙍𝘾𝞝〞. ", url=f"https://t.me/sourceav"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["حسن"])
    & filters.group
  
)
async def yas(client, message):
    usr = await client.get_chat("QF_QG")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊⌯⊶★━⩺\n\n🧞‍♂️ ¦𝙺𝙸𝙽𝙶 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐒𝐇𝐀𝐑𝐊⌯⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    
    
   



