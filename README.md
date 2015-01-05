準備
-------------------------------
####  *Homebrew*を導入する
```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```    

####  下記のコマンドを入力し、最新の状態であるか確かめる。
```
brew doctor
brew update
```
  
下記の通り表示されればOK
```
Your system is ready to brew.
```
  
もし、警告が出た場合は下記のサイトを参照し、メッセージが出ないようにする。
+ [コマンドラインでbrew doctorすると警告だらけになっちゃった助けて](http://qiita.com/fumi_042/items/55be8fb37cc23325b7c2)
+ [Homebrewのエラーを治す](http://qiita.com/cubdesign/items/176e655a14d47b374a75)
  
####  下記のコマンドを入力し、最新のpythonのバージョンをインストールする。
```
brew install python
```
  
####  pythonパッケージ管理ツールであるpipを導入する
[get-pip.py](https://bootstrap.pypa.io/get-pip.py)をダウンロードし、下記の通り実行する
```
python get-pip.py
```
(Python 2.7.9以降，又はPython 3.4以降であればpipが既に存在している可能性がある。[pip document](https://pip.pypa.io/en/latest/installing.html))
  
####  numpyとopenCVをインストールする
openCVはnumpyに依存しているため、numpyを先にインストールする必要がある。
```
pip install numpy
pip install openCV
```
  
####  終了
  
