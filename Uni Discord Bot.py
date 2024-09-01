import discord #line:1
from discord .ext import commands #line:2
from discord .ui import Button ,View #line:3
import os #line:4
intents =discord .Intents .default ()#line:5
intents .messages =True #line:6
intents .guilds =True #line:7
intents .message_content =True #line:8
bot =commands .Bot (command_prefix ="!",intents =intents )#line:9
VERIFICATION_CHANNEL_ID =1274309419022155846 #line:10
ROLE_ID =1274309768634171443 #line:11
PING_CHANNEL_ID =1274312988655878168 #line:12
YOUTUBE_ROLE_ID =1274313008050601995 #line:13
ANNOUNCEMENTS_ROLE_ID =1274703518565011476 #line:14
DOWNLOAD_CHANNEL_ID =1274309278907367504 #line:15
VERIFY_ALL_CHANNEL_ID =1274309278907367504 #line:16
VERIFY_ROLE_ID =1274309768634171443 #line:17
AUTHORIZED_ROLE_ID =1272823826606067744 #line:18
class VerificationView (View ):#line:19
    def __init__ (O0OO000OOO0O00O0O ,O0O0O00OOOOOO00O0 ):#line:20
        super ().__init__ ()#line:21
        O0OO000OOO0O00O0O .role_id =O0O0O00OOOOOO00O0 #line:22
    @discord .ui .button (label ="Verify",style =discord .ButtonStyle .green ,custom_id ="verify_button")#line:23
    async def verify (O000000OO000000O0 ,O0OOOOO000O00O000 :discord .Interaction ,O0O00OO0000OO000O :discord .ui .Button ):#line:24
        O00O000O00OOO00O0 =O0OOOOO000O00O000 .guild #line:25
        O000000000O00000O =O0OOOOO000O00O000 .user #line:26
        O0O0O0000000000O0 =O00O000O00OOO00O0 .get_role (O000000OO000000O0 .role_id )#line:27
        if O0O0O0000000000O0 is None :#line:28
            await O0OOOOO000O00O000 .response .send_message ("Role not found.",ephemeral =True )#line:29
            return #line:30
        if O0O0O0000000000O0 in O000000000O00000O .roles :#line:31
            await O0OOOOO000O00O000 .response .send_message ("You are already verified.",ephemeral =True )#line:32
            return #line:33
        await O000000000O00000O .add_roles (O0O0O0000000000O0 )#line:34
        await O0OOOOO000O00O000 .response .send_message ("You have been verified and given the role!",ephemeral =True )#line:35
class PingRoleView (View ):#line:36
    def __init__ (OO0O00OOOO00000O0 ):#line:37
        super ().__init__ ()#line:38
    @discord .ui .button (label ="YouTube Pings",style =discord .ButtonStyle .danger ,custom_id ="youtube_pings_button")#line:39
    async def youtube_pings (OO000OOO0000O00OO ,OO0OOOO000OOO0OO0 :discord .Interaction ,O0000000O0000OO00 :discord .ui .Button ):#line:40
        O00OO00O0000OOO0O =OO0OOOO000OOO0OO0 .guild #line:41
        O00O0O00O0O0O000O =OO0OOOO000OOO0OO0 .user #line:42
        OOOO000O000O00O0O =O00OO00O0000OOO0O .get_role (YOUTUBE_ROLE_ID )#line:43
        if OOOO000O000O00O0O is None :#line:44
            await OO0OOOO000OOO0OO0 .response .send_message ("Role not found.",ephemeral =True )#line:45
            return #line:46
        await O00O0O00O0O0O000O .add_roles (OOOO000O000O00O0O )#line:47
        await OO0OOOO000OOO0OO0 .response .send_message ("You have been given the YouTube pings role!",ephemeral =True )#line:48
    @discord .ui .button (label ="Announcements Ping",style =discord .ButtonStyle .danger ,custom_id ="announcements_pings_button")#line:49
    async def announcements_pings (OO000O0OO0O0O0O00 ,OO0O00O0O0O00OO00 :discord .Interaction ,O00O00O0OO00000O0 :discord .ui .Button ):#line:50
        OO00OOOO0OO000OOO =OO0O00O0O0O00OO00 .guild #line:51
        O0OO000OOO0O0O0O0 =OO0O00O0O0O00OO00 .user #line:52
        O0O0OOOOO0O00OO0O =OO00OOOO0OO000OOO .get_role (ANNOUNCEMENTS_ROLE_ID )#line:53
        if O0O0OOOOO0O00OO0O is None :#line:54
            await OO0O00O0O0O00OO00 .response .send_message ("Role not found.",ephemeral =True )#line:55
            return #line:56
        await O0OO000OOO0O0O0O0 .add_roles (O0O0OOOOO0O00OO0O )#line:57
        await OO0O00O0O0O00OO00 .response .send_message ("You have been given the Announcements pings role!",ephemeral =True )#line:58
