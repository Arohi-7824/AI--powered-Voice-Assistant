const startBtn = document.getElementById('start-btn');
const responseElem = document.getElementById('response');

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if (!SpeechRecognition) {
  responseElem.textContent = "Your browser doesn't support speech recognition.";
} else {
  const recognition = new SpeechRecognition();
  recognition.lang = 'en-US';
  recognition.interimResults = false;
  recognition.maxAlternatives = 1;

  startBtn.onclick = () => {
    recognition.start();
    responseElem.textContent = "🎙️ Listening...";
  };

  recognition.onresult = async (event) => {
    const transcript = event.results[0][0].transcript;
    responseElem.textContent = `You said: "${transcript}"`;

    try {
      const res = await fetch('/api/message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: transcript })
      });

      const data = await res.json();

      if (data.response) {
        responseElem.textContent = `Gemini: ${data.response}`;
        const utterance = new SpeechSynthesisUtterance(data.response);
        window.speechSynthesis.speak(utterance);
      } else {
        responseElem.textContent = "No response from assistant.";
      }
    } catch (err) {
      responseElem.textContent = "Request failed.";
    }
  };

  recognition.onerror = (event) => {
    responseElem.textContent = `Error: ${event.error}`;
  };
}
