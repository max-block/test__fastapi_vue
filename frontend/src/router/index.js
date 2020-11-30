import {createRouter, createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import Data1 from "../views/Data1"
import Data2 from "../views/Data2"

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/data1',
        name: 'Data1',
        component: Data1
    },
    {
        path: '/data2',
        name: 'Data2',
        component: Data2
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
