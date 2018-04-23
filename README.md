# ArtaBot
**ArtaBot** is a fully modular bot for Discord, which means the user can enable/disable features to customize as they wish.  
This is a *self-hosted* bot, meaning the user has to host the bot themself.  
The default set of modules are:  
* Self Reminder  
* Mirror the entire text channel to your own channel  
* Simple and easy Wikipedia search result  
* Play music in voice chat (YouTube only)   
* Music Lyrics connected with YouTube videos ***WIP***
* Stream alerts (Twitch) ***WIP***   
* And many more to come!!


# Commands   
**Use !help to get a list of all commands in Discord.**  

***Bot User Features***  
* !reset_name : Set your bot's username to its given username.  
* !set_nickname [@mention] [nickname] : Set a user's nickname. Only usable with right permissions.  
* !set_status [status] : Set the bot's status to anything.  
* !shutdown  
* !restart    
**Common Features**  
* !av [@mention] : Returns the mentioned user's avatar. Can be used multiple like !av [@metion1] [@mention2]. If no mention found, returns the message author's avatar.  
* !dm [message] : Sends a direct message with [message] to the author.  
* !ping : Returns "Pong!"  
* !say [message] : Repeats [message] on the same text channel.      
**Text Channel Mirror Features**  
* !map [source_ID] [destination_ID] : Fetches every text message sent in [source_ID]'s channel, and forwards them to [destination_ID]'s channel.  
* !unmap [source_ID] : Removes the mapped channel.     
**Reminder Feature**  
* !remind [minutes] [message] : Sends the author the [message] in [minutes] minutes.     
**Wiki Feature**  
* !wiki [search] : Returns the closest search query it can find on Wikipedia.     
**Music Features**  
* !summon : Brings bot to the author's voice channel.  
* !play [youtube_URL] : Play the URL's music through voice channel.  
* !stop : Clears the queue, if the queue is already cleared, leave the channel.  
* !volume [0-100] : Sets the volume from 0 to 100.  
* !pause  
* !skip  
* !resume  
