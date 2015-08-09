var prof_pics = [
    '/static/img/Chimney_prof_pic.jpg',
    '/static/img/Killington_prof_pic.jpg',
    '/static/img/Niagara_prof_pic.jpg',
    '/static/img/Oozefest_prof_pic.jpg'
]

$(function() {
    $('.navigation-row').attr('onclick', 'show_page(this)');
    $('#profile_image').click(function() {
        var index = Math.floor(Math.random() * prof_pics.length);
        var new_src = prof_pics[index];
        prof_pics[index] = $('#profile_image').attr('src');
        $('#profile_image').attr('src', new_src);
    });
});

function show_page(elem) {
    $('.navigation-row').removeClass('bg-info');
    $('.page-div').addClass('hidden');

    $(elem).addClass('bg-info');
    var target = $(elem).attr('id').replace('_navigation', '');
    $('#' + target).removeClass('hidden');
}
