import { createRouter, createWebHistory } from 'vue-router'
import { ref,computed } from 'vue'
import HomeView from '../views/HomeView.vue'
import MovieListView from '../views/MovieListView.vue'
import MovieDetailView from '../views/MovieDetailView.vue'
import ReviewSearchView from '../views/ReviewSearchView.vue'
import RecommendedView from '../views/RecommendedView.vue'

// Vue.use(VueRouter);

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/movies',
      name: 'MovieList',
      component: MovieListView
    },
    {
      path: '/:movieId',
      name: 'moviedetail',
      component: MovieDetailView
    },
    {
      path: '/review-search',
      name: 'review-search',
      component: ReviewSearchView
    },
    {
      path: '/recommended',
      name: 'recommended',
      component: RecommendedView
    },
  ]
})

export default router
