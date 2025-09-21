# GitHub Pages デプロイ用ファイル

## 手動デプロイ手順

1. GitHub でリポジトリ作成
   - リポジトリ名: `kobayashi-dental-clinic`
   - Public に設定

2. ローカルファイルをアップロード
   - `frontend/dist/` の中身を全てアップロード
   - この README.md も一緒に

3. GitHub Pages 設定
   - Settings → Pages
   - Source: Deploy from a branch  
   - Branch: main
   - Folder: / (root)

## ファイル一覧
- index.html (メインページ)
- 404.html (SPA対応)
- CNAME (カスタムドメイン用)
- assets/ (JS/CSS/画像)
- favicon.svg

## URL
- デフォルト: https://wingman0527.github.io/kobayashi-dental-clinic/
- カスタム: https://kobayashi-dental-kasai.com/ (DNS設定後)

## 注意事項
- 全ファイルをリポジトリルートに配置
- CNAME ファイルを削除しないこと
- 404.html は SPA 動作に必要
