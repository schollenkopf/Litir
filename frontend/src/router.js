import {createRouter,createWebHistory} from 'vue-router'

import IntroPage from './components/IntroPage.vue'
import MainPage from './components/MainPage.vue'
import LoginPage from './components/LoginPage.vue'
import RegisterPage from './components/RegisterPage.vue'

const routes = [
    {
        path: '/',
        component: IntroPage,
        name: 'IntroPage'
    },

    {
        path: '/login',
        component: LoginPage,
        name: 'LoginPage'
    },

    {
        path: '/register',
        component: RegisterPage,
        name: 'RegisterPage'
    },

    {
        path: '/application',
        component: MainPage,
        name: 'MainPage',
    //     children: [
            // {
            //     path: 'graph',
            //     component: GraphView,
            //     name: 'GraphView'
            // },
        
            // {
            //     path: 'filter',
            //     component: FilterView,
            //     name: 'FilterView'
            // }
    //     ]
    }
]

const router = createRouter({

    history: createWebHistory(),
    routes
}
)

export default router


