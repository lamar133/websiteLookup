$(document).ready(function () {
    
    
    $('#profile_container').each(function() {
        
        $('#actor_name').hide();
        
        $('#reveal_bttn').click(function () {
            $('#actor_name').toggle()
        });
        
        $('#next_bttn').click(function () {
            $('#actor_name').hide()
        });
        
        $('#prev_bttn').click(function () {
            $('#actor_name').hide()
        });

        $(this).find('img').first().siblings().hide();
        $(this).find('.name').first().siblings().hide();

        $(this).find('#next_bttn').click(function () {
            $(this)
                .parent('#profile_container')
                .find('img:first-child')
                .fadeOut(function () {
                $(this)
                    .next()
                    .fadeIn()
                $(this)
                    .appendTo($(this).parent())
            });
            $(this)
                .parent('#profile_container')
                .find('.name:first-child')
                .fadeOut(function () {
                $(this)
                    .next()
                    .fadeIn()
                $(this)
                    .appendTo($(this).parent())
            });

        });

        $(this).find('#prev_bttn').click(function () {
            $(this)
                .parent('#profile_container')
                .find('img:first-child')
                .fadeOut(function () {
                $(this)
                    .parent()
                    .find('img:last-child')
                    .fadeIn()
                    .prependTo($(this).parent())
            });
            $(this)
                .parent('#profile_container')
                .find('.name:first-child')
                .fadeOut(function () {
                $(this)
                    .parent()
                    .find('.name:last-child')
                    .fadeIn()
                    .prependTo($(this).parent())
            });

        });

    });
});