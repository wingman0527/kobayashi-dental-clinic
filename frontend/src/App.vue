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
      motto: 'いつもの治療を、ていねいに。',
      address: '東京都江戸川区西葛西6-16-4 エスペランス3F',
      phone: '03-3878-4182',
      access: 'JR京葉線/東京メトロ東西線 西葛西駅南口 徒歩1分',
      director: '小林 太郎',
      hours: {
        mon_fri: '9:00-12:30 / 14:30-19:00',
        sat: '9:00-12:30 / 14:30-17:00',
        sun_holiday: '休診'
      },
      services: [
        { name: '一般歯科', path: '/services/general' },
        { name: '予防・審美歯科', path: '/services/preventive' },
        { name: '矯正歯科', path: '/services/orthodontics' },
        { name: '小児歯科', path: '/services/pediatric' },
        { name: '補綴・口腔外科', path: '/services/oral-surgery' }
      ]
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
