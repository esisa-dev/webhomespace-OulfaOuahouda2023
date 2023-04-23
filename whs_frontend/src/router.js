import { createRouter, createWebHistory } from 'vue-router';
import Login from './components/Login.vue';
import UserHome from './components/UserHome.vue';

const routes = [
  {
    path: '/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/home',
    name: 'UserHome',
    component: UserHome,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
