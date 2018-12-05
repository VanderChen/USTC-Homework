function clearStyle() {
    $('#test_style table').removeClass('table table-striped');
}

function setBootstrapStyle() {
    clearStyle();
    $('#test_style table').addClass('table table-striped');
}

function setHandMadeStyle1() {
    clearStyle();
}

function setHandMadeStyle2() {
    clearStyle();
}

$( document ).ready(function() {
    $('table').addClass('table table-striped');
});