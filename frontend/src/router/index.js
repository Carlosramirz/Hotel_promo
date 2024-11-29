import { createRouter, createWebHistory } from 'vue-router';
import RegisterForm from '@/views/RegisterForm.vue';
import VerifyEmail from '@/views/VerifyEmail.vue';
import AdminLogin from '@/views/AdminLogin.vue';
import AdminPanel from '@/views/AdminPanel.vue';


const routes = [
    { path: '/', component: RegisterForm},
    { path: '/verify-email', component: VerifyEmail},
    { path: '/admin-login', component: AdminLogin},
    { path: '/admin-panel', component: AdminPanel, meta: { requiresAuth: true}},
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

router.beforeEach((to, from, next) => {
    const token = localStorage.getItem('token');
    if (to.path === '/admin-panel' && !token) {
        next('/admin-login');
    } else {
        next();
    }
})


export default router;