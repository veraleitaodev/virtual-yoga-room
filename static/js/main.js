$(document).ready(function () {

    // to change background colour to expanded elements on navbar once menu button is clicked
    $('.navbar-toggler').click(function () {
        console.log('menu button was clicked, it works!');

        $('#navbarSupportedContent').addClass('bg-black');
    });

    // on scroll down homepage change navbar background to black
    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#transparent-navbar').addClass('bg-dark-pink');

        } else {
            $('#transparent-navbar').removeClass('bg-dark-pink');
        }
    });

    // Update the copyright date in the footer
    $("#copyright").text(new Date().getFullYear());

    // to enable bootstrap tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
});