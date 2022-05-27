import Vue from 'vue'
import VueRouter from 'vue-router'

import MovieListView from '@/views/movies/MovieListView.vue'
import MovieDetailView from '@/views/movies/MovieDetailView.vue'
import MovieGenreView from '@/views/movies/MovieGenreView.vue'
import MovieTimeView from '@/views/movies/MovieTimeView.vue'
import MovieBirthView from '@/views/movies/MovieBirthView.vue'
import MovieMdView from '@/views/movies/MovieMdView.vue'

import ArticleListView from '@/views/articles/ArticleListView.vue'
import ArticleDetailView from '@/views/articles/ArticleDetailView.vue'
import ArticleNewView from '@/views/articles/ArticleNewView'
import ArticleEditView from '@/views/articles/ArticleEditView'

import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: MovieListView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticleListView
  },
  {
    path: '/articles/create',
    name: 'articleNew',
    component: ArticleNewView
  },
  {
    path: '/articles/:articlePk',
    name: 'article',
    component: ArticleDetailView
  },
  {
    path: '/articles/:articlePk/edit',
    name: 'articleEdit',
    component: ArticleEditView
  },
  
  {
    path: '/movies/genre',
    name: 'movieGenre',
    component: MovieGenreView
  },
  {
    path: '/movies/time',
    name: 'movieTime',
    component: MovieTimeView
  },
  {
    path: '/movies/birth',
    name: 'movieBirth',
    component: MovieBirthView
  },
  {
    path: '/movies/md',
    name: 'movieMd',
    component: MovieMdView
  },
  {
    path: '/movies/:moviePk',
    name: 'movie',
    component: MovieDetailView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
