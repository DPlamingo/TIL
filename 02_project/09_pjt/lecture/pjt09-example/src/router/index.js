import { createRouter, createWebHistory } from 'vue-router'
import ProductDetail from '@/views/ProductDetail.vue'
import HomeView from '@/views/HomeView.vue'
import CartView from '@/views/CartView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/cart',
      name: 'cart',
      component: CartView
    },
    {
      path: '/:productid',
      name: 'Productdetail',
      component: ProductDetail
    },
    
  ]
})

export default router
