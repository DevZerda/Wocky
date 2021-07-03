import os, sys, time, json


def read_line_c(FilePath):
    filedata = ""
    try:
        filedata = open(FilePath,"r").read()
    except:
        print("Failed")
    return len(filedata.split("\n"))

def read_function(filePath):
    filedata = ""
    try:
        filedata = open(filePath,"r").read()
    except:
        print("Failed")
    lines = filedata.split("\n")
    for line in lines:
        if line.startswith("class"):
            print(line)
        elif line.startswith("def ") or line.startswith("	def ") or line.startswith("    def ") or line.startswith("	def "):
            print(line)

Files = {
    "Main CNC File": ["\\cnc.py", "Main CNC Base"],
    "Attack System": ["\\assets\\api_system\\Main.py", "Read APIs from DB based of the method being used. save time from sending attack to all APIs"],
    "Crud": ["\\assets\\auth\\crud.py", "User CRUD"],
    "CrudFunctions": ["\\assets\\auth\\crudFunc.py", "Extra functions for specific user info pulling"],
    "Main Auth": ["\\assets\\auth\\main.py", "Main Login Function Here"],
    "Banner Modification": ["\\assets\\banner_system\\modify.py", "Text file banner reader and value replacing"],
    "Data Grid Creator": ["\\assets\\banner_system\\datagrid.py", "Data Grid View \\ Box Creator"],
    "CNC Control Panel": ["\\assets\\cnc_controlpanel\\main.py", "Main CP CLI Tool for CNC"],
    "CNC CP Function": ["\\assets\\cnc_controlpanel\\functions.py", "Other CNC functions to communicate with the current box"],
    "Admin Boardcast": ["\\assets\\Commands\\admin_boardcast.py", "Admin Boardcas Command Function"],
    "Admin Handler": ["\\assets\\Commands\\admin_handler.py", "Admin Command Handler"],
    "Attack System": ["\\assets\\Commands\\attack.py", "Temporary Attack System"],
    "Command Handler": ["\\assets\\Commands\\command_handler.py", "Main Command Handler"],
    "DNS Resolver Command": ["\\assets\\Commands\\dns.py", "DNS Resolver Command Function"],
    "Geo Command": ["\\assets\\Commands\\geo.py", "Geo Command Function"],
    "Main Screen Function": ["\\assets\\Commands\\main_screen.py", "Main Screen Function"],
    "Method Command": ["\\assets\\Commands\\methods.py", "Methods Commands Function"],
    "MSG Command": ["\\assets\\Commands\\msg.py", "MSG Command Function"],
    "New Command added by BETA": ["\\assets\\Commands\\mtr.py", "CURRENTLY UNKNOWN FUNCTION"],
    "Port Scanner Command": ["\\assets\\Commands\\portscan.py", "Port Scanner Command Function"],
    "Config Functions": ["\\assets\\Config\\functions.py", "Config Functions"],
    "Net Config": ["\\assets\\Config\\main.py", "Net Config \\ Settings"],
    "Discord LOgger": ["\\assets\\Logger\\discord.py", "Discord Webhook Sender"],
    "Logger": ["\\assets\\Logger\\main.py", "Main File Logger"],
    "CLI": ["\\assets\\utils\\CLI.py", "CLI Graphical\\Controller Control"],
    "Db Lookup": ["\\assets\\utils\\db_lookup.py", "Net Logs Lookup"],
    "Db Stats": ["\\assets\\utils\\db_stats.py", "Net Statistic Counts"],
    "Error Handler": ["\\assets\\utils\\error_handler.py", "Error Handler"],
    "Main Utils": ["\\assets\\utils\\main.py", "utils"],
    "Python Check": ["\\assets\\utils\\python_check.py", "Python3 Check and Module installations"]
}
TotalLineCount = 0
for v in Files:
    # print(f"File Reason: {v}")
    FilePath = os.getcwd() + Files[v][0]
    # gang = read_line_c(FilePath)
    # TotalLineCount += int(gang)
    print(f"File Path: {FilePath}")
    read_function(FilePath)
    # print(f"Line Count: {gang}")
    # print(f"File Description: {Files[v][1]}")
    print("___________________________________________________________")

print(f"Total Files: {len(Files)} | Total Line Count: {TotalLineCount}")
