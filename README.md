# realtimedatabase-import-tools

競馬csvデータ(ヘッダー付き)を Firebaseへ移行するためのツール（競馬データ以外にも使用できる）  

## 実行コマンド

```
# ./inputディレクトリ配下のcsvをjsonに変換
$ csv2json.py

# .env と serviceAccountKey.json の情報を元に RealtimeDatabaseにデータをimport
# データが多いとかなり時間がかかる
$ import2firebase.py
```

## データベースルール

```
{
  "rules": {
    "result_data": {
      ".read": "auth.uid === 'my-service-worker'",
      ".write": "auth.uid === 'my-service-worker'"
    }
  }
}
```