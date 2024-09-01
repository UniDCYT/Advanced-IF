import discord #line:1
from discord .ext import commands #line:2
from discord .ui import Button ,View #line:3
import os #line:4
intents =discord .Intents .default ()#line:5
intents .messages =True #line:6
intents .guilds =True #line:7
intents .message_content =True #line:8
bot =commands .Bot (command_prefix ="!",intents =intents )#line:9
CHANNEL_ID =1274309419022155846 #line:10
ROLE_ID =1274309768634171443 #line:11
COMMAND_CHANNEL_ID =1274309278907367504 #line:12
AUTHORIZED_ROLE_ID =1272823826606067744 #line:13
class VerificationView (View ):#line:14
    def __init__ (O00O0OOOOOOOOO0OO ,O0O0OO0000OOOOO0O ):#line:15
        super ().__init__ ()#line:16
        O00O0OOOOOOOOO0OO .role_id =O0O0OO0000OOOOO0O #line:17
    @discord .ui .button (label ="Verify",style =discord .ButtonStyle .green ,custom_id ="verify_button")#line:18
    async def verify (O0OO0OO00OOO00OO0 ,O000O00O0000OOO0O :discord .Interaction ,OO0O00OOOOOOO0000 :discord .ui .Button ):#line:19
        OO0OO00000000OOO0 =O000O00O0000OOO0O .guild #line:20
        O00OO0O0OOOO0OOOO =O000O00O0000OOO0O .user #line:21
        OOO0000O00OOOO0O0 =OO0OO00000000OOO0 .get_role (O0OO0OO00OOO00OO0 .role_id )#line:22
        if OOO0000O00OOOO0O0 is None :#line:23
            await O000O00O0000OOO0O .response .send_message ("Role not found.",ephemeral =True )#line:24
            return #line:25
        if OOO0000O00OOOO0O0 in O00OO0O0OOOO0OOOO .roles :#line:26
            await O000O00O0000OOO0O .response .send_message ("You are already verified.",ephemeral =True )#line:27
            return #line:28
        await O00OO0O0OOOO0OOOO .add_roles (OOO0000O00OOOO0O0 )#line:29
        await O000O00O0000OOO0O .response .send_message ("You have been verified and given the role!",ephemeral =True )#line:30
@bot .event #line:31
async def on_ready ():#line:32
    print (f'Logged in as {bot.user}')#line:33
    O0OOO00OO00O00O0O =bot .get_channel (CHANNEL_ID )#line:34
    if O0OOO00OO00O00O0O is None :#line:35
        print ("Verification channel not found")#line:36
        return #line:37
    async for OOO0OO00OOO0OO00O in O0OOO00OO00O00O0O .history (limit =100 ):#line:38
        await OOO0OO00OOO0OO00O .delete ()#line:39
    O000OOOOO000OO00O =discord .Embed (title ="Verification",description ="Click the button below to verify",color =0x00ff00 )#line:40
    O0O00O00000000000 =VerificationView (role_id =ROLE_ID )#line:41
    await O0OOO00OO00O00O0O .send (embed =O000OOOOO000OO00O ,view =O0O00O00000000000 )#line:42
    O00OOO0O00OOOOO00 =bot .get_channel (1274312988655878168 )#line:43
    if O00OOO0O00OOOOO00 is None :#line:44
        print ("Ping channel not found")#line:45
        return #line:46
    async for OOO0OO00OOO0OO00O in O00OOO0O00OOOOO00 .history (limit =100 ):#line:47
        await OOO0OO00OOO0OO00O .delete ()#line:48
    O000OOOOO000OO00O =discord .Embed (title ="Choose What Channels You Want Pings From",description ="Click the buttons below to select your preferences.",color =0x00ff00 )#line:49
    O0O00O00000000000 =View ()#line:50
    OOOO0O0O000OOOO0O =Button (label ="YouTube Pings",style =discord .ButtonStyle .red ,custom_id ="youtube_pings")#line:51
    O0O0000O00O00OO00 =Button (label ="Announcements Ping",style =discord .ButtonStyle .green ,custom_id ="announcements_ping")#line:52
    O0O00O00000000000 .add_item (OOOO0O0O000OOOO0O )#line:53
    O0O00O00000000000 .add_item (O0O0000O00O00OO00 )#line:54
    await O00OOO0O00OOOOO00 .send (embed =O000OOOOO000OO00O ,view =O0O00O00000000000 )#line:55
