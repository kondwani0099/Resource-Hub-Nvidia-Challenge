const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');
const images = []; // Array to store captured images

// Request access to the user's webcam
navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    video.srcObject = stream;
  })
  .catch(err => {
    console.error("Error accessing webcam: ", err);
  });

// Capture image every 5 seconds
const captureImages = setInterval(() => {
  if (images.length < 4) { // Capture up to 4 images
    // Draw video frame to canvas
    context.drawImage(video, 0, 0, canvas.width, canvas.height);

    // Convert canvas to base64-encoded image
    const imageData = canvas.toDataURL('image/jpeg');
    images.push(imageData); // Store the image

    console.log(`Captured image ${images.length}`);
  } else {
    // Stop capturing after 4 images and send to backend
    clearInterval(captureImages);
    sendImagesToBackend(images);
  }
}, 5000); // Capture every 5 seconds

// Function to send captured images to the backend
function sendImagesToBackend(images) {
  fetch('http://127.0.0.1:5000/upload_image', {  // Change this to your server URL
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ images: images }) // Send the array of images
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok ' + response.statusText);
    }
    return response.json();
  })
  .then(data => {
    console.log("Images uploaded successfully:", data);
  })
  .catch(err => {
    console.error("Error uploading images:", err);
  });
}