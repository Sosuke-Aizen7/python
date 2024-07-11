document.getElementById("startBtn").addEventListener("click", startListening);

function startListening() {
  chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
    chrome.tabs.sendMessage(tabs[0].id, { command: "startListening" });
  });
}

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
  if (request.command === "updateOutput") {
    document.getElementById("output").innerText = request.text;
  }
});


chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.command === "startListening") {
      // Communicate with the Python script here
      // Use an AJAX request or other suitable method
    }
  });
  