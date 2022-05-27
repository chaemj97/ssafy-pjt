const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'

export default {
  admin:{
    admin: () => HOST + 'admin/'
  }, 
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    topten: () => HOST + MOVIES + 'topten/',
    movies: () => HOST + MOVIES,
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    likeMovie: moviePk => HOST + MOVIES + `${moviePk}/` + 'like/',
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + 'reviews/',
    review: (moviePk, reviewPk) => HOST + MOVIES + `${moviePk}/` + 'reviews/' + `${reviewPk}/`,
    genre: () => HOST + MOVIES + 'genre/',
    time: () => HOST + MOVIES + 'time/',
    birth: () => HOST + MOVIES + 'birth/',
    md: () => HOST + MOVIES + 'md/',
  },
  articles: { 
    articles: () => HOST + ARTICLES,
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    // comments: () => HOST + ARTICLES + COMMENTS, // 댓글 목록
    comment: (articlePk,commentPk) => HOST + ARTICLES +`${articlePk}/`+ COMMENTS + `${commentPk}/`, // 댓글 디테일
    commentcreate: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS, // 댓글 생성
  },
}
