import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Student from "../views/Student"
import StudentManager from "../views/StudentManager";
import AddStudent from "../views/AddStudent";
import Index from "../views/index"
import StudentUpdate from "../views/StudentUpdate";

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  {
    path: '/',
    name:"图书管理",
    component:Index,
    show: true,
    redirect:"/StudentManager",
    children:[
      {
        path: '/StudentManager',
        name:'查询人员',
        component: StudentManager
      },
      {
        path: '/AddStudent',
        name:'添加人员',
        component: AddStudent
      }
    ]
  },
  {
    path:'/StudentUpdate',
    name: "更新人员",
    component: StudentUpdate,
    show: false
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
