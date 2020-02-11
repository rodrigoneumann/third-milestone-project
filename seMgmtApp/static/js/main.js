$(document).ready(function () {
    $('.for-rent-div').hide();

    $("#toBuy-tab").click(function () {
        $('.for-rent-div').hide();
        $('.for-sale-div').show();
    });

    $("#toRent-tab").click(function () {
        $('.for-sale-div').hide();
        $('.for-rent-div').show();
    });

});