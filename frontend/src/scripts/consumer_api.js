
const API = "http://localhost:5000/api/v1";
function get(url) {
  return Vue.axios.get(API + url);
}

function post(url, body, header = {}) {
    JSON.stringify(body)
  return Vue.axios.post(API + url, body);
}

export { get, post };
