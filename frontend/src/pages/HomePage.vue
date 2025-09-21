<template>
  <div>
  <HeroSection :motto="clinic?.motto" />
    <ServicesSection :services="clinic?.services" />
    <AccessSection :address="clinic?.address" :phone="clinic?.phone" :hours="clinic?.hours" :access="clinic?.access" :director="clinic?.director" />
  <ContactSection :phone="clinic?.phone" />
  </div>
</template>
<script setup lang="ts">
import HeroSection from '../components/HeroSection.vue'
import ServicesSection from '../components/ServicesSection.vue'
import AccessSection from '../components/AccessSection.vue'
import ContactSection from '../components/ContactSection.vue'

const { clinic } = defineProps<{ clinic: any | null }>()
</script>
