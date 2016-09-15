'use strict'

angular.module('Djangauth')
  .config([
    '$routeProvider',
    function ($routeProvider) {
      $routeProvider
        .when('/', {
          controller: 'HomeControl',
          controllerAs: 'home',
          templateUrl: '/partials/home.html'
        })
    }
  ])
