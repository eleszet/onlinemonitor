import tableHandling
import pingHandler
import showStatus
import sys

# use passed argument if available
oMode = ""
if(len(sys.argv) > 1):
    oMode = sys.argv[1]
    print("Argument passed")

# check & create tables
tableHandling.checkExists()

# check for new hostname or starting mode
if(oMode == ""):
    oMode = showStatus.enterNewHost()

# start action depending om mode
if(oMode == "-v"):  # verbose mode - start ping without result
    pingHandler.startPingHandle()
    showStatus.Loop()
elif(oMode == "-o"):  # show output only
    showStatus.showPingsLoop()
else:  # Standard mode: start ping and show result
    pingHandler.startPingHandle()
    showStatus.showPingsLoop()
