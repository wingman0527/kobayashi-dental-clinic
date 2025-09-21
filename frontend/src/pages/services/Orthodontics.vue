<template>
  <section class="section">
    <div class="container">
  <h1 class="h2">矯正歯科</h1>
  <p class="p">不正咬合の改善を目的に、噛み合わせと顔貌の調和を考慮した治療計画をご提案します。目立ちにくい装置にも対応します。</p>
      <figure class="card" style="overflow:hidden;margin:16px 0">
        <img :src="photo" alt="矯正歯科のイメージ" loading="lazy" style="width:100%;display:block;object-fit:cover;max-height:360px" />
      </figure>
  <router-link :to="{ path: '/', hash: '#services' }" class="link">診療内容に戻る</router-link>
      <h2 class="h2" style="margin-top:28px">治療メニュー</h2>
      <TreatmentMenu :items="menu" />
    </div>
  </section>
</template>
<script setup lang="ts">
import TreatmentMenu, { type TreatmentRow } from '../../components/TreatmentMenu.vue'
import photo from '../../clinic_photo/pexels-cottonbro-6502303_2.jpg'

const menu: TreatmentRow[] = [
  { type: '矯正相談', description: 'カウンセリング・検査のご案内', visits: '1回', price: '無料/数千円台', coverage: '自費', note: '医院規定による' },
  { type: '小児矯正', description: '成長期の顎の誘導・拡大（I期治療）', visits: '数ヶ月～', price: '数十万円～', coverage: '自費' },
  { type: '成人矯正', description: 'ワイヤー矯正/目立ちにくい装置（II期治療）', visits: '1～2年', price: '数十万円～', coverage: '自費' },
  { type: 'マウスピース矯正', description: '透明なマウスピース型装置による矯正', visits: '数ヶ月～2年', price: '数十万円～', coverage: '自費', note: '適応症例に限る' },
  { type: '保定', description: '歯並びを維持する装置', visits: '数回', price: '数万円～', coverage: '自費' },
]
</script>
