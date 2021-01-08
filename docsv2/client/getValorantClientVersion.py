# In the next line you need to put your game directory following the example.
gameDir = r'F:\Juegos\Valorant\Riot Games\VALORANT\live\ShooterGame\Binaries\Win64'

def getClientVer(offset=1.65, readLen=7.5):
    with open(gameDir + r'\VALORANT-Win64-Shipping.exe', 'rb') as gameBin:
        gameBin.seek(0, 2)
        gameBin.seek( int(gameBin.tell() / offset) )
        clientverB = gameBin.read( int(gameBin.tell() / readLen) ).rsplit('++Ares-Core+'.encode('utf-16-le'), 1)[-1][:96]
        clientverList = list( filter(None, clientverB.decode('utf-16-le').split('\x00')) )
        return '-'.join( [ clientverList[0], clientverList[2], clientverList[3].rsplit('.', 1)[-1].lstrip('0') ] )

print(getClientVer(offset=1.65, readLen=7.5))   # modify parameter values if needed

# prints "release-01.14-32-502227" as "branch-buildversion-changelist"

# clientverList = ['release-01.14', 'Dec 10 2020', '32', '01.14.00.0502227']
#
# clientverList[0] = "branch"
# clientverList[1] = "build date" -> "MMM dd yyyy"
# clientverList[2] = "buildversion"
# clientverList[3] = "major.minor.micro.changelist" ->  major: 2 digit EPISODE number (leading 0)
#                                                       minor: 2 digit PATCH number (leading 0)
#                                                       micro (a.k.a. patch) SEEMS to be always '00'
#                                                       changelist: 7 digit number (leading zeros)
# Full credits to @floxay in GitHub
