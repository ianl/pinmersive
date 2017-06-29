$(document).ready(function() {

    $('#guest-sign-in').on('click', function() {
        $('input[name=username]').val("ianthl");
        $('input[name=password]').val("pinmersive123");

        setTimeout(function(){
            $('#log-in').trigger('click');  
        }, 500);
    })
    
});