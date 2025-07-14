from flask import Flask
import utils.configs as configs

app = Flask(__name__)
app.secret_key = configs.secret_key  # 用于加密 session

from gateway.index import *
from gateway.geteway import *
from gateway.chatgpt import *
from gateway.login import *
from gateway.timing import *
from gateway.user import *
from gateway.admin import *
from gateway.claude import *

# 启动 Flask 应用
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
