$(document).ready(function() {
    // Categories Dropdown
    $('.dropdown-toggle').dropdown();

    // Pins Isotope
    $('.grid').isotope({
        itemSelector: '.grid-item',
        masonry: {
            columnWidth: 20,
            gutter: 0,
            fitWidth: true
        }
    });

    var elements = $('.grid').find('.grid-item');
    $('.grid').addClass('is-showing-items').isotope('revealItemElements', elements);
});