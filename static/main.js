// <script src="{{ url_for('static', filename='main.js') }}"></script> で接続します。

const addEventDiv = document.getElementById("addEventDiv")
const openEventButton = document.getElementById("openEventButton")
const closeEventButton = document.getElementById("closeEventButton")

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