var csrftoken = getCookie('csrftoken');

let timerslider = document.getElementById("timerslider");
let timertext = document.getElementById("timertext");
let timeForOff = document.getElementById("offtime").innerHTML
let temp
let all_leds = 0


var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("X-CSRFToken", csrftoken);

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

window.setInterval(getTimeForOff, 1000);
document.getElementById("bigbutton").addEventListener("click", putTimeForOff);
document.getElementById("iroffbutton").addEventListener("click", turnOffTimeNow);
document.getElementById("7LED").addEventListener("click", led7);
document.getElementById("14LED").addEventListener("click", led14);

function led7(){
  all_leds = 0
  console.log("all_leds: " + all_leds);
  document.getElementById("7LED").className = "btn btn-primary"
  document.getElementById("14LED").className = "btn btn-secondary"

  var raw = JSON.stringify({"all_leds":all_leds});
  var requestOptions = {
      method: 'PATCH',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    
    fetch("http://192.168.0.18/babymon/apileds/1/", requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));

}


function led14(){
  all_leds = 1;
  console.log("all_leds: " + all_leds);

  document.getElementById("14LED").className = "btn btn-primary"
  document.getElementById("7LED").className = "btn btn-secondary"

  var raw = JSON.stringify({"all_leds":all_leds});
  var requestOptions = {
      method: 'PATCH',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
    };
    
    fetch("http://192.168.0.18/babymon/apileds/1/", requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
}

window.setInterval(countdown, 100);


function turnOffTimeNow() {
    newTimeForOff = Date.now()
    timeForOff = newTimeForOff

    var raw = JSON.stringify({"on_until":newTimeForOff,"duty_cycle_percent":dutyslider.value,"all_leds":all_leds});
    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };
      
      fetch("http://192.168.0.18/babymon/apileds/1/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}


function putTimeForOff() {
    let newTimeForOff = Date.now() + timerslider.value*1000;
    timeForOff = newTimeForOff

    var raw = JSON.stringify({"on_until":newTimeForOff,"duty_cycle_percent":dutyslider.value,"all_leds":all_leds});
    var requestOptions = {
        method: 'PUT',
        headers: myHeaders,
        body: raw,
        redirect: 'follow'
      };
      
      fetch("http://192.168.0.18/babymon/apileds/1/", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
}


function countdown(){
    let timeNow = Date.now();
    let timeLeft = timeForOff - timeNow;
    //console.log(timeForOff)
    //document.getElementById("timeNow").innerHTML = timeNow;
    //document.getElementById("timeForOff").innerHTML = timeForOff;
    //console.log(timeLeft);

    if (timeLeft < 0) {
        
        document.getElementById("timeLeft").innerText =  '0.0'
        document.getElementById("bigbutton").className = 'btn btn-dark'
    }
    else {
        document.getElementById("timeLeft").innerText = (timeLeft/1000).toFixed(1);
        document.getElementById("bigbutton").className = 'btn btn-warning'
    }
}


function getTimeForOff(){

    var requestOptions = {
        method: 'GET',
        headers: myHeaders,
        redirect: 'follow'
      };
      
        fetch("http://192.168.0.18/babymon/apileds/1/", requestOptions)
        .then((response) => {
          return response.json();
        })
        .then((myJson) => {
          timeForOff = myJson.on_until;
        });
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
