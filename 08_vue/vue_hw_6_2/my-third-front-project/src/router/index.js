import { createRouter, createWebHistory } from 'vue-router'
import SomeView from '@/views/SomeView.vue'
import OtherView from '@/views/OtherView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home', 
      component: SomeView
    },
    {
      path: '/other',
      name: 'other', 
      component: OtherView
    },
  
  ]
})

export default router // 다른곳에서 쓰고 싶다 외부로 내보내기 main.js 에서 씀
// export default를 걸어주니까 main.js에서 사용할 수 있음.
