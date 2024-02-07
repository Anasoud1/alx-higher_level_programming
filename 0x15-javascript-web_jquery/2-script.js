const element = $('header');
const element2 = $('DIV#red_header');
element2.on('click', function () {
  element.css('color', '#FF0000');
});
