$(document).ready(function () {

    // Display Siri-like speaking message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        // Set text inside the <p class="siri-message">
        $(".siri-message").text(message);

        // Optional: play animation if using textillate.js
        $('.siri-message').textillate({ in: { effect: 'fadeIn' } });
    }

    // Show hood animation
    eel.expose(ShowHood)
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
    }

    // Show sender (user) message in chat bubble
    eel.expose(senderText)
    function senderText(message) {
        const chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `
            <div class="row justify-content-end mb-4">
                <div class="width-size">
                    <div class="sender_message">${message}</div>
                </div>
            </div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    // Show receiver (assistant) message in chat bubble
    eel.expose(receiverText)
    function receiverText(message) {
        const chatBox = document.getElementById("chat-canvas-body");
        if (message.trim() !== "") {
            chatBox.innerHTML += `
            <div class="row justify-content-start mb-4">
                <div class="width-size">
                    <div class="receiver_message">${message}</div>
                </div>
            </div>`;
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    }

    // Hide loader and show face auth animation
    eel.expose(hideLoader)
    function hideLoader() {
        $("#Loader").attr("hidden", true);
        $("#FaceAuth").attr("hidden", false);
    }

    // Hide face auth and show success
    eel.expose(hideFaceAuth)
    function hideFaceAuth() {
        $("#FaceAuth").attr("hidden", true);
        $("#FaceAuthSuccess").attr("hidden", false);
    }

    // Hide face auth success and show greeting
    eel.expose(hideFaceAuthSuccess)
    function hideFaceAuthSuccess() {
        $("#FaceAuthSuccess").attr("hidden", true);
        $("#HelloGreet").attr("hidden", false);
    }

    // Hide start screen and show Siri blob
    eel.expose(hideStart)
    function hideStart() {
        $("#Start").attr("hidden", true);

        setTimeout(function () {
            $("#Oval").addClass("animate__animated animate__zoomIn");
        }, 1000);

        setTimeout(function () {
            $("#Oval").attr("hidden", false);
        }, 1000);
    }

});
