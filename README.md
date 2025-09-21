# 小林歯科クリニック Web サイト

Vue (Vite) + Python (FastAPI) 構成のシンプルで洗練された Apple 風デザインの雛形です。

## 仕様
- フロントエンド: Vue 3 + Vite
- バックエンド: FastAPI + Uvicorn
- デザイン方針: 余白・タイポグラフィ中心、低彩度、繊細なアニメーション
- Contact/予約 API のダミー保存（JSON 追記）

## セットアップ

### 1) Python API の起動
```powershell
# ルートへ移動
cd "c:\Users\tsuba\OneDrive\ドキュメント\dev\kobayashi_dental_clinic"

# (任意) 仮想環境推奨
# py -m venv .venv
# .venv\\Scripts\\Activate.ps1

# 依存インストール
pip install -r backend/requirements.txt

# 起動 (http://127.0.0.1:8000)
python -m uvicorn backend.app:app --reload --port 8000
```

### 2) フロントエンドの起動
```powershell
cd "c:\Users\tsuba\OneDrive\ドキュメント\dev\kobayashi_dental_clinic\frontend"

# 依存インストール
npm install

# 開発サーバ起動 (http://localhost:5173)
npm run dev
```

バックエンド CORS は `http://localhost:5173` を許可済みです。

## ビルド
```powershell
cd frontend
npm run build
```
`dist/` が生成されます。静的ホスティングの際は、API は別ドメインで運用してください。

## API 概要
- GET `/api/clinic-info` クリニック情報
- POST `/api/contact` お問い合わせ保存
- POST `/api/appointment` 予約保存

保存先: `backend/data/contacts.json`, `backend/data/appointments.json`

## 注意
- Apple のデザインやアセットをコピーせず、ミニマルな設計思想のみ参考にしています。
