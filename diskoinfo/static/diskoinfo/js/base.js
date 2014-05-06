$(document).ready(function() {
    // activate clikable
    $('.clickable').click(function() {
        window.location = $(this).attr('href');
        return false;
    });
});
