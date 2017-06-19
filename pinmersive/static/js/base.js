$(document).ready(function() {
    $('.dropdown-toggle').dropdown();

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