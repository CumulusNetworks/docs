$(function() {

    ///////////////////////////////////////////
    // TOP ANNOUNCEMENT BAR //////////////////
    /////////////////////////////////////////

    // Create cookie. Expiration date is determined in Wagtail.
    function setdismissNvidiaAnnouncementBlogPost() {
        $.cookie('dismissNvidiaAnnouncementBlogPost', 'true', { expires: 5, path: '/' });
    }

    // Check if dismissNvidiaAnnouncementBlogPost cookie exists
    if ( !$.cookie('dismissNvidiaAnnouncementBlogPost') ) {
        $('body').prepend('<div class="cta announcement-bar nvidia-green"> <a href="javascript:void(0)" class="close"><img src="//icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" alt="Close" class="svg"></a> <p>Cumulus Networks is now NVIDIA&reg;. <a href="https://blogs.nvidia.com/blog/2020/06/16/cumulus-programming-networks/"  target="_blank">Learn more</a>.</p></div>');
        $('head').append('<style>@media screen and (min-width: 992px){body{transition: all 0.5s; -webkit-transition: all 0.5s;}.globalNav{top: 60px;}.globalNav.snapp {top: 12px;}body{position: relative; top: 60px;}}</style>');
    }

    // Close the announcement bar when the user hits the X button
    $('body').on('click','.cta.announcement-bar a.close', function(e){
        $('.cta.announcement-bar').css('top', '-60px');
        $('.globalNav, body').css('top', '0');
        setdismissNvidiaAnnouncementBlogPost();
        e.preventDefault();
    });

    //////////////////////////////////////////////
    // BOTTOM ANNOUNCEMENT BAR //////////////////
    ////////////////////////////////////////////

    var banner = null;

    // Show the banner
    if ( !$.cookie('dismissNvidiaAnnouncementBlogPostMobile') && !$('.m-bottom-promo-banner').length) {

        banner = '<div class="m-bottom-promo-banner nvidia-green"><a href="" class="close"><img src="//icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" alt="Close" class="svg close-banner"></a><h3>Cumulus Networks is now NVIDIA&reg;.</h3><a href="https://blogs.nvidia.com/blog/2020/06/16/cumulus-programming-networks/" class="m-button m-button-white m-button-medium" target="_blank" style="color: rgb(94, 94, 94);">Learn more</a>.</div>';

        $(banner).insertBefore('footer');

        setTimeout(function(){
            $('.m-bottom-promo-banner').addClass('active');
        },500);

    }

    // Create mobile cookie. Expiration date is determined in Wagtail.
    function setdismissNvidiaAnnouncementBlogPostMobile() {
        $.cookie('dismissNvidiaAnnouncementBlogPostMobile', 'true', { expires: 5, path: '/' });
    }

    // Close the banner when the user hits the X button
    $('body').on('click','.m-bottom-promo-banner a.close', function(e){
        $('.m-bottom-promo-banner').remove();
        setdismissNvidiaAnnouncementBlogPostMobile();
        e.preventDefault();
    }); 

});