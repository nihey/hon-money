import Ember from 'ember';
import HonUtils from '../utils/hon';

export default Ember.Route.extend({

  setupController: function(controller, model) {
    controller.set('model', model);

    HonUtils.ajax({
      type: 'GET',
      data: {account_name: model.account_slug},
      url: HonENV.APP.host + '/transactions',
      success: function(transactions) {
        controller.set('transactions', transactions);
      },
      context: this,
    });
  },
});
