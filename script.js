
//typing animation
function showTyping() {
    let box = document.getElementById("chatbox");

    let div = document.createElement("div");
    div.className = "bot typing";
    div.id = "typing";
    div.innerHTML = "Bot is typing<span class='dots'></span>";

    box.appendChild(div);
    box.scrollTop = box.scrollHeight;
}
function removeTyping()
{
    let typing=document.getElementById("typing");
    if(typing) typing.remove();
}

function sendMessage() {
    let input = document.getElementById("userInput");
    let message = input.value.trim();
    if (!message) return;

    addMessage("You: " + message, "user");
    input.value = "";

    showTyping();

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(res => res.json())
    .then(data => {
        setTimeout(() => {
            removeTyping();
            addMessage(data.reply, "bot");
        }, 1000);
    })
    .catch(err => {
        removeTyping();
        addMessage("Error connecting to server", "bot");
    })
}

function addMessage(text, cls) {
    let box = document.getElementById("chatbox");
    let div = document.createElement("div");
    div.className = cls;
    div.innerText = text;
    box.appendChild(div);
    // Smooth scroll
    box.scrollTo({
        top: box.scrollHeight,
        behavior: "smooth"
    });
    
 
}
   //enter key support
   document.getElementById("userInput").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
