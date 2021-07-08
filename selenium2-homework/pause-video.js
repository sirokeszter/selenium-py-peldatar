<video id="html5video" controls="" src="https://upload.wikimedia.org/wikipedia/commons/b/b8/Dwarf_hamsters_running_on_disc_2.ogv"></video>
<button onclick="playPause()">Play/Pause</button>

myVideo = document.querySelector("#html5video")
pauseBtn=document.querySelector("body > div > button:nth-child(1)")

//var currentTime = Math.floor (myVideo.currentTime);
//if (currentTime == 10) {
//myVideo.pause (1);

pauseBtn.onclick = function () {
myVideo.pause ();
}
