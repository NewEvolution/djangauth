'use strict'

angular.module('Djangauth', ['ngRoute'])
  .constant('apiUrl', 'http://localhost:8000')
  .config([
    '$httpProvider',
    function ($httpProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
  ])
