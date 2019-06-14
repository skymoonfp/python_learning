/*$(window).scroll(function() {

    var h = $(window).scrollTop();

    if (h < 100) {
        $("#return_top").hide();
    }
    else {
        $("#return_top").show();
    }
});*/

$(window).scroll(function() {

    var h = $(window).scrollTop();

    if (h >= 100) {
        $("#return_top").removeClass("hide");
    }
    else {
        $("#return_top").addClass("hide");
    }
});

function GoTop() {
    $ (window).scrollTop(0);
}