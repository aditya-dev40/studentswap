const message_timeout = document.querySelectorAll('.message-timer');

setTimeout(function() {

    message_timeout.forEach(function(message) {
        message.style.display = "none";
    });
    
}, 2500);
