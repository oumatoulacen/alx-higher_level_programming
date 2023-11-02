$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#hello').text(data.hello);
  });
});
/* fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the value
of hello from that fetch in the HTML tag DIV#hello
$.getJSON("https://fourtonfish.com/hellosalut/?lang=fr", function(resp){
    $("#hello").text(resp.hello);
}); */
/*
$.ajax({
  method: 'GET',
  url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
  dataType: 'json'
}).done(function (data) {
  $('div#hello').html(data.hello);
});
 */
