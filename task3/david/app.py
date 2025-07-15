from flask import Flask, request, render_template
import os
from io import BytesIO
from gtts import gTTS
import base64

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("input_text", "").strip()
        lang = request.form.get("lang", "ko")

        if not text:
            return render_template("index.html", error="입력된 문장이 없습니다.")

        try:
            fp = BytesIO()
            tts = gTTS(text=text, lang=lang)
            tts.write_to_fp(fp)
            fp.seek(0)
            audio_data = base64.b64encode(fp.read()).decode("utf-8")
            return render_template("index.html", audio=audio_data)

        except Exception as e:
            return render_template("index.html", error="TTS 변환 중 오류가 발생했습니다.")

    return render_template("index.html")

if __name__ == '__main__':
    print("서버 실행 중")
    app.run('0.0.0.0', 8080)
    