showContent = function (content_id) {
  $('#left-content').animate({"width": "40vw"}, 400);
  $('.collapse-button-left').css('display', 'block');
}

hideContent = function () {
  $('#left-content').animate({"width": "0"}, 400);
  $('.collapse-button-left').css('display', 'none');
}
