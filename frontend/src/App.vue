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
      name: '小林歯科',
      tagline: 'あなたの笑顔を、美しく健やかに',
      motto: 'いつもの治療を、ていねいに。',
      address: '〒134-0083 中葛西6-2-1',
      phone: '03-3687-4181',
      access: '地下鉄東西線 西葛西駅から 都バス なぎさニュータウン行『西葛西6丁目』下車 徒歩9分 / JR京葉線 葛西臨海公園駅から 都バス 西葛西駅行『中葛西7丁目』下車 徒歩3分',
      director: '小林 一公',
      hours: {
        mon_fri: '09:30 - 13:00 / 14:30 - 19:30',
        sat: '09:30 - 13:00 / 14:30 - 16:30',
        sun_holiday: '休診（日・祝）'
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
