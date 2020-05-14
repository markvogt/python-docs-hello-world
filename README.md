# API APP HELLO WORLD PROJECT

For original details see the BOTOM of this readme.md file...

## DAILY JOURNAL by MV

REFERENCE IN DOCS.MICROSOFT.COM: 

https://docs.microsoft.com/en-us/azure/app-service/containers/quickstart-python?tabs=bash

### 2020 05 14 MV: 
- CONTINUED work... 
- INSPECTED exception message... 
- THEORY: my using "-l northcentralus" WASN'T a VALID location? 
- CHANGE location to "-l centralus" per sample article
- RE-DEPLOYED 
- - => SUCCESSFUL deployment to https://mvhelloworld.azurewebsites.net !!
- ADDED additional app route "/detectpage"
- RE-DEPLOYED
- - => SUCCESSFUL deployment to https://mvhelloworld.azurewebsites.net/detectpage !!
- ADDED mock JSON returns to above app route 
- RE-DEPLOYED
- - => SUCCESSFUL deployment & function ! 
- - BROWSING to https://mvhelloworld.azurewebsites.net/detectpage 
-- returns mock JSON  {key1:value1, key2:value2, key3:value3} 
- PAUSED on THIS app - time to CLONE, RENAME and EXPAND !!! 
- UPDATED readme.md (this file)
- COMMITTED and PUSHED...

### 2020 05 13 MV: 
- CONTINUED work on this API App...
- PREPARED to deploy this helloworld app actuall to the Azure Cloud Services
- INSTALLED AzureCLI (for linux) on thing1 
- - => SUCCESSFUL :-)
- RAN commands (locally on thing1 using AzureCLI invoked from VSCode's integrated terminal)
- ATTEMPTED deploy-to-AzureCloud of "mvhelloworld" API app as follows: 
- - $ az webapp up --sku F1 -n "mvhelloworld"
- - => EXCEPTION immediately
- - exception related to MISSING "location" parame (required in AzureCLI 2.5.0 and above)
- ATTEMPTED deploy-to-AzureCloud of mvhelloworld API app as follows: 
- - $ az webapp up --sku F1 -n "mvhelloworld" -l northcentralus
- - => EXCEPTION after 30+ minutes; NOT sure WHY :-( ... 
- PAUSED for the night

### 2020 05 12 MV: 
- FORKED project to cloud repo in github.com (no changes)
- CLONED project down to thing1
- READ reference (see above)
- RAN project as-is ==> SUCCESFUL :-) 

#########################################################################
#########################################################################

---
page_type: sample
description: "This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux."
languages:
- python
products:
- azure
- azure-app-service
---

# Python Flask sample for Azure App Service (Linux)

This is a minimal sample app that demonstrates how to run a Python Flask application on Azure App Service on Linux.

For more information, please see the [Python on App Service quickstart](https://docs.microsoft.com/azure/app-service/containers/quickstart-python).

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