class DownloadProView (View ):#line:59
    def __init__ (OO0000OOO0O000OOO ):#line:60
        super ().__init__ ()#line:61
    @discord .ui .button (label ="Download Windows 10-11 Pro Installer",style =discord .ButtonStyle .danger ,custom_id ="download_pro_button")#line:62
    async def download_pro (OO0OO0OOOO00O0O00 ,O000O00OOOOO0OO0O :discord .Interaction ,O0OO0OOO0OOO000OO :discord .ui .Button ):#line:63
        OO000O00000O0O00O ='ProInstaller.bat'#line:64
        if os .path .isfile (OO000O00000O0O00O ):#line:65
            await O000O00OOOOO0OO0O .response .send_message (file =discord .File (OO000O00000O0O00O ),ephemeral =True )#line:66
        else :#line:67
            await O000O00OOOOO0OO0O .response .send_message ("File not found.",ephemeral =True )#line:68
class DownloadFreeView (View ):#line:69
    def __init__ (O000O0000OO00OO00 ):#line:70
        super ().__init__ ()#line:71
    @discord .ui .button (label ="Download Windows 10-11 Free Installer",style =discord .ButtonStyle .success ,custom_id ="download_free_button")#line:72
    async def download_free (OO0OOO0O0O00O0O0O ,OO0O000OOOOOO0000 :discord .Interaction ,O0OOO0O00OO000OOO :discord .ui .Button ):#line:73
        O00OO0OO0O0OO000O ='FreeInstaller.bat'#line:74
        if os .path .isfile (O00OO0OO0O0OO000O ):#line:75
            await OO0O000OOOOOO0000 .response .send_message (file =discord .File (O00OO0OO0O0OO000O ),ephemeral =True )#line:76
        else :#line:77
            await OO0O000OOOOOO0000 .response .send_message ("File not found.",ephemeral =True )#line:78
@bot .event #line:79
async def on_ready ():#line:80
    print (f'Logged in as {bot.user}')#line:81
    OOO00000O00O00000 =bot .get_channel (VERIFICATION_CHANNEL_ID )#line:82
    if OOO00000O00O00000 is None :#line:83
        print ("Verification channel not found")#line:84
    else :#line:85
        async for O0O0O000OO0O0OOOO in OOO00000O00O00000 .history (limit =100 ):#line:86
            await O0O0O000OO0O0OOOO .delete ()#line:87
        O0O00OO000OO000O0 =discord .Embed (title ="Verification",description ="Click the button below to verify",color =0x00ff00 )#line:88
        O000O00O0000OO0OO =VerificationView (role_id =ROLE_ID )#line:89
        await OOO00000O00O00000 .send (embed =O0O00OO000OO000O0 ,view =O000O00O0000OO0OO )#line:90
    OOO0OOOO0000000OO =bot .get_channel (PING_CHANNEL_ID )#line:91
    if OOO0OOOO0000000OO is None :#line:92
        print ("Ping roles channel not found")#line:93
    else :#line:94
        async for O0O0O000OO0O0OOOO in OOO0OOOO0000000OO .history (limit =100 ):#line:95
            await O0O0O000OO0O0OOOO .delete ()#line:96
        O0O00OO000OO000O0 =discord .Embed (title ="Choose Your Pings",description ="Click the buttons below to choose what channels you want pings from.",color =0xff0000 )#line:97
        O000O00O0000OO0OO =PingRoleView ()#line:98
        await OOO0OOOO0000000OO .send (embed =O0O00OO000OO000O0 ,view =O000O00O0000OO0OO )#line:99
