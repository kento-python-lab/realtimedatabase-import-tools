# coding: UTF-8

import os
from os.path import join, dirname
from dotenv import load_dotenv
import json
import glob
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import ulid


# 環境変数読み込み
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# RealtimeDatabaseのURL
DATABASE_URL = os.environ.get('DATABASE_URL')
# 書き込み権限認証コード
UID = os.environ.get('UID')
# ドキュメント名
DATABASE_DOC = os.environ.get('DATABASE_DOC')
# データベース接続認証コード類
cred = credentials.Certificate('./serviceAccountKey.json')

# データベース接続
firebase_admin.initialize_app(cred, {
    'databaseURL': DATABASE_URL,
    'databaseAuthVariableOverride': {
        'uid': UID
    }
})

# ドキュメント名の指定（存在しない場合作成される）
ref = db.reference(DATABASE_DOC)
ref.delete()
