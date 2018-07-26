showContent = function (content_obj) {
  $('#left-content-panel').animate({"width": "40vw"}, 400);
  $('.collapse-button-left').css('display', 'inline-block');

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
