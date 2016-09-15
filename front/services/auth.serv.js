'use strict'

let credentials = {};

class AuthService {
  authorized (creds) {
    return new Promise((resolve, reject) => {
      if (creds) {
        credentials = creds;
      } else if (credentials.hasOwnProperty('username')) {
        resolve(window.btoa(`${credentials.username}:${credentials.password}`));
      } else {
        reject(false);
      }
    })
  }
}

angular.module('Djangauth').service('authService', AuthService);
