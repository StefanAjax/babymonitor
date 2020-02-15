let timerslider = document.getElementById("timerslider");
let timertext = document.getElementById("timertext");
let timeForOff = document.getElementById("offtime").innerHTML
console.log(timeForOff);


timertext.innerHTML = timerslider.value;

timerslider.oninput = function() {
  timertext.innerHTML = this.value;
}

let dutyslider = document.getElementById("dutyslider");
let dutytext = document.getElementById("dutytext");
dutytext.innerHTML = dutyslider.value;

dutyslider.oninput = function() {
  dutytext.innerHTML = this.value;
}

document.getElementById("ironbutton").addEventListener("click", setTimer);

document.getElementById("iroffbutton").addEventListener("click", turnOffTimeNow);

function turnOffTimeNow() {
    timeForOff = Date.now()
}

function setTimer() {
    timeForOff = Date.now() + timerslider.value*1000;
}

window.setInterval(myTimer, 100);

function myTimer(){
    let timeNow = Date.now();
    let timeLeft = timeForOff - timeNow;
    //document.getElementById("timeNow").innerHTML = timeNow;
    //document.getElementById("timeForOff").innerHTML = timeForOff;

    if (timeLeft < 0) {
        document.getElementById("timeLeft").outerHTML =  '<span id="timeLeft" class="card text-dark bg-secondary">0.0</span>'
    }
    else {
        document.getElementById("timeLeft").outerHTML =  '<span id="timeLeft" class="card text-dark bg-warning"></span>'
        document.getElementById("timeLeft").innerHTML = (timeLeft/1000).toFixed(1);
    }
}