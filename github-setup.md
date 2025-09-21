# GitHub リポジトリ作成とプッシュ手順

## 1. GitHub でリポジトリを作成
ブラウザで https://github.com/new にアクセスして：
- Repository name: `kobayashi-dental-clinic`
- Description: `小林歯科クリニック公式ウェブサイト`
- Public を選択
- README, .gitignore, license は追加しない（既に作成済み）
- 「Create repository」をクリック

## 2. ローカルからプッシュ
リポジトリ作成後、以下のコマンドを実行：

```powershell
git push -u origin main
```

## 3. GitHub Pages の設定
プッシュ後、GitHub リポジトリページで：
- Settings タブをクリック
- 左メニューから「Pages」をクリック
- Source: 「Deploy from a branch」を選択
- Branch: 「main」を選択、フォルダは「/ (root)」
- 「Save」をクリック

## 4. カスタムドメイン設定（オプション）
GitHub Pages 設定画面で：
- Custom domain に `kobayashi-dental-kasai.com` を入力
- 「Save」をクリック
- Xserver でのDNS設定も必要

## 完了後のURL
- デフォルト: https://wingman0527.github.io/kobayashi-dental-clinic/
- カスタム: https://kobayashi-dental-kasai.com/ （DNS設定後）
