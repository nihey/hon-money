import Ember from 'ember';
import HonUtils from '../utils/hon';

export default Ember.Route.extend({

  setupController: function(controller, model) {
    controller.set('model', model);

    HonUtils.ajax({
      type: 'GET',
      url: HonENV.APP.host + '/accounts',
      success: function(accounts) {
        controller.set('accounts', accounts);
      },
      context: this,
    });
  },
});
