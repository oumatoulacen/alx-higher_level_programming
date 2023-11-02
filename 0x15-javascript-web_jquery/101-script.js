$(document).ready(function () {
  $('div#add_item').click(function () {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });
  $('div#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
/* $(document).ready(function() {
    $("#add_item").on("click", function() {
        $("ul.my_list").append("<li>Item</li>");
    });

    $("#remove_item").on("click", function() {
        $("ul.my_list li:last").remove();
    });

    $("#clear_list").on("click", function() {
        $("ul.my_list").empty();
    });
});
 */
