<template>
  <div class="menu card">
    <table class="tbl">
      <thead>
        <tr>
          <th>治療種別</th>
          <th>治療内容</th>
          <th>通院回数（目安）</th>
          <th>料金</th>
          <th>保険/自費</th>
          <th>備考</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(row, i) in items" :key="i">
          <td :data-th="'治療種別'">{{ row.type }}</td>
          <td :data-th="'治療内容'">{{ row.description }}</td>
          <td :data-th="'通院回数（目安）'">{{ row.visits || '-' }}</td>
          <td :data-th="'料金'">{{ row.price || '-' }}</td>
          <td :data-th="'保険/自費'">{{ row.coverage || '-' }}</td>
          <td :data-th="'備考'">{{ row.note || '-' }}</td>
        </tr>
        <tr v-if="!items || !items.length">
          <td colspan="6" style="text-align:center;color:var(--muted)">準備中です</td>
        </tr>
      </tbody>
    </table>
    <p class="p note">※ 掲載の料金は目安です。症状・材料・保険点数改定等により変動します。正確な費用は診察時にご案内します。</p>
  </div>
</template>
<script setup lang="ts">
export interface TreatmentRow {
  type: string
  description: string
  visits?: string
  price?: string
  coverage?: '保険' | '自費' | string
  note?: string
}

defineProps<{ items: TreatmentRow[] }>()
</script>
<style scoped>
.menu{padding:12px}
.tbl{width:100%;border-collapse:separate;border-spacing:0}
th,td{padding:12px 12px;vertical-align:top;border-bottom:1px solid var(--border)}
th{font-weight:600;text-align:left;color:#111114cc}
tr:last-child td{border-bottom:none}
.note{margin:10px 4px;color:var(--muted);font-size:12.5px}
@media (max-width: 760px){
  .tbl thead{display:none}
  .tbl tr{display:block;border-bottom:1px solid var(--border)}
  .tbl td{display:flex;gap:8px;padding:10px 2px;border:none}
  .tbl td::before{content:attr(data-th);min-width:110px;color:#6e6e73}
}
</style>
