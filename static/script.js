// static/script.js
// Make data structure for prof_pic URLs
var mugshots = [
    '/static/img/favicon.jpg',
    '/static/img/Killington_mugshot.jpg',
    // '/static/img/Niagara_mugshot.jpg',
    // '/static/img/Graduation_mugshot.jpg',
    '/static/img/Oozefest_mugshot.jpg'
]

// Returns capitalized string
function capitalize(s) {
    return s[0].toUpperCase() + s.slice(1);
}

// Puts corresponding scene on stage
function put_scene(elem) {
    // Hide all scenes, then unhide corresponding scene
    $('.scene').addClass('hidden');
    var target = $(elem).attr('id').split('_')[0];
    $('#' + target + '_scene').removeClass('hidden');

    // Deselect all entries, then select corresponding entry
    $('.entry').removeClass('bg-selected');
    $(elem).addClass('bg-selected');

    // Update page title
    $('title').text('The ' + capitalize(target) + ' of ADB');
}

// Puts home scene on stage
function show_home() {
    put_scene(document.getElementById('home_entry'));
}

// Runs when page is done loading
$(function() {
    // Add new tab link functionality. This is necessary because of the markdown parsing
    $('a').attr('target', '_blank');

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
    $('.project-caption').hover(
        function() {
            $(this).removeClass('hidden');
            $(this).siblings().addClass('img-blurred');
        },
        function() {
            $(this).siblings().removeClass('img-blurred');
            $(this).addClass('hidden');
        }
    );

    // Add prof-pic swap functionality
    $('#mugshot').click(function() {
        var index = Math.floor(Math.random() * mugshots.length);
        var new_src = mugshots[index];
        mugshots[index] = $(this).attr('src');
        $(this).attr('src', new_src);
    });
});
