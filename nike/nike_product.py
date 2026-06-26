from bs4 import BeautifulSoup
from colors import *
import os
import json
from discord_webhook import DiscordEmbed
import discord 

def get_product(html : str):
    soup = BeautifulSoup(html, "html.parser")
    image = soup.find('img', attrs={"data-testid" : "Thumbnail-Img-0"})
    imgLink = image['src']
    title = soup.find('h1', id="pdp_product_title")
    price = soup.find('div', id="price-container")
    print(f"Shoe Name : {title.text}\nPrice : {price.text}\n")
    titleEmbed = f"Shoe Name : {title.text}\nPrice : {price.text}\n" 
    message = "\nSizes :\n"
    stockInfos = parseDataStock()
    if stockInfos:
        # y = 0
        # idx = 0
        # for i in stockInfos:
        #     unvailable = i.find('input', attrs={"aria-disabled": "true"})
        #     if unvailable:
        #         print(f"{RED}[{i.text.strip()}] {stockInfos[idx]} {RESET} ", end=" ")
        #         message += f"🔴 {i.text.strip()} [{stockInfos[idx]}]\n"
        #     else:
        #         print(f"{GREEN}[{i.text.strip()}] {stockInfos[idx]} {RESET}", end=" ")
        #         message += f"🟢 {i.text.strip()} [{stockInfos[idx]}]\n"
        #     y += 1
        #     idx += 1
        #     if y == 3:
        #         print()
        #         y = 0
        for taille, stock in stockInfos.items():
            if stock == "OOS":
                print(f"{RED}[{taille}] {stock} {RESET} ", end=" ")
                message += f"🔴 {taille} [{stock}]\n"
            if stock == "LOW":
                print(f"{GREEN}[{taille}] {stock} {RESET} ", end=" ")
                message += f"🟠 {taille} [{stock}]\n"
            if stock == "MID":
                print(f"{GREEN}[{taille}] {stock} {RESET} ", end=" ")
                message += f"🟡 {taille} [{stock}]\n"
            if stock == "HIGH":
                print(f"{GREEN}[{taille}] {stock} {RESET} ", end=" ")
                message += f"🟢 {taille} [{stock}]\n"
    else:
        print("error sizes\n")
        message += "erroe sizes\n"
    print()
    embed = discord.Embed(
        title=titleEmbed, 
        description=message, 
        color=0x000000 # Format hexadécimal pur pour discord.py
    )
    embed.set_image(url=imgLink)
    embed.set_footer(
        text="Nike Availability Scraper", 
        icon_url='https://cdn.discordapp.com/attachments/1520092588198199478/1520092618082615386/nike.jpg'
    )
    return embed

def parseDataStock():
    file = open('nike_stock_data.json', "r")
    lines = file.readlines()
    stock = {}
    for line in lines:
        if "localizedLabel" in line:
            tmp = line.split(":")
            tmp[1] = tmp[1].strip()
            tmp[1] = tmp[1].strip(",")
            tmp[1] = tmp[1].strip("\"")
            size = tmp[1]
        if "ship" in line:
            level = line.split(":")
            if level[1]:
                level[1] = level[1].strip()
                level[1] = level[1].strip(",")
                level[1] = level[1].strip("\"")
                infos = level[1]
                if size and infos:
                    stock[size] = infos
    os.remove('nike_stock_data.json')
    return stock
