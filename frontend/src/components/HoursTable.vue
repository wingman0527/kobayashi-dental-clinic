<template>
  <div class="hoursTable card">
    <div class="scroll">
      <table class="tbl">
        <thead>
          <tr>
            <th></th>
            <th>月</th>
            <th>火</th>
            <th>水</th>
            <th>木</th>
            <th>金</th>
            <th>土</th>
            <th>日</th>
            <th>祝</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th>9:30–13:00</th>
            <td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>－</td><td>－</td>
          </tr>
          <tr>
            <th>14:30–18:00</th>
            <td>●</td><td>－</td><td>－</td><td>●</td><td>－</td><td>－</td><td>－</td><td>－</td>
          </tr>
          <tr>
            <th>14:30–19:30</th>
            <td>－</td><td>●</td><td>●</td><td>－</td><td>●</td><td>－</td><td>－</td><td>－</td>
          </tr>
          <tr>
            <th>14:30–16:00</th>
            <td>－</td><td>－</td><td>－</td><td>－</td><td>－</td><td>●</td><td>－</td><td>－</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="p note">9:30～13:00 14:30～19:30 月・木曜18:00まで 土曜16:00まで／予約制／科により異なる／臨時休診あり</p>
  </div>
</template>
<script setup lang="ts">
// 静的な診療時間表（Doctors File 掲載内容を反映）
</script>
<style scoped>
.hoursTable{padding:8px}
.scroll{overflow-x:auto}
.tbl{width:100%;border-collapse:separate;border-spacing:0;min-width:560px;font-size:14px}
th,td{padding:6px 8px;border-bottom:1px solid var(--border);text-align:center}
thead th{font-weight:600;color:#111114cc}
tbody th{text-align:left;white-space:nowrap;color:#111114cc}
tr:last-child td, tr:last-child th{border-bottom:none}
.note{margin:8px 4px;color:var(--muted);font-size:12px}

/* スマートフォン対応 */
@media (max-width: 768px) {
  .tbl {
    font-size: 12px;
    min-width: 480px;
  }
  
  th, td {
    padding: 4px 6px;
  }
  
  tbody th {
    font-size: 11px;
  }
  
  .note {
    font-size: 11px;
    line-height: 1.4;
  }
  
  .hoursTable {
    padding: 6px;
  }
}

@media (max-width: 480px) {
  .tbl {
    font-size: 11px;
    min-width: 420px;
  }
  
  th, td {
    padding: 3px 4px;
  }
  
  tbody th {
    font-size: 10px;
  }
}
</style>
