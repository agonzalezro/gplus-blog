var Post = new Backbone.Model.extend({
  title: 'test'
});

var Buzz = Backbone.Collection.extend({
  model: Post,
  url: '/buzz'
});

buzz = new Buzz;

buzz.fetch({
  success: function() {
    console.log('success');
  }
});
