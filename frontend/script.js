
var messages = [], 
  lastUserMessage = "", 
  botMessage = "", 
  botName = 'Chatbot', 
  talking = true;
function chatbotrequest(xhttp,message) {
  talking = true;
  xhttp.open("POST", "http://127.0.0.1:5000/v2/ask", true);
  xhttp.setRequestHeader("Content-type", "application/json");
  var data = {"message":message}
  xhttp.send(JSON.stringify(data));
  
}
function chatbotreply(xhttp){
	xhttp.onload= function() {
       botMessage1 = this.response;
	   botMessage2 = JSON.parse(botMessage1);
	   botMessage = botMessage2["answer"];
	   messages.push("<b>" + botName + ":</b> " + botMessage);
	   Speech(botMessage);
	
  };
  for (var i = 1; i < 8; i++) {
      if (messages[messages.length - i])
        document.getElementById("chatlog" + i).innerHTML = messages[messages.length - i];
    }
}
//user enter 
function newEntry(xhttp) {
  if (document.getElementById("chatbox").value != "") {
    lastUserMessage = document.getElementById("chatbox").value;
    document.getElementById("chatbox").value = "";

	
    chatbotrequest(xhttp,lastUserMessage);
	messages.push(lastUserMessage);
  }
}

//text to Speech
//https://developers.google.com/web/updates/2014/01/Web-apps-that-talk-Introduction-to-the-Speech-Synthesis-API
function Speech(say) {
  if ('speechSynthesis' in window && talking) {
    var utterance = new SpeechSynthesisUtterance(say);
    speechSynthesis.speak(utterance);
  }
}

document.onkeypress = keyPress;
// ¡°Enter to input¡±
function keyPress(e) {
  var x = e || window.event;
  var key = (x.keyCode || x.which);
  var xhttp = new XMLHttpRequest();
  if (key == 13 || key == 3) {
    newEntry(xhttp);
	chatbotreply(xhttp);
	
    
  }
}
function placeHolder() {
  document.getElementById("chatbox").placeholder = "";
}