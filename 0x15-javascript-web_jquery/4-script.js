$('DIV#toggle_header').click(function () {
  const header = $('header');
  if (header.hasClass('green')) {
    header.removeClass('green').addClass('red');
  } else if (header.hasClass('red')) {
    header.removeClass('red').addClass('green');
  }
});
