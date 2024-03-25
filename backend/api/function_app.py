# import logging
# import azure.functions as func

# app = func.FunctionApp()
# sudo
# @app.queue_trigger(arg_name="msg", 
#                    queue_name="outqueue", 
#                    connection="AzureWebJobsStorage")
# @app.cosmos_db_input(arg_name="documents", 
#                      database_name="MyDatabase",
#                      collection_name="MyCollection",
#                      id="{msg.payload_property}",
#                      partition_key="{msg.payload_property}",
#                      connection_string_setting="MyAccount_COSMOSDB")
# @app.cosmos_db_output(arg_name="outputDocument", 
#                       database_name="MyDatabase",
#                       collection_name="MyCollection",
#                       connection_string_setting="MyAccount_COSMOSDB")
# def test_function(msg: func.QueueMessage,
#                   inputDocument: func.DocumentList, 
#                   outputDocument: func.Out[func.Document]):
#      document = documents[id]
#      document["text"] = "This was updated!"
#      doc = inputDocument[0]
#      doc["text"] = "This was updated!"
#      outputDocument.set(doc)
#      print(f"Updated document.")

#Trigger - Run a function when an Azure Cosmos DB document is created or modified
#Input Binding - Read an Azure Cosmos DB document
#Output Binding - Save changes to an Azure Cosmos DB document

#Original
import azure.functions as func
import logging
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="GetEKVisitorCounter")
def GetEKVisitorCounter(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )