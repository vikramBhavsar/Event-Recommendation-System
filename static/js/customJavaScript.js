

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function sendGetRequest(){

    var csrf_token = getCookie('csrftoken');

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function (){
        var myData = JSON.parse(this.responseText);
    }

    // xhttp.open('GET','/collector/test',true);

    xhttp.open('POST','/collector/put_evidence/',true);
    xhttp.setRequestHeader('X-CSRFToken',csrf_token);
    xhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    xhttp.send('movie=justice_league&director=zack snyder');
}

function sendEvidenceToCollector(userid,eventid,evidenceType){
    // alert(`User: ${userid}\nEvent:${eventid}\nEvidence:${evidenceType}`);

    var csrf_token = getCookie('csrftoken');
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        
    }

    xhttp.open('POST','/collector/put_evidence/',true);
    xhttp.setRequestHeader('X-CSRFToken',csrf_token);
    xhttp.setRequestHeader('Content-type','applica  tion/x-www-form-urlencoded');
    xhttp.send(`user=${userid}&eventid=${eventid}&evidenceType=${evidenceType}`);

}


function testRecommendation(){
    
}

function sendHistoryToServerUsingGet(){
    alert("From inside send history to server")
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        alert(xhttp.responseText);
    }

    xhttp.open('GET','/recommender/index/',true);
    // xhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded');
    xhttp.send();
}
