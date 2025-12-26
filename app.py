from flask import Flask, Response, request

from scraper import scrape_and_build_response

app = Flask(__name__)


@app.post("/sms")
def sms_reply() -> Response:
    message_body = request.form.get("Body", "").strip()
    if not message_body:
        reply_text = "No command text received. Send a search query to continue."
    else:
        reply_text = scrape_and_build_response(message_body)

    twiml = f"""<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<Response>
  <Message>{reply_text}</Message>
</Response>"""
    return Response(twiml, mimetype="application/xml")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
