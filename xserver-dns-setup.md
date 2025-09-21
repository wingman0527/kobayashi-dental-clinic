# Xserver DNS設定手順（既存WordPressサイト置き換え）

## 事前確認
現在のkobayashi-dental-kasai.comでWordPressサイトが動作中です。
GitHub Pagesに切り替える前に、必要に応じて既存サイトのバックアップを取得してください。

## 1. Xserverサーバーパネルにログイン
https://www.xserver.ne.jp/login_server.php

## 2. 既存WordPressサイトの無効化
### オプション1: ファイル移動（推奨）
1. ファイルマネージャーにログイン
2. `public_html` フォルダを開く
3. 既存のWordPressファイルを `backup_wordpress` などの名前のフォルダに移動
4. これにより既存サイトが一時的に無効になります

### オプション2: .htaccessで一時無効化
1. ファイルマネージャーで `public_html/.htaccess` を編集
2. 最上部に以下を追加：
```
# Temporary redirect to maintenance page
RewriteEngine On
RewriteCond %{REQUEST_URI} !^/maintenance.html$
RewriteRule ^(.*)$ /maintenance.html [R=302,L]
```
3. 簡単なメンテナンス用HTMLファイル（maintenance.html）を作成

## 3. DNSレコード設定
1. サーバーパネルで「DNSレコード設定」をクリック
2. 対象ドメイン「kobayashi-dental-kasai.com」を選択
3. 「DNSレコード追加」タブをクリック

## 4. 必要なDNSレコードを追加・変更

⚠️ **重要**: 既存のAレコードを削除してから新しいレコードを追加してください

### 既存レコードの削除
1. 現在のAレコード（Xserverのサーバーを指すもの）を削除
2. 既存のCNAMEレコードがあれば削除

### Aレコード（@用）
- ホスト名: @ (空白)
- 種別: A
- 内容: 185.199.108.153
- 優先度: 0

### Aレコード（@用）追加分
- ホスト名: @ (空白)
- 種別: A
- 内容: 185.199.109.153
- 優先度: 0

### Aレコード（@用）追加分
- ホスト名: @ (空白)
- 種別: A
- 内容: 185.199.110.153
- 優先度: 0

### Aレコード（@用）追加分
- ホスト名: @ (空白)
- 種別: A
- 内容: 185.199.111.153
- 優先度: 0

### CNAMEレコード（www用）
- ホスト名: www
- 種別: CNAME
- 内容: wingman0527.github.io
- 優先度: 0

## 5. 既存のレコードを確認・削除
⚠️ **この手順が最も重要です**
- 現在XserverのIPアドレスを指している既存のAレコードを削除
- 既存のCNAMEレコードがあれば削除
- MXレコード（メール用）は残しておいてください

## 6. 段階的な切り替え手順（推奨）
1. **準備段階**: 既存WordPressサイトをバックアップ
2. **DNS変更**: 上記のGitHub Pages用DNSレコードに変更
3. **確認**: DNS反映後、新しいサイトが正常に動作することを確認
4. **完全移行**: 問題なければ既存WordPressファイルを削除

## 7. ロールバック手順（問題が発生した場合）
問題が発生した場合、以下で元に戻せます：
1. DNSレコードを元のXserverのAレコードに戻す
2. WordPressファイルを `public_html` に戻す
3. DNS反映を待つ（数時間）

## 8. 設定完了後
- DNS反映には最大48時間かかる場合があります
- 通常は数時間で反映されます
- 反映状況の確認: https://www.whatsmydns.net/ でkobayashi-dental-kasai.comを検索

## 9. 注意事項
- **メール設定**: 既存のメール設定（MXレコード）は影響を受けません
- **SEO**: 検索エンジンのインデックスには時間がかかります
- **SSL証明書**: GitHub Pagesが自動でHTTPS証明書を発行します

## GitHub側の設定
GitHub Pages設定で「kobayashi-dental-kasai.com」を設定済みです。
CNAMEファイルもリポジトリに配置済みです。
