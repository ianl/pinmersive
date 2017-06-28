$(document).ready(function() {
    // Board-Item Pins Isotope
    $('.board-item-pins-grid').isotope({
        itemSelector: '.board-item-pins-grid-item',
        masonry: {
            columnWidth: 14,
            gutter: 3,
            isFitWidth: true
        }
    });

    var elements = $('.board-item-pins-grid').find('.board-item-pins-grid-item');
    $('.board-item-pins-grid').addClass('is-showing-items').isotope('revealItemElements', elements);
});