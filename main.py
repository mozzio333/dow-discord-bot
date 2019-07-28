import discord
import os
import re
import math

client = discord.Client()


def isLeapYear(y):
    if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
        return True
    else:
        return False


def isValid(y, m, d):
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        if 1 <= d <= 31:
            return True
        else:
            return False
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if 1 <= d <= 30:
            return True
        else:
            return False
    elif m == 2:
        if isLeapYear(y) == True:
            if 1 <= d <= 29:
                return True
            else:
                return False
        else:
            if 1 <= d <= 28:
                return True
            else:
                return False


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if client.user != message.author:

        if re.match('\d{1,4}年\d{1,2}月\d{1,2}日', message.content):
            y = int(message.content.split('年')[0])
            m = int(message.content.split('年')[1].split('月')[0])
            d = int(message.content.split('月')[1].split('日')[0])

        elif re.match('\d{1,4}/\d{1,2}/\d{1,2}', message.content):
            y = int(message.content.split('/')[0])
            m = int(message.content.split('/')[1])
            d = int(message.content.split('/')[2])

        if isValid(y, m, d) == True:
            if m == 1 or m == 2:
                y = y - 1
                m = m + 12
            C = math.floor(y / 100)
            Y = y % 100
            G = 5 * C + math.floor(C / 4)
            h = (d + math.floor(26 * (m + 1) / 10) +
                 Y + math.floor(Y / 4) + G) % 7
            if h == 0:
                msg = '土曜日'
            elif h == 1:
                msg = '日曜日'
            elif h == 2:
                msg = '月曜日'
            elif h == 3:
                msg = '火曜日'
            elif h == 4:
                msg = '水曜日'
            elif h == 5:
                msg = '木曜日'
            elif h == 6:
                msg = '金曜日'
            else:
                msg = 'error'
        else:
            msg = '年月日が正しくありません'
        await message.channel.send(msg)

client.run(os.environ['DISCORD_SECRET'])
