# Load Obj Sequence as Shape Keys
Blender スクリプト

## 概要
このスクリプトは複数のOBJファイルをアクティブなオブジェクトのシェイプキーとしてロードします。生成されるシェイプキーの名称はOBJファイルの名称になります。

このスクリプトのオリジナルは cmomoney 氏が作成して["Merging multiple OBJ files into one file with shape keys"](https://blender.stackexchange.com/questions/58147/merging-multiple-obj-files-into-one-file-with-shape-keys)に公開しているものですが、ここに公開しているのは私(@konoha18537007)がそれにバグの修正と多少の変更を加えたものです。

変更内容は下記の通りです：
  - 読み込んだオブジェクトを削除するプロセス内のロジックの複数のバグを修正
  - メンバ変数の宣言をアノテーションを用いて記述するように変更
  - ファイルIOダイアログが開いた際のデフォルトのロケーションをblendファイルの場所に変更

## 使い方
1. 対象のオブジェクトを選択。

2. "File" > "Import" > "Obj As Shapekey(.obj)" で実行。

## インストール
Edit > Preferences > Add-ons > Install... and select Load_Obj_Sequence_as_Shape_Keys.py

## 注意
* 転送先のオブジェクトに既に転送元と同じ名称のシェイプキーがあった場合、"ほげ.001"のように追加されます。(既存のシェイプキーは上書きされない)

## ライセンス
* オリジナルのスクリプトは blender Stack Exchange に公開されているものです。したがって、このスクリプトのラインセンスも [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) です。
  - [blender Stack Exchange license](https://blender.stackexchange.com/help/licensing)
