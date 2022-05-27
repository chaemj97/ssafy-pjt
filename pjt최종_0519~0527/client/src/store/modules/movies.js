import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import _ from 'lodash'

export default {
  state: {
    topten: [],
    movies: [],
    movie: {},
    genres: {},
    time: {},
    birth: {},
    md: {}, 
  },
  getters: {
    topten: state => state.topten,
    movies: state => state.movies,
    movie: state => state.movie,
    genres: state => state.genres,
    time: state => state.time,
    birth: state => state.birth,
    md: state => state.md,
  },
  mutations: {
    SET_TOP_TEN: (state, topten) => state.topten = topten,
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MOVIE_REVIEWS: (state, reviews) => state.movie.review_set = reviews,
    SET_GENRES: (state, genres) => state.genres = genres,
    SET_TIME: (state, time) => state.time = time,
    SET_SERACH_MOVIES: (state,birth) =>state.birth = birth,
    SET_MD: (state,md) => state.md = md,
  },
  actions: {
    fetchTopTen({commit, getters}) {
      axios({
        url: drf.movies.topten(),
        method: 'GET',
      })
        .then(res => {
          if (getters.topten.length === 0) {
            commit('SET_TOP_TEN', res.data)
          }
          
          commit('SET_TOP_TEN', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },
    fetchMovies({commit, getters}) {
      axios({
        url: drf.movies.movies(),
        method: 'GET',
        // headers: getters.authHeader,
      })
        .then(res => {
          if (getters.movies.length === 0) {
            commit('SET_MOVIES', res.data)
          }
          const numbers = _.range(1, res.data.length)
          const sampleNums = _.sampleSize(numbers, 30)
          let sampleMovies = []
          for (const key in sampleNums) {
            sampleMovies.push(res.data[sampleNums[key]])
          }
          commit('SET_MOVIES', sampleMovies)
        })
        .catch(err => {
          console.log(err)
        })
    },
    fetchMovie({commit, }, moviePk) {
      axios({
        url: drf.movies.movie(moviePk),
        method: 'GET',
        // headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
        })
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({name: 'NotFound404'})
          }
        })
    },
    likeMovie({commit, getters}, moviePk) {
      axios({
        url: drf.movies.likeMovie(moviePk),
        method: 'POST',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE', res.data)
        })
        .catch(err => {
          console.error(err.response)
        })
    },
    createReview({commit, getters, dispatch}, {moviePk, score}) {
      const review = {score}
      axios({
        url: drf.movies.reviews(moviePk),
        method: 'POST',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
          dispatch('fetchMovie', moviePk)
        })
        .catch(err => {
          console.error(err.response)
        })
    },
    updateReview({commit, getters, dispatch}, {moviePk, reviewPk, score}) {
      const review = {score}
      axios({
        url: drf.movies.review(moviePk, reviewPk),
        method: 'PUT',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_MOVIE_REVIEWS', res.data)
          dispatch('fetchMovie', moviePk)
        })
        .catch(err => {
          console.error(err.response)
        })
    },
    deleteReview({commit, getters, dispatch}, {moviePk, reviewPk}) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.movies.review(moviePk, reviewPk),
          method: 'DELETE',
          data: {},
          headers: getters.authHeader,
        })
          .then(res => {
            commit('SET_MOVIE_REVIEWS', res.data)
            dispatch('fetchMovie', moviePk)
          })
          .catch(err => {
            console.error(err.response)
          })
      } 
    },
    fetchMovieGenre({commit, }) {
      axios({
        url: drf.movies.genre(),
        method: 'GET',
        // headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_GENRES', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    fetchMovieTime({commit, }) {
      axios({
        url: drf.movies.time(),
        method: 'GET',
        // headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_TIME', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    fetchMovieMd({commit}) {
      axios({
        url: drf.movies.md(),
        method: 'GET',
        
      })
        .then(res => {
          commit('SET_MD', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    searchMovie({commit}, {birthday}){
      axios({
        url: drf.movies.birth(),
        method: 'post',
        data: {birthday},
        // headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_SERACH_MOVIES',res.data)
      })
      .catch(err => console.log(err.response))
    },

  },
}