@bot .command (name ='DownloadPro')#line:100
async def download_pro (OOOO0OO00O0O0OO0O ):#line:101
    if OOOO0OO00O0O0OO0O .channel .id !=DOWNLOAD_CHANNEL_ID :#line:102
        return #line:103
    OO0OOO0O00OOOO0O0 =discord .Embed (title ="Download Windows 10-11 Pro Installer",description ="Click the button below to download the installer.",color =0x0000ff )#line:104
    OOOO0O000O00O00OO =DownloadProView ()#line:105
    try :#line:106
        await OOOO0OO00O0O0OO0O .author .send (embed =OO0OOO0O00OOOO0O0 ,view =OOOO0O000O00O00OO )#line:107
        O0O000O00O000O000 =await OOOO0OO00O0O0OO0O .send ("I have sent you the download link via DM.",delete_after =10 )#line:108
        await O0O000O00O000O000 .delete ()#line:109
    except discord .Forbidden :#line:110
        await OOOO0OO00O0O0OO0O .send ("I was unable to send you a DM. Please make sure your DMs are open.",delete_after =10 )#line:111
@bot .command (name ='DownloadFree')#line:112
async def download_free (OOO00000OOOO00O0O ):#line:113
    if OOO00000OOOO00O0O .channel .id !=DOWNLOAD_CHANNEL_ID :#line:114
        return #line:115
    OOO000OOO00OOOO00 =discord .Embed (title ="Windows 10-11 Free Installer",description ="Click the button below to download the installer.",color =0x0000ff )#line:116
    O0OOO0O0OOOOOOOO0 =DownloadFreeView ()#line:117
    try :#line:118
        await OOO00000OOOO00O0O .author .send (embed =OOO000OOO00OOOO00 ,view =O0OOO0O0OOOOOOOO0 )#line:119
        OOOO000OO00O0OO00 =await OOO00000OOOO00O0O .send ("I have sent you the download link via DM.",delete_after =10 )#line:120
        await OOOO000OO00O0OO00 .delete ()#line:121
    except discord .Forbidden :#line:122
        await OOO00000OOOO00O0O .send ("I was unable to send you a DM. Please make sure your DMs are open.",delete_after =10 )#line:123
@bot .command (name ='VerifyAll')#line:124
@commands .has_role (AUTHORIZED_ROLE_ID )#line:125
async def verify_all (O0O0OOO00000OO0OO ):#line:126
    O0OO00O00000000O0 =O0O0OOO00000OO0OO .guild #line:127
    OO0OOOO0OO0OOOOOO =discord .utils .get (O0OO00O00000000O0 .roles ,id =VERIFY_ROLE_ID )#line:128
    if OO0OOOO0OO0OOOOOO is None :#line:129
        await O0O0OOO00000OO0OO .send ("Verification role not found.")#line:130
        return #line:131
    OO0OO0OO000O000O0 =[]#line:132
    O0O0000O00OO0O0OO =[]#line:133
    for OOOOO00O00OOO00OO in O0OO00O00000000O0 .members :#line:134
        if OO0OOOO0OO0OOOOOO not in OOOOO00O00OOO00OO .roles :#line:135
            await OOOOO00O00OOO00OO .add_roles (OO0OOOO0OO0OOOOOO )#line:136
            O0O0000O00OO0O0OO .append (OOOOO00O00OOO00OO .mention )#line:137
        else :#line:138
            OO0OO0OO000O000O0 .append (OOOOO00O00OOO00OO .mention )#line:139
    OOO0OOO000OO000O0 =""#line:140
    if O0O0000O00OO0O0OO :#line:141
        OOO0OOO000OO000O0 +="The following members were given the verification role:\n"+"\n".join (O0O0000O00OO0O0OO )+"\n"#line:142
    else :#line:143
        OOO0OOO000OO000O0 +="No members needed to be verified.\n"#line:144
    if OO0OO0OO000O000O0 :#line:145
        OOO0OOO000OO000O0 +="The following members were already verified:\n"+"\n".join (OO0OO0OO000O000O0 )+"\n"#line:146
    await O0O0OOO00000OO0OO .send (OOO0OOO000OO000O0 )#line:147
def load_token ():#line:148
    O00OO0O00000OO00O ='Token.txt'#line:149
    if not os .path .isfile (O00OO0O00000OO00O ):#line:150
        raise FileNotFoundError (f"Token file not found: {O00OO0O00000OO00O}")#line:151
    with open (O00OO0O00000OO00O ,'r')as O0OO0O0O0OO0O0O00 :#line:152
        O000O0O00O0O00O0O =O0OO0O0O0OO0O0O00 .read ().strip ()#line:153
    if not O000O0O00O0O00O0O :#line:154
        raise ValueError ("Token file is empty.")#line:155
    return O000O0O00O0O00O0O #line:156
TOKEN =load_token ()#line:157
bot .run (TOKEN )#line:158
