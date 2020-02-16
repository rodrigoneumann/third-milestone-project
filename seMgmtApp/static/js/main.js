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


    $('#sort_by').change(function () {
        let url = null
        const selection = this.options[this.selectedIndex].value
        document.location.href = `/properties_list?search=${selection}`
    })

    $('#sort_by_agent').change(function () {
        let url = null
        const selection = this.options[this.selectedIndex].value
        document.location.href = `/my_ads?search2=${selection}`
    })
});
