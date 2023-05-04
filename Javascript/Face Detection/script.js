const video = document.getElementById('video')
const resultDiv = document.getElementById('result')
const captureButton = document.getElementById('capture')

Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('/models')
]).then(startVideo)

function startVideo() {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
      video.srcObject = stream
    })
    .catch(err => console.error(err))
}

video.addEventListener('play', () => {
  const canvas = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas)
  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions({ inputSize: 416, scoreThreshold: 0.5 })).withFaceLandmarks().withFaceExpressions()

    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas.getContext('2d').clearRect(0, 0, canvas.width, canvas.height)
    faceapi.draw.drawDetections(canvas, resizedDetections)
    faceapi.draw.drawFaceLandmarks(canvas, resizedDetections)
    faceapi.draw.drawFaceExpressions(canvas, resizedDetections)
    
    // Update emoticon results
    if (detections.length > 0) {
      const expressions = detections[0].expressions
      const maxValue = Math.max(...Object.values(expressions))
      const dominantExpression = Object.keys(expressions).find(key => expressions[key] === maxValue)
      resultDiv.innerHTML = `emotion result：${dominantExpression}`
    }
  }, 100)
})

// emotion cature
captureButton.addEventListener('click', () => {
  const canvas = document.createElement('canvas')
  canvas.width = video.videoWidth
  canvas.height = video.videoHeight
  const ctx = canvas.getContext('2d')
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
  const imgUrl = canvas.toDataURL('image/png')
  const link = document.createElement('a')
  link.href = imgUrl
  link.download = 'emotion.png'
  link.click()
})
