
"use strict";
// debugger;
// THE MOST IMPORTANT LINE you should add when using a background video
$('.background-video video').on('click', e => e.preventDefault());

function scaleVideo() {
if ($(window).innerWidth() > $(window).innerHeight()) {
 $('.background-video video').attr('width', $(window).innerWidth());
 $('.background-video video').attr('height', '');
} else {
 $('.background-video video').attr('height', $(window).innerHeight());
 $('.background-video video').attr('width', '');
}

// Also set the height of <header>, so that all your important content goes
// BELOW the video
$('header').height($('.background-video video').height());
}
// Wait for EVERYTHING to load before resizing the video. If we don't do
// Caveat: this causes the page to look wonky on initial load.
$(window).on('load', scaleVideo);  // for fun, comment this line out!

// Resize the video if the window is resized
$(window).on('resize', scaleVideo);
