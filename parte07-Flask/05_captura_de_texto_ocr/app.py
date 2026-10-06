from flask import Flask, render_template, request, send_file
from translate import Translator
import easyocr

import io

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/textoExtraido", methods=["POST"])
def extrair_texto():
    if 'imagem' not in request.files:
        return 'Nenhuma imagem enviada', 400

    imagem = request.files['imagem']

    if imagem.filename == '':
        return 'Nenhuma imagem selecionada', 400

    reader = easyocr.Reader(['en', 'pt'], gpu=False)

    result = reader.readtext(imagem.read())

    texto_extraido = ' '.join([res[1] for res in result])

    return render_template(
        "extracao.html",
        texto=texto_extraido
    )


@app.route("/exportarTexto", methods=['POST'])
def exportar_texto():
    texto = request.form.get("texto", "")

    arquivo_buffer = io.BytesIO(
        texto.encode('utf-8')
    )

    return send_file(
        arquivo_buffer,
        mimetype='text/plain',
        as_attachment=True,
        download_name='texto_extraido.txt'
    )


@app.route("/traducao", methods=['POST'])
def traduzir():
    tradutor = Translator(to_lang="pt")

    texto = request.form.get("texto", "")

    texto_traduzido = tradutor.translate(texto)

    return render_template(
        "extracao.html",
        texto=texto_traduzido
    )


if __name__ == "__main__":
    app.run(debug=True)
