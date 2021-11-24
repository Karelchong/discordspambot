from flask import Flask
import discordaidanspambot

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    discordaidanspammer.runner()
    return "Hij is aangezet"

if __name__ == '__main__':
    app.run()
