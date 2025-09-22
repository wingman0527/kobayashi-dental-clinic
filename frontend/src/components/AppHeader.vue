<template>
  <header class="nav card">
    <div class="container inner">
      <router-link class="brand" to="/">
        <img class="brand-icon" src="/favicon.svg" alt="" aria-hidden="true" />
        <span class="brand-text">{{ clinicName }}</span>
        <span class="tag">いつもの治療を、ていねいに。</span>
      </router-link>
      <button class="menu-toggle" @click="toggleMenu" :class="{ active: menuOpen }">
        <span></span>
        <span></span>
        <span></span>
      </button>
      <nav class="links" :class="{ open: menuOpen }">
        <router-link to="/" @click="closeMenu">ホーム</router-link>
        <router-link :to="{ path: '/', hash: '#services' }" @click="closeMenu">診療内容</router-link>
        <router-link to="/faq" @click="closeMenu">よくある質問</router-link>
        <router-link :to="{ path: '/', hash: '#access' }" @click="closeMenu">アクセス</router-link>
        <router-link :to="{ path: '/', hash: '#contact' }" @click="closeMenu">お問い合わせ</router-link>
      </nav>
    </div>
  </header>
</template>
<script setup lang="ts">
import { ref } from 'vue'

defineProps<{ clinicName: string }>()

const menuOpen = ref(false)

function toggleMenu() {
  menuOpen.value = !menuOpen.value
}

function closeMenu() {
  menuOpen.value = false
}
</script>
<style scoped>
.nav{
  position:fixed;top:12px;left:0;right:0;z-index:20;padding:10px 0;
}
.inner{display:flex;align-items:center;justify-content:space-between;gap:16px}
.brand{display:flex;align-items:center;gap:8px;font-weight:600;letter-spacing:.2px;text-decoration:none;color:var(--fg)}
.brand-icon{width:18px;height:18px;display:block}
.brand-text{white-space:nowrap}
.tag{color:var(--muted);font-size:12.5px;margin-left:4px;white-space:nowrap}
.menu-toggle{display:none}
.links{display:flex;gap:20px}
.links a{color:#111114cc;text-decoration:none;white-space:nowrap}
.links a:hover{color:var(--fg)}

/* スマートフォン対応 */
@media (max-width: 768px) {
  .nav {
    top: 8px;
    padding: 8px 0;
  }
  
  .brand {
    flex-direction: column;
    align-items: flex-start;
    gap: 2px;
  }
  
  .brand-text {
    font-size: 14px;
  }
  
  .tag {
    font-size: 10px;
    margin-left: 0;
    white-space: nowrap;
  }
  
  .mobile-br {
    display: block;
  }
  
  .menu-toggle {
    display: flex;
    flex-direction: column;
    gap: 4px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
    width: 40px;
    height: 32px;
  }
  
  .menu-toggle span {
    width: 24px;
    height: 2px;
    background: var(--fg);
    transition: all 0.3s ease;
    transform-origin: center;
  }
  
  .menu-toggle.active span:nth-child(1) {
    transform: rotate(45deg) translate(6px, 6px);
  }
  
  .menu-toggle.active span:nth-child(2) {
    opacity: 0;
  }
  
  .menu-toggle.active span:nth-child(3) {
    transform: rotate(-45deg) translate(6px, -6px);
  }
  
  .links {
    position: fixed;
    top: 70px;
    left: 12px;
    right: 12px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: saturate(1.2) blur(20px);
    border-radius: 12px;
    border: 1px solid var(--border);
    flex-direction: column;
    gap: 0;
    padding: 16px 0;
    opacity: 0;
    visibility: hidden;
    transform: translateY(-10px);
    transition: all 0.3s ease;
  }
  
  .links.open {
    opacity: 1;
    visibility: visible;
    transform: translateY(0);
  }
  
  .links a {
    padding: 12px 20px;
    display: block;
    color: var(--fg);
    font-size: 15px;
  }
  
  .links a:hover {
    background: rgba(0, 0, 0, 0.05);
  }
}

@media (max-width: 480px) {
  .brand-text {
    font-size: 13px;
  }
  
  .tag {
    font-size: 9px;
  }
  
  .links {
    top: 60px;
  }
}
</style>
