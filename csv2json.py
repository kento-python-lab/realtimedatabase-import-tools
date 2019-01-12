# coding: UTF-8

import os
import json
import csv
import glob


# 相対パスでCSVファイル一覧を取得
def listup_files(path):
    return glob.glob(path)

def main():
    for csv_file_name in listup_files('./input/*'):
        json_list = []
        # CSV ファイルの読み込み
        print(csv_file_name)
        with open(csv_file_name, 'r', encoding='utf-8') as f:
            print(csv.DictReader(f))
            for row in csv.DictReader(f):
                print(row)
                json_list.append(row)

        json_file_name = os.path.basename(csv_file_name)
        # JSON ファイルへの書き込み
        with open('./output/' + json_file_name + '.json', 'w', encoding='utf-8') as f:
            json.dump(json_list, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
