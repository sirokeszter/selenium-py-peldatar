<iframe id="youtubeframe" width="420" height="346" src="https://www.youtube.com/embed/tgbNymZ7vqY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>

var stopVideo = function ( element ) {
	var iframe = element.querySelector( 'document.querySelector("#youtubeframe")');
	var video = element.querySelector( 'document.querySelector("#movie_player")');
	if ( iframe ) {
		var iframeSrc = iframe.src;
		iframe.src = iframeSrc;
	}
	if ( video ) {
		video.pause();
	}
};