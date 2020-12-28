from generator.haiku_generator import generate_haiku
from flask import Flask, render_template, request
# Flaskとrender_template（HTMLを表示させるための関数）をインポート


# Flaskオブジェクトの生成
app = Flask(__name__)

# 「/」へアクセスがあった場合に、"Hello World"の文字列を返す


@app.route("/")
def hello():
    app.logger.debug('debug')
    app.logger.info('info')
    app.logger.warn('warn')
    app.logger.error('error')
    app.logger.critical('critical')
    return "Hello World"


@app.route("/get_haiku", methods=["get"])
def get_haiku():
    key1 = request.args.get("key1", '')
    key2 = request.args.get("key2", '')
    key3 = request.args.get("key3", '')
    prefix = request.args.get("prefix", '')
    app.logger.debug(f"key1:{key1} key2:{key2} key3:{key3} prefix: {prefix}")
    haiku = generate_haiku(key1=key1, key2=key2, key3=key3, prefix=prefix)
    return f"key:{key1}, {key2}, {key3}\nprefix: {prefix}\noutput: {haiku}"


if __name__ == "__main__":
    app.run(debug=True)
