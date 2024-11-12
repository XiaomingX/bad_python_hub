from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/import_object", methods=['POST'])
def import_object():
    data = request.files.get('user_file').read()
    user_object = pickle.loads(data)  # 危险的反序列化操作
    return 'OK'