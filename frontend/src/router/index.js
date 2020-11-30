import {createRouter, createWebHistory} from 'vue-router'
import Data1 from "../views/Data1Page"
import Data2 from "../views/Data2Page"

const routes = [
    {
        path: '/',
        redirect: () => ({"s": 1})
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