@bot .event #line:56
async def on_interaction (OO000000OO0O0OOOO :discord .Interaction ):#line:57
    if OO000000OO0O0OOOO .type ==discord .InteractionType .component :#line:58
        if OO000000OO0O0OOOO .custom_id =="youtube_pings":#line:59
            OOO00O0O00OOO0OOO =OO000000OO0O0OOOO .guild .get_role (1274313008050601995 )#line:60
            if OOO00O0O00OOO0OOO :#line:61
                await OO000000OO0O0OOOO .user .add_roles (OOO00O0O00OOO0OOO )#line:62
                await OO000000OO0O0OOOO .response .send_message ("You have been given the YouTube pings role!",ephemeral =True )#line:63
            else :#line:64
                await OO000000OO0O0OOOO .response .send_message ("Role not found.",ephemeral =True )#line:65
        elif OO000000OO0O0OOOO .custom_id =="announcements_ping":#line:66
            OOO00O0O00OOO0OOO =OO000000OO0O0OOOO .guild .get_role (1274703518565011476 )#line:67
            if OOO00O0O00OOO0OOO :#line:68
                await OO000000OO0O0OOOO .user .add_roles (OOO00O0O00OOO0OOO )#line:69
                await OO000000OO0O0OOOO .response .send_message ("You have been given the Announcements pings role!",ephemeral =True )#line:70
            else :#line:71
                await OO000000OO0O0OOOO .response .send_message ("Role not found.",ephemeral =True )#line:72
@bot .command (name ='DownloadPro')#line:73
async def download_pro (OOOOO0O000O000OO0 ):#line:74
    if OOOOO0O000O000OO0 .channel .id !=COMMAND_CHANNEL_ID :#line:75
        await OOOOO0O000O000OO0 .send ("This command can only be used in the designated channel.",delete_after =10 )#line:76
        return #line:77
    await OOOOO0O000O000OO0 .message .delete ()#line:78
    OO0O0O00O0OO00O00 =discord .Embed (title ="Download Windows 10-11 Pro Advanced IF Installer",description ="Click the button below to download.",color =0x0000ff )#line:79
    OO000O00000O0OOOO =View ()#line:80
    OOOO0O0O00000O0OO =Button (label ="Download",style =discord .ButtonStyle .red ,url ="https://raw.githubusercontent.com/UniDCYT/Advanced-IF/main/ProInstaller.bat")#line:81
    OO000O00000O0OOOO .add_item (OOOO0O0O00000O0OO )#line:82
    await OOOOO0O000O000OO0 .send (embed =OO0O0O00O0OO00O00 ,view =OO000O00000O0OOOO )#line:83
@bot .command (name ='DownloadFree')#line:84
async def download_free (O00000OOO00O0000O ):#line:85
    if O00000OOO00O0000O .channel .id !=COMMAND_CHANNEL_ID :#line:86
        await O00000OOO00O0000O .send ("This command can only be used in the designated channel.",delete_after =10 )#line:87
        return #line:88
    await O00000OOO00O0000O .message .delete ()#line:89
    OO0000OO00O000O00 =discord .Embed (title ="Download Windows 10-11 Free/Non-Pro Installer",description ="Click the button below to download.",color =0x00ff00 )#line:90
    OO0OO0OOOO0O00OO0 =View ()#line:91
    O0O00O0O00O000O00 =Button (label ="Download",style =discord .ButtonStyle .green ,url ="https://raw.githubusercontent.com/UniDCYT/Advanced-IF/main/FreeInstaller.bat")#line:92
    OO0OO0OOOO0O00OO0 .add_item (O0O00O0O00O000O00 )#line:93
    await O00000OOO00O0000O .send (embed =OO0000OO00O000O00 ,view =OO0OO0OOOO0O00OO0 )#line:94
