import Ember from 'ember';
import HonUtils from '../utils/hon';

export default Ember.Controller.extend({

  needs: ['application'],

  actions: {

    createTransaction: function() {
      this.set('formFailed', false);

      var data = {
        name: this.get('name'),
        value: this.get('value'),
        account_name: this.get('model').account_slug,
      };

      HonUtils.ajax({
        type: 'POST',
        url: HonENV.APP.host + '/transactions',
        data: data,
        success: function(transaction) {
          this.get('transactions').pushObject(transaction);
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
