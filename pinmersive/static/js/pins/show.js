$(document).ready(function() {
    
    $(document).mouseup(function(e) {
        var container = $('.pin-container > .modal-dialog .modal-content, #pin-show-body> .modal-forms');
        if (!container.is(e.target) && container.has(e.target).length === 0) {
            parent.history.back();
            return false;
        }
    });
});