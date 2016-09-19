'use strict'

let credentials = null;

class AuthService {
  authorized (creds) {
    return new Promise((resolve, reject) => {
      if (creds) {
        credentials = window.btoa(`${creds.username}:${creds.password}`);
        $cookies.put('djangauth', credentials); // eslint-disable-line no-undef
      } else if (credentials) {
        credentials = $cookies.get('djangauth'); // eslint-disable-line no-undef
      }
      if (credentials) {
        resolve(credentials);
      }
      reject(false);
    })
  }
}

angular.module('Djangauth').service('authService', ['$cookies', AuthService]);
