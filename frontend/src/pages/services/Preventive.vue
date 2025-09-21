<template>
  <section class="section">
    <div class="container">
  <h1 class="h2">予防・審美歯科</h1>
      <p class="p">定期検診とクリーニング（スケーリング/PMTC）を中心に、むし歯や歯周病を「治す前に防ぐ」ためのケアをご提供します。日常のケアアドバイスも行います。</p>
      <figure class="card" style="overflow:hidden;margin:16px 0">
  <img :src="photo" alt="予防・審美歯科のイメージ" loading="lazy" style="width:100%;display:block;object-fit:cover;max-height:360px" />
      </figure>
      <router-link :to="{ path: '/', hash: '#services' }" class="link">診療内容に戻る</router-link>
  <h2 class="h2" style="margin-top:28px">予防・審美メニュー</h2>
      <TreatmentMenu :items="menu" />
    </div>
  </section>
</template>
<script setup lang="ts">
import TreatmentMenu, { type TreatmentRow } from '../../components/TreatmentMenu.vue'
// 画像はURL解決で安定読込
const photo = new URL('../../clinic_photo/pexels-rdne-10566161.jpg', import.meta.url).href
const menu: TreatmentRow[] = [
  { type: '定期検診', description: '歯と歯ぐきのチェック、レントゲン/口腔内写真（必要に応じて）', visits: '1回', price: '数百～数千円', coverage: '保険' },
  { type: 'スケーリング', description: '歯石除去（歯周基本治療）', visits: '1～数回', price: '数百～数千円', coverage: '保険' },
  { type: 'PMTC', description: '専用機器でのクリーニング・着色除去', visits: '1回', price: '数千円台～', coverage: '自費/保険', note: '適応により異なる' },
  { type: 'メインテナンス', description: '歯周安定後の定期的な清掃・評価', visits: '3～6ヶ月毎', price: '数百～数千円', coverage: '保険' },
  { type: 'ブラッシング指導', description: '個別リスクに合わせた清掃指導と道具の選び方', visits: '1回', price: '数百円～', coverage: '保険' },
  { type: 'フッ素塗布', description: '再石灰化を促す予防処置（年齢・リスクに応じて）', visits: '1回', price: '数百～数千円', coverage: '保険/自費' },
  { type: 'ホワイトニング', description: '薬剤と専用トレーによる歯の漂白', visits: '2～3回', price: '数万円～', coverage: '自費' },
]
</script>
