import Ember from 'ember';
import HonUtils from '../utils/hon';

export default Ember.Controller.extend({

  needs: ['application'],

  actions: {

    createAccount: function() {
      this.set('formFailed', false);

      HonUtils.ajax({
        type: 'POST',
        url: HonENV.APP.host + '/accounts',
        data: {name: this.get('account')},
        success: function() {
          this.transitionToRoute('/' + this.get('model').user_slug);
        },
        error: function(xhr) {
          this.set('formFailed', true);
          this.set('error', xhr.responseJSON);
        },
        context: this,
      });
    },
  },
});
