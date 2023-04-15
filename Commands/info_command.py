import discord

async def on_message(message):
  # Ignore messages that are not from a guild
  if message.guild is None:
    return

  # Split the message into command and arguments
  split_message = message.content.split(" ")
  command = split_message[0]
  args = split_message[1:]

  # If the command is "/info", display the requested information
  if command == "/info":
    # Get the member object for the target user
    if len(args) == 0:
      # If no user is specified, use the user who sent the message as the target
      member = message.author
    else:
      # Try to get the target user from the mention or user ID
      target_user = args[0]
      member = message.mentions[0] if message.mentions else None
      if member is None:
        # If the target user was not mentioned, try to get the user by ID
        try:
          user_id = int(target_user)
          member = message.guild.get_member(user_id)
        except ValueError:
          pass
      if member is None:
        # If the target user was not found, send an error message and return
        await message.channel.send("User not found")
        return

    # Get the member's join date, guild, username, and avatar URL
    discord_join_date = member.created_at
    guild_join_date = member.joined_at
    username = member.display_name
    avatar_url = member.display_avatar

    formatted_discord_join_date = discord_join_date.strftime("%b %d, %Y")
    formatted_guild_join_date = guild_join_date.strftime("%b %d, %Y")
    
    # Create an embed object and set the title, thumbnail, and fields
    embed = discord.Embed(title=f"Information for {username}", color = 0x660066)
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="Discord Join Date", value=formatted_discord_join_date)
    embed.add_field(name="Guild Join date", value=formatted_guild_join_date)

    # Send the embed to the text channel
    await message.channel.send(embed=embed)
# End of /info command