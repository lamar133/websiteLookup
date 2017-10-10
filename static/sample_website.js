$(document).ready(function () {
    var show = document.querySelectorAll('.sample_website');

    Array.prototype.slice.call(show).forEach(function(title){
        title.addEventListener('click', function(e){
            $('#siteInput').val(this.innerHTML);
        })
    })
});