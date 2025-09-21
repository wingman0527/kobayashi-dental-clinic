<template>
  <div class="page">
    <AppHeader :clinicName="clinic?.name || '小林歯科'" />
    <main>
      <router-view :clinic="clinic" />
    </main>
    <AppFooter />
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { api } from './lib/api'
import AppHeader from './components/AppHeader.vue'
import { router } from './router'
import HomePage from './pages/HomePage.vue'
import AppFooter from './components/AppFooter.vue'

const clinic = ref<any | null>(null)

onMounted(async () => {
  try {
    const { data } = await api.get('/api/clinic-info')
    clinic.value = data
  } catch (e) {
    // API が落ちていても UI は表示
    clinic.value = {
      name: '小林歯科クリニック',
      tagline: 'あなたの笑顔を、美しく健やかに',
    }
  }
})
</script>

<style scoped>
.page {
  background: var(--bg);
  color: var(--fg);
}
main { padding-top: 64px; }
</style>
