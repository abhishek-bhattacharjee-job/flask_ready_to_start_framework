$(document).ready(function() {
  // Function to change the background color when the button is clicked
  $('#changeColorBtn').click(function() {
    var randomColor = getRandomColor();
    $('body').css('background-color', randomColor);
  });

  // Function to generate a random color in hexadecimal format
  function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

  // Function to call my_get_api on button click
  $('#changeColorBtn').click(function() {
    $.get('http://localhost:8000/my_get_api', function(data) {
      $('#get_call_responseArea').text(JSON.stringify(data));
    });
  });

  // Function to call my_post_api on button click
  $('#changeColorBtn').click(function() {
      var jsonData = {
        key1: 'value1',
        key2: 'value2'
      };

      // Convert the JSON data into a string
      var jsonString = JSON.stringify(jsonData);

      // Send the POST request with the JSON data
      $.ajax({
        url: 'http://localhost:8000/my_post_api',
        type: 'POST',
        contentType: 'application/json', // Set the content type to JSON
        data: jsonString,
        success: function(data) {
          $('#post_call_responseArea').text(JSON.stringify(data));
        },
        error: function(xhr, status, error) {
          console.error('Error:', error);
        }
      });
    });
});
