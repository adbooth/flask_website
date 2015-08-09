$(function() {
    $('.navigation-row').attr('onclick', 'show_page(this)');
    show_page(document.getElementById('about_navigation'));
});

function show_page(elem) {
    var current_page = $('.current');
    current_page.addClass('hidden');
    current_page.removeClass('current');

    var target = elem.id.replace('_navigation', '');
    $('#' + target).removeClass('hidden');
    $('#' + target).addClass('current');
}
