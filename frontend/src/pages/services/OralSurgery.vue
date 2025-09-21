<template>
  <section class="section">
    <div class="container">
  <h1 class="h2">補綴・口腔外科</h1>
  <p class="p">入れ歯・ブリッジなどの補綴治療に加え、親知らずの抜歯や小手術などの口腔外科処置にも対応します。安全性と咬み合わせのバランスに配慮して進めます。</p>
      <figure class="card" style="overflow:hidden;margin:16px 0">
  <img :src="photo" alt="補綴・口腔外科のイメージ" loading="lazy" style="width:100%;display:block;object-fit:cover;max-height:360px" />
      </figure>
  <router-link :to="{ path: '/', hash: '#services' }" class="link">診療内容に戻る</router-link>
      <h2 class="h2" style="margin-top:28px">治療メニュー</h2>
      <TreatmentMenu :items="menu" />
    </div>
  </section>
</template>
<script setup lang="ts">
import TreatmentMenu, { type TreatmentRow } from '../../components/TreatmentMenu.vue'
const photo = new URL('../../clinic_photo/pexels-olly-3779693_2.jpg', import.meta.url).href

const menu: TreatmentRow[] = [
  { type: '入れ歯（部分・総義歯）', description: '型取り〜装着、使用感の調整', visits: '数回', price: '数千円台～／自費は数万円～', coverage: '保険/自費', note: '設計・材料により異なる' },
  { type: 'ブリッジ', description: '欠損部を両隣の歯で補う固定式の補綴', visits: '2～3回', price: '数千円台～／自費は数万円～', coverage: '保険/自費', note: '部位・材質により異なる' },
  { type: 'クラウン（被せ物）再製・再装着', description: '外れた冠の再装着や再製作', visits: '1～2回', price: '数千円台～／自費は数万円～', coverage: '保険/自費' },
  { type: '義歯調整・修理', description: '痛み・外れやすさの調整、破損修理', visits: '1～数回', price: '数千円台～', coverage: '保険/自費' },
  { type: '親知らずの抜歯', description: '埋伏・水平埋伏など難易度に応じて対応', visits: '1回', price: '数千円台～', coverage: '保険/自費' },
  { type: '小手術', description: '小帯切除・嚢胞摘出など', visits: '1回', price: '数千～数万円', coverage: '保険/自費' },
]
</script>
