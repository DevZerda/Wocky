## Modules
import sys, os, time

## Files
from ..utils.main import *
from ..utils.db_stats import *
from ..Config.main import *


class BannerModify:
    def GetBannerFromFile(filee):
        slash = None
        if OS_Func.GetOSType() == True:
            slash = "/"
        else:
            slash = "\\"
            
        ## isnt reading file data or character symbols from file [THIS NEEDS TO BE FIXED]
        try:
            BannerFile = open(f"{os.getcwd()}/assets/banner_system/banners/{filee}.txt","r", encoding="utf-8")
            BannerFile = BannerFile.read()
        except:
            print("Error")
            BannerFile = "Failed"

        return BannerFunc.ColorBanner(BannerFile)
        

class BannerFunc():

    def ColorBanner(bnnr):
        bnnr = bnnr.replace("\n", "\r\n")
        bnnr = bnnr.replace("{RED}", Strings.MainColors['Red'])
        bnnr = bnnr.replace("{YELLOW}", Strings.MainColors['Yellow'])
        bnnr = bnnr.replace("{BLUE}", Strings.MainColors['Blue'])
        bnnr = bnnr.replace("{PURPLE}", Strings.MainColors['Purple'])
        bnnr = bnnr.replace("{GREEN}", Strings.MainColors['Green'])
        bnnr = bnnr.replace("{BLACK}", Strings.MainColors['Black'])
        bnnr = bnnr.replace("{GREY}", Strings.MainColors['Grey'])
        bnnr = bnnr.replace("{CYAN}", Strings.MainColors['Cyan'])
        bnnr = bnnr.replace("{WHITE}", Strings.MainColors['White'])
        bnnr = bnnr.replace("{RESET}", Strings.MainColors['Reset'])
        bnnr = bnnr.replace("{BG_BLACK}", Strings.MainColors['Background_Black'])
        bnnr = bnnr.replace("{BG_RED}", Strings.MainColors['Background_Red'])
        bnnr = bnnr.replace("{BG_GREEN}", Strings.MainColors['Background_Green'])
        bnnr = bnnr.replace("{BG_YELLOW}", Strings.MainColors['Background_Yellow'])
        bnnr = bnnr.replace("{BG_BLUE}", Strings.MainColors['Background_Blue'])
        bnnr = bnnr.replace("{BG_PURPLE}", Strings.MainColors['Background_Purple'])
        bnnr = bnnr.replace("{BG_CYAN}", Strings.MainColors['Background_Cyan'])
        bnnr = bnnr.replace("{BG_LIGHTGREY}", Strings.MainColors['Background_LightGrey'])
        bnnr = bnnr.replace("{BG_DARKGREY}", Strings.MainColors['Background_DarkGrey'])
        bnnr = bnnr.replace("{BG_LIGHTRED}", Strings.MainColors['Background_LightRed'])
        bnnr = bnnr.replace("{BG_LIGHTGREEN}", Strings.MainColors['Background_LightGreen'])
        bnnr = bnnr.replace("{BG_LIGHTYELLOW}", Strings.MainColors['Background_LightYellow'])
        bnnr = bnnr.replace("{BG_RESET}", Strings.MainColors['Background_Reset'])

        bnnr = bnnr.replace("{CLEAR}", Strings.MainColors['Clear'])
        bnnr = bnnr.replace("{NEWLINE}", "\r\n")

        
        bnnr = bnnr.replace("{TOTALUSERS}", str(db_Stats.TotalUsers()))
        bnnr = bnnr.replace("{ONLINEUSERS}", str(db_Stats.OnlineUsers()))
        bnnr = bnnr.replace("{TOTALATTACKS}", str(db_Stats.TotalAttack()))

        bnnr = bnnr.replace("{USERNAME}", Strings.CurrentUser)
        bnnr = bnnr.replace("{CURRENTIP}", Strings.CurrentIP)
        bnnr = bnnr.replace("{CURRENTRANK}", Strings.CurrentLvl)
        bnnr = bnnr.replace("{CURRENTMTIME}", Strings.CurrentMtime)
        bnnr = bnnr.replace("{CURRENTCONN}", Strings.CurrentConn)
        bnnr = bnnr.replace("{CURRENTADMIN}", Strings.CurrentAdmin)

        return bnnr # Im pretty sure we will return banner right?

class CustomBannerMaker:
    def CreateMOTD(motd):
        box = "                                                                            "
        boxlen = len(box)

        new_line = str(Strings.MainColors['Purple'] + "MOTD: " + motd + box[len("MOTD: " + motd):len(box)] + Strings.MainColors['Reset'])

        return f"{Strings.MainColors['White']}╔═════════════════════════════════════════════════════════════════════════════╗\r\n║ {new_line}║\r\n╚═════════════════════════════════════════════════════════════════════════════╝\r\n"