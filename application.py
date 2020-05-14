from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("HANDLING request to 'root' route '/'...")
    return "Hello World!"

@app.route("/detectpage")
def detectPage():
    print("HANDLING request to 'detectPage' route '/detectpage'...")
    print("BEGIN EXECUTING function detectPage(image)...")

    # CREATE variable incomingImage...

    # CREATE & INITIALIZE a variable jsonPayload (this will be the final output)...

    # COMPOSE HTTP request of incomingImage to PEEM...

    # SEND HTTP request & RECEIVE all detected objects as JSON output...

    # PROCESS JSON to OCR each object to extract its text...
    
    # PROCESS resulting OCR to determine & keep 'desirable' SH, SSH & PA sub-images...

    # CHERRY-PICK only the JSON key:value pairs required as output...

    # POPULATE the variable jsonPayload... 

    # TEMPORARY ! create a MOCKED-UP jsonPayload
    jsonPayload = "{key1:value1, key2:value2, key3:value3}"
    # RETURN the variable jsonPayload...
    return jsonPayload 