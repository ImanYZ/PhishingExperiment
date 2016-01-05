$(document).ready(function(){
    $(".btn-game").click(function(){
        if ($(this).hasClass( "btn-info" )) {
            $(this).removeClass( "btn-info" );
            var siblingBtn = $(this).parent().parent().find(".btn-info");
            siblingBtn.removeClass( "btn-info" );
            siblingBtn.addClass( "btn-default" );
            $(this).addClass( "btn-success" );
        }
        else if ($(this).hasClass( "btn-default" )) {
            $(this).removeClass( "btn-default" );
            var siblingBtn = $(this).parent().parent().find(".btn-success");
            siblingBtn.removeClass( "btn-success" );
            siblingBtn.addClass( "btn-default" );
            $(this).addClass( "btn-success" );
        }
        var thisId = $(this).attr('id');
        var inputId = thisId.substring(0, thisId.length - 7);
        $("#" + inputId).val(this.name);
    });
    $("#Decision1OptionA").click(function(){
    });
});

function swapBtnsClasses(btnObj) {
}