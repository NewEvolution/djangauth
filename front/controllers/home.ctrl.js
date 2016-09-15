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
  .controller('HomeControl', function () {
    const home = this;
    home.heading = 'Yep, got us some AngularJS';
  })
