import Ember from 'ember';
import HonUtils from '../utils/hon';

export default Ember.Controller.extend({

  needs: ['application'],

  actions: {

    login: function() {
      this.set('loginFailed', false);

      var data = {
        username: this.get('username'),
        password: this.get('password'),
      };

      HonUtils.ajax({
        type: 'POST',
        url: HonENV.APP.host + '/login',
        data: data,
        success: function(user) {
          this.set('controllers.application.User', user);
          localStorage['user_slug'] = user.username;
          this.transitionToRoute('/' + user.username);
        },
        error: function(xhr) {
          this.set('loginFailed', true);
          this.set('error', xhr.responseJSON);
        },
        context: this,
      });
    },
  },
});
