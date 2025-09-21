<template>
  <section class="section">
    <div class="container">
      <h1 class="h2">一般歯科（保険診療中心）</h1>
      <p class="p">むし歯・歯周病の治療や詰め物・被せ物の調整など、日々の診療で必要なケアを丁寧に行います。</p>
      <figure class="card" style="overflow:hidden;margin:16px 0">
        <img :src="photo" alt="院内写真（一般歯科）" loading="lazy" style="width:100%;display:block;object-fit:cover;max-height:360px" />
      </figure>
  <router-link :to="{ path: '/', hash: '#services' }" class="link">診療内容に戻る</router-link>
      <h2 class="h2" style="margin-top:28px">治療メニュー</h2>
      <TreatmentMenu :items="menu" />
    </div>
  </section>
</template>
<script setup lang="ts">
import TreatmentMenu, { type TreatmentRow } from '../../components/TreatmentMenu.vue'
import photo from '../../clinic_photo/image4.jpeg'

const menu: TreatmentRow[] = [
  { type: 'むし歯治療', description: 'レジン充填（小～中）', visits: '2回', price: '数千円台～', coverage: '保険' },
  { type: 'むし歯治療', description: 'インレー（詰め物）', visits: '2回', price: '数千円台～／自費は数万円～', coverage: '保険/自費', note: '材料・部位により異なる' },
  { type: '根管治療', description: '前歯～臼歯の根の治療', visits: '2～数回', price: '数千円台～', coverage: '保険' },
  { type: '被せ物', description: 'クラウン（金属・セラミック等）', visits: '2～3回', price: '数千円台～／自費は数万円～', coverage: '保険/自費', note: '材質・部位により異なる' },
  { type: '歯周治療', description: 'スケーリング/ルートプレーニング', visits: '1～数回', price: '数千円台～', coverage: '保険' },
]
</script>
