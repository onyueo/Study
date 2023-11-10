import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SavedVideosView from '../views/SavedVideosView.vue'
import SearchView from '../views/SearchView.vue'
import VideoDetailView from '../views/VideoDetailView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path : '/',
      name : 'home',
      component :HomeView
    },
    {
      path : '/search',
      name : 'search',
      component :SearchView
    },
    {
      path : '/detail/:videoId',
      name : 'detail',
      component :VideoDetailView
    },

    /////////////////////
    {
      path : '/saved',
      name : 'saved',
      component : SavedVideosView
    },
  ]
})

export default router
