## 写真を整理して配置するスクリプトです

DropboxのCamera Uploadsフォルダの中を、年/月/日のフォルダに振り分けて配置するスクリプトです。

### 必要環境

Python 2.5 < 3.x

### 使い方

#### Windowsの方

もしPythonをインストールしていない場合、  
[http://www.python.jp/Zope/download/pythoncore](http://www.python.jp/Zope/download/pythoncore)からWindows用のPythonをダウンロードしてインストールして下さい。  
Pythonのバージョンは**2.7.x(2012/5/3時点だと2.7.3)**を選択して下さい。

'arrangement.py', 'win.bat', 'win_test.bat' を下図のように、Camera Uploadsフォルダ直下に配置します。

Camera Uploads  
├── arrangement.py  
├── win.bat  
└── win_test.bat  

#### Macの方

'arrangement.py', 'mac.command', 'mac_test.command' を下図のようにCamera Uploadsフォルダ直下に配置します。

Camera Uploads  
├── arrangement.py  
├── mac.command  
└── mac_test.command  

#### テストスクリプトを動かそう

'win_test.bat'(Macの方は'mac_test.command')をダブルクリックして下さい。写真の配置が始まります。  
テストスクリプトはCamera Uploads直下にある写真ファイルを削除しません。

#### テストスクリプトが上手く動いたら

写真配置が上手くいっているようであれば、'xxx_test'系のファイルは削除して構いません。  
'_test'がついていないファイル'win.bat'('mac.command')をダブルクリックして下さい。  
ファイル配置(既に配置済みの場合はスキップ)が行われ、Camera Uploads直下の写真は削除されます。

#### 他のスクリプトは？

'win_nodate.bat', 'mac_nodate.command'のように_nodateがついているスクリプトは日付フォルダを生成しません。  
'Camera Uploads/年/月/写真ファイル'  
のように配置します。日付フォルダが不要な場合はこちらを使って下さい。
