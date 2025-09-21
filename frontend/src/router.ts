import { createRouter, createWebHistory } from 'vue-router'

const HomePage = () => import('./pages/HomePage.vue')
const Preventive = () => import('./pages/services/Preventive.vue')
const General = () => import('./pages/services/General.vue')
const Orthodontics = () => import('./pages/services/Orthodontics.vue')
const Pediatric = () => import('./pages/services/Pediatric.vue')
const OralSurgery = () => import('./pages/services/OralSurgery.vue')
const FAQ = () => import('./pages/FAQ.vue')

export const router = createRouter({
  history: createWebHistory('/kobayashi-dental-clinic/'),
  routes: [
    { path: '/', name: 'home', component: HomePage },
  { path: '/services/preventive', name: 'services-preventive', component: Preventive },
    { path: '/services/general', name: 'services-general', component: General },
    { path: '/services/orthodontics', name: 'services-orthodontics', component: Orthodontics },
    { path: '/services/pediatric', name: 'services-pediatric', component: Pediatric },
    { path: '/services/oral-surgery', name: 'services-oral-surgery', component: OralSurgery },
  { path: '/faq', name: 'faq', component: FAQ },
  ],
  scrollBehavior(to: any, from: any, savedPosition: any) {
    if (savedPosition) return savedPosition
    if (to.hash) return { el: to.hash, behavior: 'smooth' }
    return { top: 0 }
  }
})
