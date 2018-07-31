showContent = function (content_obj) {
  $('#left-content-panel').animate({"width": "40vw"}, 400);
  $('.collapse-button-left').css('display', 'inline-block');
  theme_id = content_obj.header_id;
  $('#theme_'+theme_id).addClass('active');
  $('#theme_'+theme_id+'_layers').addClass('in');

  $.ajax({
    type: "GET",
    url: "/rea/get_content",
    // contentType: "application/json; charset=utf-8",
    dataType: 'html',
    data: content_obj,
    success: function(content) {
      console.log(data);
      $('#left-content').html(content);
    },
    error: function(data, error) {
      console.log(error);
    }
  });

};

hideContent = function () {
  $('#left-content-panel').animate({"width": "0"}, 400);
  $('.collapse-button-left').css('display', 'none');
  $('#left-content').html(null);
};

showFoci = function(foci_div_id, event) {
  $('.foci-menu').hide(300);
  $('#'+foci_div_id).show(200);
  event.stopPropagation();
}
