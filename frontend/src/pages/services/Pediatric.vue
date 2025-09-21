<template>
  <section class="section">
    <div class="container">
  <h1 class="h2">小児歯科</h1>
  <p class="p">成長段階に応じた予防と治療で、将来の歯並び・噛み合わせも見据えたケアを行います。まずは歯科医院に慣れることから。</p>
      <figure class="card" style="overflow:hidden;margin:16px 0">
  <img src="https://images.pexels.com/photos/5327653/pexels-photo-5327653.jpeg?auto=compress&cs=tinysrgb&w=1600" alt="小児歯科のイメージ" style="width:100%;display:block;object-fit:cover;max-height:360px" />
  <figcaption class="p" style="padding:8px 12px;color:#6e6e73">Photo: Pexels</figcaption>
      </figure>
  <router-link :to="{ path: '/', hash: '#services' }" class="link">診療内容に戻る</router-link>
      <h2 class="h2" style="margin-top:28px">治療メニュー</h2>
      <TreatmentMenu :items="menu" />
    </div>
  </section>
</template>
<script setup lang="ts">
import TreatmentMenu, { type TreatmentRow } from '../../components/TreatmentMenu.vue'

const menu: TreatmentRow[] = [
  { type: 'フッ素塗布', description: 'う蝕予防のためのフッ素塗布', visits: '1回', price: '数百～数千円', coverage: '保険/自費' },
  { type: 'シーラント', description: '奥歯の溝を樹脂でコーティング', visits: '1回', price: '数百～数千円', coverage: '保険/自費' },
  { type: 'むし歯治療', description: '小児のレジン充填', visits: '1回', price: '数千円台～', coverage: '保険' },
]
</script>
