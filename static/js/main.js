$(document).ready(function () {
    
   // to change background colour to expanded elements on navbar once menu button is clicked
   $('.navbar-toggler').click(function () {
    console.log('menu button was clicked, it works!');

    $('#navbarSupportedContent').addClass('bg-black');
  });

});