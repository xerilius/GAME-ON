
"use strict";
// debugger;
$('.background-video video').on('click', e => e.preventDefault());

function scaleVideo() {
if ($(window).innerWidth() > $(window).innerHeight()) {
 $('.background-video video').attr('width', $(window).innerWidth());
 $('.background-video video').attr('height', '');
} else {
 $('.background-video video').attr('height', $(window).innerHeight());
 $('.background-video video').attr('width', '');
}
// sets height of <header> so content goes below video
$('header').height($('.background-video video').height());
}
// Wait for EVERYTHING to load before resizing the video
$(window).on('load', scaleVideo);
$(window).on('resize', scaleVideo);
