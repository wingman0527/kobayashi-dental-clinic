<template>
  <section class="section">
    <div class="container">
      <h1 class="h2">料金の目安</h1>
      <p class="p">保険診療は全国一律の点数制（1点=10円）に基づき計算されます。以下は代表的な処置の目安です。症状・使用材料・改定により変動します。</p>
      <div class="card" style="padding:16px;margin:16px 0">
        <ul>
          <li class="p">初診料（保険）: 約 2,000〜3,000円（検査/処置内容で変動）</li>
          <li class="p">再診料（保険）: 約 1,000〜2,000円（処置内容で変動）</li>
          <li class="p">レジン充填（小〜中）: 数百〜数千点（例: 約 1,000〜3,000円台）</li>
          <li class="p">スケーリング: 数百点（例: 約 1,000円台〜）</li>
          <li class="p">根管治療: 数千点（部位/回数により）</li>
        </ul>
        <p class="p" style="margin-top:8px;color:var(--muted)">※ 実際の点数は口腔内の状態、画像検査、処置の範囲で増減します。詳細は来院時にご案内いたします。</p>
      </div>

      <h2 class="h2">自費診療の目安</h2>
      <div class="card" style="padding:16px;margin:16px 0">
        <ul>
          <li class="p">ホワイトニング: 数万円〜</li>
          <li class="p">セラミック修復: 数万円〜十数万円</li>
          <li class="p">成人矯正: 数十万円〜</li>
        </ul>
        <p class="p" style="margin-top:8px;color:var(--muted)">※ 自費診療は材料・方法で幅があります。無料/有料カウンセリングの有無はお問い合わせください。</p>
      </div>

      <router-link class="link" to="/">トップへ戻る</router-link>
    </div>
  </section>
</template>
<script setup lang="ts"></script>
