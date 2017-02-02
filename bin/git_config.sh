#!/bin/bash -f

git config --global http.proxy http://goproxy.micron.com:8080
git config --global https.proxy http://goproxy.micron.com:8080
git config --global url."https://".insteadOf git://
  #git config --global credential.helper cache                    # パスワードを一定時間記憶 うまく動かない。別の方法で。
  #git config --global credential.helper 'cache --timeout=3600'   # パスワード記憶時間を設定 うまく動かない。別の方法で。

git config --global user.name "N.Saito"
git config --global user.email "nytenderberry@gmail.com"
git config --global core.quotepath false
#git config --global gui.encoding utg-8 # 文字化けある場合  utf-8の間違い？

# git diffに色付け
git config --global color.diff auto
git config --global color.status auto
git config --global color.branch auto

git config --global core.editor micro  # エディタ設定

#git config --list   # 設定を確認
#cat ~/.gitconfig    # 設定を確認
