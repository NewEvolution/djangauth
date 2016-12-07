'use strict'

angular.module('Djangauth', ['ngRoute', 'ngCookies'])
  .constant('apiUrl', 'http://localhost:8000');

angular.module('Djangauth').run(authService => {
  authService.authorize();
});
