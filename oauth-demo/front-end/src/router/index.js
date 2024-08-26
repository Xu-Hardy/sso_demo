import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home.vue';
import Login from '@/components/Login.vue';
import AuthCallback from '@/components/AuthCallback.vue';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: { requiresAuth: true } // 需要验证
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/auth/callback',
      name: 'AuthCallback',
      component: AuthCallback
    }
  ]
});

// 全局前置守卫
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('access_token');
  // 检查是否需要认证和token是否存在
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!token) {
      next({ 
        path: '/login',
        query: { redirect: to.fullPath }  // 将用户尝试访问的页面路径作为参数传递
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
