$(document).ready(function() {

    $('#guest-sign-in').on('click', function() {
        $('input[name=username]').val("isabel");
        $('input[name=password]').val("pinmersive");

        setTimeout(function(){
            $('#log-in').trigger('click');  
        }, 500);
    })
    
});