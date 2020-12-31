#-----------------------------------------------------------------------------
# practicing some python
# - using different files / functions
# - using local postgres DB wit hsome create/select/delete statements
# - show & maintain a host table
# - execute several ping commands parallel and store the result in a table
#-----------------------------------------------------------------------------

import tableHandling
import pingHandler
import showStatus

# check & create tables
tableHandling.checkExists()

# check for new hostname and insert
showStatus.enterNewHost()

# start ping handles
pingHandler.startPingHandle()

#pingThread.join()
showStatus.showHostList()