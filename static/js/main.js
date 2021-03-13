$(document).ready(function () {
    
   // to change background colour to expanded elements on navbar once menu button is clicked
   $('.navbar-toggler').click(function () {
    console.log('menu button was clicked, it works!');

    $('#navbarSupportedContent').addClass('bg-black');
  });

  // on scroll down homepage change navbar background to black
  $(window).scroll(function(){
      if ($(this).scrollTop() > 50) {
         $('#transparent-navbar').addClass('bg-dark-pink');
         
      } else {
         $('#transparent-navbar').removeClass('bg-dark-pink');
      }
  });

  // to update the copyright date in the footer
  $("#copyright").text(new Date().getFullYear());

  // to activate select form on lectures template
  $('#sort-selector').change(function() {
        var selector = $(this);
        var currentUrl = new URL(window.location);

        var selectedVal = selector.val();
        if(selectedVal != "reset"){
            var sort = selectedVal.split("_")[0];
            var direction = selectedVal.split("_")[1];

            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    });
    
    // back to the top button is hidden in default position and shows when the user scrolls down
    
    $(window).scroll(function() {
       console.log("page scrolling!");
     $('.back-top-btn').show();
    });

    // when the user clicks on the back to top button, the page returns to the top and the button disappears
    $('.back-top-link').click(function () {
        console.log("button was clicked!"); 
         
        window.scrollTo(0,0);
        $('.back-top-btn').hide();
        location.reload(true)
        
    });
});