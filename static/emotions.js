async function uploadImage(images) {
    const response = await fetch('/upload_image', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ images: images })
    });

    const data = await response.json();

    if (data.error) {
        alert(data.error);
    } else {
        showEmotionPopup(data.detected_emotions, data.responses);
    }
}

function showEmotionPopup(emotions, responses) {
    const resultsContainer = document.getElementById('emotion-results');
    resultsContainer.innerHTML = '';

    emotions.forEach((emotion, index) => {
        const responseText = responses[index] || "Stay positive and keep going!";
        resultsContainer.innerHTML += `
            <div class="response-item">
                <strong>Detected Emotion:</strong> ${emotion} <br>
                <strong>Encouragement:</strong> ${responseText}
            </div>
        `;
    });

    document.getElementById('emotion-popup').classList.remove('hidden');
}

function closePopup() {
    document.getElementById('emotion-popup').classList.add('hidden');
}

const element = document.getElementById("emotionDetection");

  let offsetX, offsetY, isDragging = false;

  element.addEventListener("mousedown", (e) => {
    isDragging = true;
    offsetX = e.clientX - element.offsetLeft;
    offsetY = e.clientY - element.offsetTop;
    document.addEventListener("mousemove", onMouseMove);
    document.addEventListener("mouseup", onMouseUp);
  });

  function onMouseMove(e) {
    if (isDragging) {
      element.style.left = `${e.clientX - offsetX}px`;
      element.style.top = `${e.clientY - offsetY}px`;
    }
  }

  function onMouseUp() {
    isDragging = false;
    document.removeEventListener("mousemove", onMouseMove);
    document.removeEventListener("mouseup", onMouseUp);
  }