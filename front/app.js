'use strict'

const app = angular.module('Djangauth', ['ngRoute']) // eslint-disable-line no-unused-vars
  .config([
    '$httpProvider',
    '$routeProvider',
    function ($httpProvider, $routeProvider) { // eslint-disable-line no-unused-vars
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    }
  ])
