<template>
  <section class="section">
    <div class="container">
      <h1 class="h2">診療内容</h1>
      <p class="p">身近な治療を、保険診療で。必要に応じて自費診療もご案内します。</p>
      <ul class="list">
        <li><router-link to="/services/general">一般歯科</router-link></li>
        <li><router-link to="/services/orthodontics">矯正歯科</router-link></li>
        <li><router-link to="/services/pediatric">小児歯科</router-link></li>
  <li><router-link to="/services/oral-surgery">補綴・口腔外科</router-link></li>
      </ul>
    </div>
  </section>
</template>
<script setup lang="ts"></script>
<style scoped>
.list{margin-top:12px}
.list a{text-decoration:none;border-bottom:1px solid #0002;color:var(--fg)}
</style>
