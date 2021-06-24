jQuery('document').ready(function(){
    $('#koko1').keyup(function(){
        var z = $(this).val();
        var a = $('#koko3').val();
        var kok = (z-(z/100*a))
        if(a == 0){
        $('#koko4').val(z);
        }
        else {
        $('#koko4').val(kok);
        }

    });
    $('#koko3').keyup(function(){
        var z = $(this).val();
        var a = $('#koko1').val();
        var kok = (a-(a/100*z))
        if(z == 0){
        $('#koko4').val(a);
        }
        else {
        $('#koko4').val(kok);
        }
    });
});
