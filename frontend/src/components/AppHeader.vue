<template>
  <header class="nav card">
    <div class="container inner">
  <router-link class="brand" to="/">
    <img class="brand-icon" src="/favicon.svg" alt="" aria-hidden="true" />
    {{ clinicName }}
  </router-link>
  <span class="tag">いつもの治療を、ていねいに。</span>
      <nav class="links">
  <router-link to="/">ホーム</router-link>
  <router-link :to="{ path: '/', hash: '#services' }">診療内容</router-link>
  <router-link to="/faq">よくある質問</router-link>
  <router-link :to="{ path: '/', hash: '#access' }">アクセス</router-link>
  <router-link :to="{ path: '/', hash: '#contact' }">お問い合わせ</router-link>
      </nav>
    </div>
  </header>
</template>
<script setup lang="ts">
defineProps<{ clinicName: string }>()
</script>
<style scoped>
.nav{
  position:fixed;top:12px;left:0;right:0;z-index:20;padding:10px 0;
}
.inner{display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{display:flex;align-items:center;gap:8px;font-weight:600;letter-spacing:.2px;text-decoration:none;color:var(--fg)}
.brand-icon{width:18px;height:18px;display:block}
.tag{color:var(--muted);font-size:12.5px}
.links{display:flex;gap:20px}
.links a{color:#111114cc;text-decoration:none}
.links a:hover{color:var(--fg)}
</style>
