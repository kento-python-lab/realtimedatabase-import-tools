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

def main():
    # outputディレクトリ配下のjsonファイルを順番に読み込みデータベースに投入する
    for json_file_name in listup_files('./output/*'):
        with open(json_file_name, 'r', encoding='utf-8') as f:
            print(f)
            for data in json.load(f):
                import_to_db(data)


# 相対パスでCSVファイル一覧を取得
def listup_files(path):
    return glob.glob(path)

# RealtimeDatabaseへのデータ投入処理
def import_to_db(json_data):

    ## add data to database
    dict_id = ulid.new()
    users_ref = ref.child(str(dict_id))
    users_ref.set(json_data)


if __name__ == "__main__":
    main()
