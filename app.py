from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('iNKbR7CzizerALI+U6ijJQQOR8vbs0sHa25SxP1TCxdLePGFESUBUYJTNcgmVUrscZ/T38f5R/KP/7jTj505OxQzfvHYVEp5k6vdAfMcYGx+dXq6VbV+V5+3pmKYHrBLfLi9SUhJ8DQ5riXGQBsDswdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('0c59aaa9a5fa84754fffc133d7446e52')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()