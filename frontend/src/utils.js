const serverOrigin = 'http://10.142.114.103:8080'

export function http(method, url, body) {
  if (!url.includes('http')) {
    url = serverOrigin + url
  }

  return window.fetch(url, {
    method,
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json'
    },
    body
  }).then(res => res.json())
}

export function get(url) {
  return http('GET', url, undefined)
}

export function post(url, json) {
  return http('POST', url, JSON.stringify(json))
}

export function put(url, json) {
  return http('PUT', url, JSON.stringify(json))
}

export function httpDelete(url) {
  return http('DELETE', url, undefined)
}

class JankState {
  constructor() {
    this.state = {};
    this.callbacks = {};
  }

  set(key, value) {
    this.state[key] = value;
  }

  get(key) {
    return this.state[key];
  }

  addCallback(name, func) {
    this.callbacks[name] = func;
  }

  dispatch(name) {
    if (this.callbacks[name]) {
      this.callbacks[name]();
    }
  }
}

export const state = new JankState();