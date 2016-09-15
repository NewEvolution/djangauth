'use strict'

angular.module('Djangauth')
  .config([
    '$routeProvider',
    function ($routeProvider) {
      $routeProvider
        .when('/auth', {
          controller: 'AuthControl',
          controllerAs: 'auth',
          templateUrl: '/partials/auth.html',
        })
    }
  ])
