import azure.functions as func
import logging


from top import one
from top import two
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

app.register_functions(one.blueprint)
app.register_functions(two.blueprint)




@app.route(route="health")
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("", status_code=200)

# blueprint = func.Blueprint()

# @blueprint.function_name(name="DemoFunc")
# @blueprint.route(route="demo")
# def demo(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function processed a request.')

#     name = req.params.get('name')
#     if not name:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             name = req_body.get('name')

#     if name:
#         return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
#              status_code=200
#         )
