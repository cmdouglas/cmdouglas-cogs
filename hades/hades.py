import random

import discord
from redbot.core import commands

from .gods import characters


class Hades(commands.Cog):
    """Fun commands based on Hades"""

    @commands.command(name="boon")
    async def _boon(self, ctx: commands.Context):
        """Receive a boon from one of the characters of Hades"""
        character = random.choice(characters)
        title = character["name"]
        if character["title"]:
            title += ", " + character["title"]
        quote = '*' + random.choice(character["quotes"]) + '*'
        if character['name'] == 'Cerberus':
            quote = '**Narrator:** ' + quote
        embed = discord.Embed(
            description=quote,
        )
        embed.set_image(url=character["image"])
        embed.set_author(name=title)

        await ctx.send(embed=embed)
