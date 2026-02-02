from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Aquí puedes usar un link de streaming real o un archivo MP3 de prueba
    stream_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" 
    return render_template('index.html', stream_url=stream_url)

if __name__ == '__main__':
    app.run(debug=True)
