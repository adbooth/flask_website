// Make data structure for prof_pic URLs
var prof_pics = [
    '/static/img/favicon.jpg',
    '/static/img/Killington_prof_pic.jpg',
    '/static/img/Niagara_prof_pic.jpg',
    // '/static/img/Graduation_prof_pic.jpg',
    '/static/img/Oozefest_prof_pic.jpg'
]

$(function() {
    // Start page on about page
    show_home();

    // Add new tab link functionality
    $('a').attr('target', '_blank');

    // Add navigation functionality to rows
    $('.navigation-row').attr('onclick', 'show_page(this)');

    // Add prof-pic swap functionality
    $('.profile-image').click(function() {
        var index = Math.floor(Math.random() * prof_pics.length);
        var new_src = prof_pics[index];
        prof_pics[index] = $('.profile-image').attr('src');
        $('.profile-image').attr('src', new_src);
    });

    $('.name-div').click(show_home);

    // Add project image hover functionality
    $('.project-thumb').hover(
        function() {
            $(this).addClass('img-blurred');
            $(this).siblings().removeClass('hidden');
        },
        function() {
            $(this).siblings().addClass('hidden');
            $(this).removeClass('img-blurred');
        }
    );
    $('.project-text').hover(
        function() {
            $(this).removeClass('hidden');
            $(this).siblings().addClass('img-blurred');
        },
        function() {
            $(this).siblings().removeClass('img-blurred');
            $(this).addClass('hidden');
        }
    );
});

function show_page(elem) {
    // Hide all pages
    $('.navigation-row').removeClass('bg-selected');
    $('.page-div').addClass('hidden');

    // Show make corresponding page
    $(elem).addClass('bg-selected');
    var target = $(elem).attr('id').replace('_navigation', '');
    $('#' + target).removeClass('hidden');
    $('title').text('The ' + capitalize(target) + ' of ADB');
}

function show_home() {
    show_page(document.getElementById('home_navigation'));
}

function show_stage(elem) {
    $('.navigation-row').removeClass('bg-selected');
    $('.page-div').addClass('hidden');

    var target = $(elem).attr('id').replace('_image', '');
    $('#' + target).removeClass('hidden');
    $('title').text('A Project of ADB');
}

function capitalize(s) {
    return s[0].toUpperCase() + s.slice(1);
}
