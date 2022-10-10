// <script src="{{ url_for('static', filename='main.js') }}"></script> で接続します。

// eventApp
const addEventDiv = document.getElementById("addEventDiv");
const openEventButton = document.getElementById("openEventButton");
const closeEventButton = document.getElementById("closeEventButton");

function displayBlockAddEventDiv() { 
    openEventButton.style.display = "none";
    addEventDiv.style.display = "block";
    closeEventButton.style.display = "block";
}

function displayNoneAddEventDiv() {
    openEventButton.style.display = "block";
    addEventDiv.style.display = "none";
    closeEventButton.style.display = "none";
}

// timerApp

var secNum = 0;
var minNum = 0;
var hourNum = 0;
var total = 0;
var audio = document.getElementById('btn_audio');
var title = document.getElementById('title');
var subtitle = document.getElementById('subtitle');
var box = document.getElementById('box');

function changeSec() {
    const sec = document.getElementById("sec").value;
    document.getElementById("displaySec").innerHTML = sec + " 秒";
    secNum = sec;
}

function changeMin() {
    const min = document.getElementById("min").value;
    document.getElementById("displayMin").innerHTML = min + " 分";
    minNum = min;
}

function changeHour() {
    const hour = document.getElementById("hour").value;
    document.getElementById("displayHour").innerHTML = hour + " 時間";
    hourNum = hour;
}

function startTimer() {
    var hour_sec = hourNum * 60 * 60;
    var min_sec = minNum * 60;
    var sec_sec = secNum * 1;
    total = hour_sec + min_sec + sec_sec;
    var m = total * 1000;

    // 初期化
    title.innerHTML = "頑張って!! 📢"
    subtitle.innerHTML = "タイマーを開始しました。"
    audio.pause();
    audio.currentTime = 0;
    box.style.display = "none";

    setTimeout(function(){
        title.innerHTML = "お疲れ様でした! 🍵"
        subtitle.innerHTML = "設定した時間になりました。"
        box.style.display = "block";
        audio.play();
    },m);
}

