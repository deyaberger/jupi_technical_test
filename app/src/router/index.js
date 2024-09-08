import { createRouter, createWebHistory } from 'vue-router'
import Suggestion from '../components/Suggestion.vue'
import SearchBar from '../components/SearchBar.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: SearchBar
    },
    {
      path: '/suggestion/:name',
      name: 'Suggestion',
      component: Suggestion
    }
  ]
})

export default router
