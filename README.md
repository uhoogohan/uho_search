# ようこそ Django でなんちゃって検索 へ

Django でアプリケーションを作って、GitHub にアップロードするまでの手順です。GitHub のアカウントをまず作っといてください。
<br>
<br>

## SSHでアクセスできるようにします
<br>

ssh-keygen でキーペアを作って、公開鍵のフィンガープリントを GitHub に登録します。[こちら](https://docs.github.com/ja/authentication/connecting-to-github-with-ssh/about-ssh)を参考にしてください。GitHub は、2021年8月13日をもってパスワード認証を廃止しました。
<br>
<br>
  
  
## GitHub のサイトで新しいリポリトリを作ります
<br>
こんなメッセージが表示されるので、前者を叩きます。
<br>
<br>


### …or create a new repository on the command line

``` bash
echo "# ようこそ" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:uhoogohan/uho_search.git
git push -u origin main
```

### …or push an existing repository from the command line
``` bash
git remote add origin git@github.com:uhoogohan/uho_search.git
git branch -M main
git push -u origin main
```


## Django でアプリケーションを作ったよ
<br>
Django でアプリケーションをつくりました。