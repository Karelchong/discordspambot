from flask import Flask
import discordaidanspammer.discordaidanspambot# will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return discordaidanspammer.discordaidanspambot.runner()

if __name__ == '__main__':
    app.run()