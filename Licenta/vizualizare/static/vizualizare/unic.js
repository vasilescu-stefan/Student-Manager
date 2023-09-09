
$(document).ready(function() {
  $('form').on('submit', function(event) {
    

    // Get the selected values from the dropdowns
    var optiune1 = $('#id_preference1').val();
    var optiune2 = $('#id_preference2').val();
    var optiune3 = $('#id_preference3').val();
    var optiune4 = $('#id_preference4').val();

    // Check if the values are different
    if (optiune1 !== optiune2 && optiune1 !== optiune3 && optiune1 !== optiune4 && optiune2 !== optiune3 && optiune2 !== optiune4 && optiune3 !== optiune4) {
      // Values are different
      alert('Dropdown values are different.');
    } else {
      // Values are the same
      alert('Dropdown values are the same.');
      event.preventDefault();
    }
  });
});