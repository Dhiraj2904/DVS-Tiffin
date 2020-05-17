$('.btn').click(function() {
  $('#content div').hide();
  var target = '#' + $(this).data('target');
  $(target).show();
})