@bot .command (name ='VerifyAll')#line:95
@commands .has_role (AUTHORIZED_ROLE_ID )#line:96
async def verify_all (OO0OOO0O0000OOO00 ):#line:97
    if OO0OOO0O0000OOO00 .channel .id !=COMMAND_CHANNEL_ID :#line:98
        await OO0OOO0O0000OOO00 .send ("This command can only be used in the designated channel.",delete_after =10 )#line:99
        return #line:100
    OOO0O00O000OOO0OO =discord .utils .get (OO0OOO0O0000OOO00 .guild .roles ,id =ROLE_ID )#line:101
    if OOO0O00O000OOO0OO is None :#line:102
        await OO0OOO0O0000OOO00 .send ("Verification role not found.",delete_after =10 )#line:103
        return #line:104
    OOOO00OO0OOOO0OO0 =[]#line:105
    O0OO0O000OOOO0OO0 =[]#line:106
    for O0OO0000OO0O00OOO in OO0OOO0O0000OOO00 .guild .members :#line:107
        if OOO0O00O000OOO0OO not in O0OO0000OO0O00OOO .roles :#line:108
            try :#line:109
                await O0OO0000OO0O00OOO .add_roles (OOO0O00O000OOO0OO )#line:110
                OOOO00OO0OOOO0OO0 .append (O0OO0000OO0O00OOO .name )#line:111
            except Exception as O00O0O0OOO00OO0OO :#line:112
                O0OO0O000OOOO0OO0 .append (f"{O0OO0000OO0O00OOO.name} ({O00O0O0OOO00OO0OO})")#line:113
    O0O0O00OOO00O0O00 ="\n".join (OOOO00OO0OOOO0OO0 )if OOOO00OO0OOOO0OO0 else "None"#line:114
    OOOOOO000O00OOO0O ="\n".join (O0OO0O000OOOO0OO0 )if O0OO0O000OOOO0OO0 else "None"#line:115
    O00O0O0O0O000O0OO =discord .Embed (title ="Verification Status",description =f"Verified Members:\n{O0O0O00OOO00O0O00}\n\nMembers Not Verified:\n{OOOOOO000O00OOO0O}",color =0x00ff00 )#line:116
    await OO0OOO0O0000OOO00 .send (embed =O00O0O0O0O000O0OO )#line:117
@bot .command (name ='embed')#line:118
@commands .has_role (AUTHORIZED_ROLE_ID )#line:119
async def embed (O00O00OOOO0O000O0 ,*,content :str ):#line:120
    try :#line:121
        O0O000O0O0OOOOO00 =content .index ('(')+1 #line:122
        OOOOOO00000OOO0O0 =content .index (')')#line:123
        OO00O00OOOO0000OO =content [O0O000O0O0OOOOO00 :OOOOOO00000OOO0O0 ].strip ().lower ()#line:124
        OOOO0O00O0O0O0OOO =content [OOOOOO00000OOO0O0 +1 :].strip ()#line:125
        OO00000O000OO0OO0 =OOOO0O00O0O0O0OOO .index ('(')+1 #line:126
        OOO0O00O00O0OOO0O =OOOO0O00O0O0O0OOO .index (')')#line:127
        O0O0O0OO000OOOOOO =OOOO0O00O0O0O0OOO [OO00000O000OO0OO0 :OOO0O00O00O0OOO0O ].strip ()#line:128
        O0000O00O0O0OOOO0 =OOOO0O00O0O0O0OOO [OOO0O00O00O0OOO0O +1 :].strip ()#line:129
        O0O000O000O0OOO00 ={'red':0xff0000 ,'green':0x00ff00 ,'blue':0x0000ff ,'yellow':0xffff00 ,'purple':0x800080 ,'orange':0xffa500 ,'white':0xffffff ,'black':0x000000 }#line:130
        OO000O00O0O00OO0O =O0O000O000O0OOO00 .get (OO00O00OOOO0000OO ,0xffffff )#line:131
        print (f"Color value used: {OO000O00O0O00OO0O}")#line:132
        O0OOOO0OO00OOO0OO =discord .Embed (title =O0O0O0OO000OOOOOO ,description =O0000O00O0O0OOOO0 ,color =OO000O00O0O00OO0O )#line:133
        await O00O00OOOO0O000O0 .message .delete ()#line:134
        await O00O00OOOO0O000O0 .send (embed =O0OOOO0OO00OOO0OO )#line:135
    except ValueError :#line:136
        await O00O00OOOO0O000O0 .send ("Invalid command format. Please use: !embed (color) (title) description")#line:137
    except Exception as O00O0OO0O00OO0O00 :#line:138
        await O00O00OOOO0O000O0 .send (f"An error occurred: {str(O00O0OO0O00OO0O00)}")#line:139
def load_token ():#line:140
    O00O0000OO0000OOO ='Token.txt'#line:141
    if not os .path .isfile (O00O0000OO0000OOO ):#line:142
        raise FileNotFoundError (f"Token file not found: {O00O0000OO0000OOO}")#line:143
    with open (O00O0000OO0000OOO ,'r')as OOOO0OO000O0OOO0O :#line:144
        OO00OOOOOOO000000 =OOOO0OO000O0OOO0O .read ().strip ()#line:145
    if not OO00OOOOOOO000000 :#line:146
        raise ValueError ("Token file is empty.")#line:147
    return OO00OOOOOOO000000 #line:148
TOKEN =load_token ()#line:149
bot .run (TOKEN )#line:150
