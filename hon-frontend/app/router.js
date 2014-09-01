import Ember from 'ember';

var Router = Ember.Router.extend({
  location: HonENV.locationType
});

Router.map(function() {
  this.resource('accounts', {path: '/:user_slug'});
  this.resource('new-account', {path: '/:user_slug/new-account'});
  this.resource('account-transactions', {path: '/:user_slug/:account_slug'});
});

export default Router;
