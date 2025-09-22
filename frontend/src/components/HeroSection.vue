<template>
  <section class="section hero">
    <div class="container content">
      <h1 class="h1 gradient">
        <span class="motto-desktop">{{ motto || 'いつもの治療を、ていねいに。' }}</span>
        <span class="motto-mobile">いつもの治療を、<br>ていねいに。</span>
      </h1>
      <p class="p">毎日の生活に寄り添う、丁寧で確かな治療。わかりやすいご説明と通いやすい体験を大切にしています。</p>
      <div class="cta">
        <a href="#contact" class="button">予約・お問い合わせ</a>
        <a href="#services" class="button ghost">診療内容を見る</a>
      </div>
    </div>
  </section>
</template>
<script setup lang="ts">
defineProps<{ tagline?: string; motto?: string }>()
</script>
<style scoped>
.hero{padding-top:120px}
.content{text-align:center}
.gradient{background:linear-gradient(90deg,#111,#555);-webkit-background-clip:text;background-clip:text;color:transparent}
.cta{margin-top:28px;display:flex;gap:16px;justify-content:center;align-items:center;flex-wrap:wrap}

/* デスクトップとモバイルでの表示切り替え */
.motto-mobile {
  display: none;
}

@media (max-width: 768px) {
  .motto-desktop {
    display: none;
  }
  
  .motto-mobile {
    display: inline;
  }
  
  .hero {
    padding-top: 80px;
  }
}
</style>
