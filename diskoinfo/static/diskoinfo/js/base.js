$(document).ready(function() {
    // activate clikable
    $('.clickable').click(function() {
        window.location = $(this).attr('href');
        return false;
    });
});

function validateForm() {
    var x = document.forms["form"]["name"].value;
    if (x == null || x == "") {
        alert("Komentar ne smije biti prazan");
        return false;
    }
}