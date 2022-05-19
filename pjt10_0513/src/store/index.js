import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movies: [],
    lists:[]
  },
  getters: {
  },
  mutations: {
    CREATE_LIST : function(state,listItem){
      state.lists.push(listItem)
    },
    LOAD_MOVIES(state, movielist) {
      state.movies = movielist
    },
  },
  actions: {
    load_movies(context) {
      const params = {
        'api_key' : '44cbb73b3c3a4210576ca36e0b33784e',
        'language' : 'ko',
        'region' : 'KR',
      }
      axios({
        method: 'get',
        url: 'https://api.themoviedb.org/3/movie/top_rated',
        params: params,
      })
      .then(response => { 
        // console.log(response.data)
        context.commit('LOAD_MOVIES', response.data.results)
      })
      .catch(error => {
        console.log(error)
      })
    },
    createList : function({commit},ListItem){
      commit('CREATE_LIST',ListItem)
    }
  },
  modules: {
  }
})
