import { createRouter, createWebHistory } from 'vue-router'
import LandingView from '../views/LandingView.vue';
import BooksListView from '../views/BooksListView.vue';
import BookDetailView from '../views/BookDetailView.vue';
import ThreadsListView from '../views/ThreadsListView.vue';
import ThreadDetailView from '../views/ThreadDetailView.vue';
import ThreadWriteView from '../views/ThreadWriteView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'LandingView',
      component: LandingView,
    },
    {
      path: '/threads',
      name: 'ThreadsListView',
      component: ThreadsListView,
    },
    { path: '/threads/:threadId', 
      name:'ThreadDetailView',
      component: ThreadDetailView },
    {
      path: '/threads/:bookId/write',
      name: 'ThreadWriteView',
      component:  ThreadWriteView,
    },
    {
      path: '/books',
      name: 'BooksListView',
      component: BooksListView,
    },
    {
      path: '/books/:bookId',
      name: 'BookDetailView',
      component: BookDetailView,
    },
  ],
})

export default router
