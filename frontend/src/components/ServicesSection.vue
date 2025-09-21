<template>
  <section id="services" class="section">
    <div class="container">
      <h2 class="h2">診療内容</h2>
      <p class="p" style="margin-bottom:24px">
  {{ services?.length ? services.join('、') : 'むし歯治療、予防・審美歯科、矯正、小児、補綴・口腔外科 など' }}
      </p>
      <p class="p" style="margin-bottom:16px">保険診療を中心に、日々の診療で必要な治療を丁寧にご提供します。自費診療にも対応し、最適な選択肢をご一緒に検討します。</p>
  <div class="grid">
        <article class="card item">
          <h3>予防・審美歯科</h3>
          <p>定期検診・クリーニングに加え、ホワイトニングなどの審美ケアにも対応します。</p>
          <router-link class="link" to="/services/preventive">詳細を見る</router-link>
        </article>
        <article class="card item">
          <h3>むし歯・根管治療</h3>
          <p>痛みを抑えた丁寧な治療を心がけています。</p>
          <router-link class="link" to="/services/general">詳細を見る</router-link>
        </article>
        <article class="card item">
          <h3>矯正・小児矯正</h3>
          <p>目立ちにくい装置にも対応しています。</p>
          <router-link class="link" to="/services/orthodontics">詳細を見る</router-link>
        </article>
        <article class="card item">
          <h3>補綴・口腔外科</h3>
          <p>入れ歯・ブリッジなどの補綴治療と、親知らず等の外科処置に対応します。</p>
          <router-link class="link" to="/services/oral-surgery">詳細を見る</router-link>
        </article>
      </div>
    </div>
  </section>
</template>
<script setup lang="ts">
defineProps<{ services?: string[] }>()
</script>
<style scoped>
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.item{padding:22px;min-height:140px}
.item h3{margin:0 0 8px}
@media (max-width: 900px){
  .grid{grid-template-columns:1fr 1fr}
}
@media (max-width: 600px){
  .grid{grid-template-columns:1fr}
}
</style>
<style>
#services{scroll-margin-top:90px}
</style>
