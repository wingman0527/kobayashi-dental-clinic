<template>
  <section id="contact" class="section">
    <div class="container">
  <h2 class="h2">予約・お問い合わせ</h2>
  <p class="p" style="margin-bottom:16px">はじめての方もご安心ください。保険診療を中心に、わかりやすくご説明します。</p>
      <div class="forms">
        <form class="card form" @submit.prevent="submitContact">
          <h3>お問い合わせ</h3>
          <!-- Honeypot (spam bot 対策) -->
          <label style="position:absolute;left:-9999px;top:auto;width:1px;height:1px;overflow:hidden">_gotcha<input v-model="contact.gotcha" tabindex="-1" autocomplete="off" /></label>
          <label>お名前<input v-model="contact.name" required /></label>
          <label>メール<input v-model="contact.email" type="email" required /></label>
          <label>内容<textarea v-model="contact.message" rows="4" required /></label>
          <button class="button" :disabled="loadingContact || doneContact">{{ doneContact ? '送信済み' : (loadingContact ? '送信中…' : '送信') }}</button>
          <Transition name="fade"><p v-if="doneContact" class="p" style="color:var(--accent, #0a7)">送信しました。ありがとうございます。</p></Transition>
          <Transition name="fade"><p v-if="errorContact" class="p" style="color:#c0392b">送信できませんでした。時間をおいて再度お試しください。</p></Transition>
          <p class="p note" style="margin-top:10px;font-size:12px">このフォームは Formspree を利用しています。送信によりプライバシーポリシーに同意したものとみなされます。</p>
        </form>
  <form class="card form coming-soon" @submit.prevent="submitAppt" aria-disabled="true" @click="toggleOverlay">
          <h3>予約</h3>
          <label>お名前<input v-model="appt.name" :disabled="bookingDisabled" required /></label>
          <label>メール<input v-model="appt.email" type="email" :disabled="bookingDisabled" required /></label>
          <label>電話<input v-model="appt.phone" :disabled="bookingDisabled" /></label>
          <div class="row">
            <label>日付<input v-model="appt.date" type="date" :disabled="bookingDisabled" required /></label>
            <label>時間<input v-model="appt.time" type="time" :disabled="bookingDisabled" required /></label>
          </div>
          <label>備考<textarea v-model="appt.note" rows="3" :disabled="bookingDisabled" /></label>
          <button class="button" :disabled="true" title="Coming Soon">予約する</button>
          <div class="soon-overlay" :class="{ active: overlayActive }">
            <div class="overlay-inner">
              <span class="soon-label">COMING SOON</span>
              <p class="overlay-msg">WEB予約は準備中です。お電話でのご予約は
                <a :href="`tel:${clinicPhone || '03-1234-5678'}`">{{ clinicPhone || '03-1234-5678' }}</a>
                へお願いいたします。</p>
            </div>
          </div>
        </form>
      </div>
    </div>
  </section>
</template>
<script setup lang="ts">
import { reactive, ref } from 'vue'
// import { api } from '../lib/api'  // Formspree利用に切替のため未使用
// 親（HomePage）から電話番号を受け取って表示
const { phone: clinicPhone } = defineProps<{ phone?: string }>()

const loadingContact = ref(false)
const doneContact = ref(false)
const errorContact = ref(false)
const loadingAppt = ref(false)
const doneAppt = ref(false)
const bookingDisabled = true
const overlayActive = ref(false)

const contact = reactive({ name: '', email: '', message: '', gotcha: '' })
const appt = reactive({ name: '', email: '', phone: '', date: '', time: '', note: '' })

function toggleOverlay() {
  overlayActive.value = !overlayActive.value
}

const FORMSPREE_ENDPOINT = (import.meta as any).env?.VITE_FORMSPREE_ENDPOINT || 'https://formspree.io/f/xxxxxxxx'; // ← xxxxxxxx を実フォームIDに変更

async function submitContact(){
  if (contact.gotcha) return // bot判定
  if (doneContact.value) return
  loadingContact.value = true
  errorContact.value = false
  doneContact.value = false
  try {
    const res = await fetch(FORMSPREE_ENDPOINT, {
      method: 'POST',
      headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: contact.name, email: contact.email, message: contact.message })
    })
    if (!res.ok) throw new Error('Formspree error')
    const data = await res.json().catch(()=>null)
    if (data && data.errors) throw new Error('Formspree validation')
    doneContact.value = true
    Object.assign(contact, { name: '', email: '', message: '', gotcha: '' })
  } catch (e){
    errorContact.value = true
  } finally {
    loadingContact.value = false
  }
}
async function submitAppt(){
  // 一時停止中：送信しない
  if (bookingDisabled) return
  // 現在は使用しないため、何もしない
}
</script>
<style scoped>
.forms{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.form{padding:22px}
.form h3{margin:0 0 12px}
label{display:block;margin:10px 0;color:var(--muted);font-size:14px}
input,textarea{width:100%;margin-top:6px;padding:12px 12px;border:1px solid var(--border);border-radius:10px;background:#fff;color:var(--fg);font-size:16px}
.row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
button[disabled]{opacity:.6}
.coming-soon{position:relative;}
.soon-overlay{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:18px;background:rgba(255,255,255,0);color:var(--fg);border-radius:12px;transition:background .25s ease, opacity .25s ease;opacity:0;text-align:center}
.coming-soon:hover .soon-overlay{background:rgba(255,255,255,.85);backdrop-filter:saturate(1.2) blur(3px);opacity:1}
.soon-overlay.active{background:rgba(255,255,255,.9);backdrop-filter:saturate(1.2) blur(3px);opacity:1}
.overlay-inner{max-width:260px}
.soon-label{display:inline-block;padding:8px 14px;border:1px solid var(--border);border-radius:999px;background:rgba(255,255,255,.95);font-weight:700;letter-spacing:.12em;font-size:12px}
.overlay-msg{margin:14px 0 0;font-size:14px;line-height:1.5;font-weight:500}
.overlay-msg a{text-decoration:none;font-weight:600}
@media (max-width: 900px){
  .forms{grid-template-columns:1fr}
}
/* タッチデバイス対応 */
@media (hover: none) and (pointer: coarse) {
  .soon-overlay {
    opacity: 0.3;
    background: rgba(255,255,255,0.3);
  }
  .soon-overlay.active {
    opacity: 1;
    background: rgba(255,255,255,.9);
    backdrop-filter: saturate(1.2) blur(3px);
  }
  .coming-soon {
    cursor: pointer;
  }
}
</style>
<style>
#contact{scroll-margin-top:90px}
</style>
