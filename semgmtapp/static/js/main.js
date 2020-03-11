$(document).ready(function () {
    /* ADD PROPERTY TYPE SELECTION BUTTON RENT OR BUY */
    $('.for-rent-div').hide();

    $("#toBuy-tab").click(function () {
        $('.for-rent-div').hide();
        $('.for-sale-div').show();
    });

    $("#toRent-tab").click(function () {
        $('.for-sale-div').hide();
        $('.for-rent-div').show();
    });
    /* ---------------- */
    /* Property Go back button */
    function goBack() {
        window.history.back();
    }
    /*  -------  */

    /* Dropdown sort Type selection */
    $('#sort_by').change(function () {
        const selection = this.options[this.selectedIndex].value;
        document.location.href = `/properties_list?search=${selection}`;
    });

    $('#sort_by_agent').change(function () {
        const selection = this.options[this.selectedIndex].value;
        document.location.href = `/my_ads?search2=${selection}`;
    });
    /* ---------------- */

    /* Modals in Agent Profile */
    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus');
    });

    /* Alert fade-out */
    $(".alert").delay(3000).slideUp(200, function () {
        $(this).alert('close');
    });

});