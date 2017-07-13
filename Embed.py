embed = discord.Embed(title="Symbiotic Gaming's Biweekly 2v2 Tournament", colour=discord.Colour(0xf955d5))

embed.set_image(url="https://cdn.discordapp.com/attachments/332332366007762945/334859735872438274/Symbioticad1.jpg")
embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/324656102941786113/334850249371942914/Symbiotic2.png")
embed.set_author(name="Symbiotic Gaming", url="https://twitter.com/SymbioticGC?lang=en", icon_url="https://cdn.discordapp.com/attachments/324656102941786113/334850249371942914/Symbiotic2.png")
embed.set_footer(text="Join Symbiotic Gaming Today!", icon_url="https://cdn.discordapp.com/attachments/324656102941786113/334850249371942914/Symbiotic2.png")

embed.add_field(name="Format", value="2v2", inline=True)
embed.add_field(name="Region", value="US East", inline=True)
embed.add_field(name="Date/Time", value="Saturday 8:00pm EST", inline=True)
embed.add_field(name="Check-in", value="Closes at 7:30pm EST", inline=True)
embed.add_field(name="Sign-Ups", value="[Sign-up Here](https://goo.gl/forms/1kAaXcsNKbw0yMx72)", inline=True)
embed.add_field(name="Discord", value="[Join here](https://discord.gg/P6vmHvd)", inline=True)

await bot.say(embed=embed)