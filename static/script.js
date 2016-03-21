// static/script.js
// Make data structure for prof_pic URLs
var mugshots = [
    '/static/img/Chimney_mugshot.jpg',
    '/static/img/Killington_mugshot.jpg',
    '/static/img/favicon.jpg',
    '/static/img/Niagara_mugshot.jpg',
    '/static/img/Oozefest_mugshot.jpg'
];

// Returns capitalized string
function capitalize(s) {
    return s[0].toUpperCase() + s.slice(1);
}

// Puts corresponding scene on stage
function put_scene(elem) {
    // Remove all traces of previous scene
    $('.scene').addClass('hidden');
    $('.entry').removeClass('bg-selected');
    // Get target scene data
    var keywords = $(elem).attr('id').split('_');
    var scene = keywords[0];
    // Show target scene
    $('#' + scene + '_scene').removeClass('hidden');
    $(elem).addClass('bg-selected');

    // Determine scene type
    if (keywords[1] == 'entry') {
        // Standard scene - update title to scene name
        $('title').text('Andrew Booth - ' + capitalize(scene));
        document.location.hash = scene;
    } else {
        // Project scene
        $('title').text('Andrew Booth - Projects');
        document.location.hash = '';
    }
}
// Puts home scene on stage
function put_home() {
    put_scene(document.getElementById('home_entry'));
}

function swap_mug() {
    var random_index = Math.floor(Math.random() * mugshots.length);
    var new_src = mugshots[random_index];
    mugshots[random_index] = $('#mugshot').attr('src');
    $('#mugshot').attr('src', new_src);
}

// Runs when page is done loading
$(function() {
    // Implement anchor hash
    var hash = document.location.hash.replace('#', '');
    var scene_elem = document.getElementById(hash + '_entry');
    if (hash && scene_elem) {
        put_scene(scene_elem);
    } else {
        put_home();
    }

    // Start with random mugshot of the first two
    var random_index = Math.floor(Math.random() * 2);
    $('#mugshot').attr('src', mugshots[random_index]);
    mugshots = mugshots.splice(random_index);

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

    // Add mugshot swap functionality
    $('#mugshot').click(swap_mug);
});
