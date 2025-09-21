<template>
  <section id="access" class="section">
    <div class="container">
  <h2 class="h2">アクセス</h2>
      <div class="card wrap">
        <div class="info">
          <p class="p"><strong>住所:</strong> {{ address || '東京都〇〇区〇〇 1-2-3' }}</p>
          <p class="p"><strong>電話:</strong> <a :href="`tel:${phone || ''}`">{{ phone || '03-1234-5678' }}</a></p>
          <p v-if="director" class="p"><strong>院長:</strong> {{ director }}</p>
          <div class="hours">
            <p class="p"><strong>診療時間:</strong></p>
            <HoursTable />
          </div>
          <p v-if="access" class="p" style="margin-top:8px"><strong>交通:</strong> {{ access }}</p>
        </div>
        <div class="map">
          <iframe
            v-if="mapSrc"
            class="mapFrame card"
            :src="mapSrc"
            style="border:0"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            allowfullscreen
          ></iframe>
          <div v-else class="mapPh card">住所が未設定です。地図は後で追加できます。</div>
        </div>
      </div>
    </div>
  </section>
</template>
<script setup lang="ts">
import { computed, toRefs } from 'vue'
import HoursTable from './HoursTable.vue'

interface Hours { mon_fri?: string; sat?: string; sun_holiday?: string }
const props = defineProps<{ address?: string; phone?: string; hours?: Hours; access?: string; director?: string }>()
const { address, phone, hours, access, director } = toRefs(props)

// 住所からGoogleマップの埋め込みURLを生成（APIキー不要の簡易埋め込み）
const mapSrc = computed(() => {
  if (!address.value) return ''
  const q = encodeURIComponent(address.value)
  return `https://www.google.com/maps?&q=${q}&output=embed`
})
</script>
<style scoped>
.wrap{display:grid;grid-template-columns:1.1fr 1fr;gap:16px;padding:22px}
.info ul{margin:8px 0 0 0;padding-left:20px;color:var(--muted)}
.map{height:100%}
.mapPh{height:100%;min-height:260px;display:flex;align-items:center;justify-content:center;border-radius:12px;background:#f0f0f3}
.mapFrame{width:100%;height:100%;min-height:260px;border-radius:12px}
@media (max-width: 900px){
  .wrap{grid-template-columns:1fr}
}
</style>
<style>
#access{scroll-margin-top:90px}
</style>
