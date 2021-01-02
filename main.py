# -----------------------------------------------------------------------------
# practice some python
# -----------------------------------------------------------------------------

import tableHandling
import pingHandler
import showStatus

# check & create tables
tableHandling.checkExists()

# check for new hostname or starting mode
oMode = showStatus.enterNewHost()

# start action depending om mode
if(oMode == "-v"):  # verbose mode - start ping without result
    pingHandler.startPingHandle()
    showStatus.Loop()
elif(oMode == "-o"):  # show output only
    showStatus.showPingsLoop()
else: # Standard mode: start ping and show result
    pingHandler.startPingHandle()
    showStatus.showPingsLoop()
