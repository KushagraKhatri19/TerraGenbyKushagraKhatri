async function generate() {
  const location = document.getElementById("location").value;
  const soil = document.getElementById("soil").value;
  const resultBox = document.getElementById("result-box");
  const resultText = document.getElementById("result");

  if (!location || !soil) {
    alert("Please fill in both location and soil type.");
    return;
  }

  resultText.textContent = "🌾 Generating AI suggestions...";
  resultBox.style.display = "block";

  try {
    const res = await fetch("/generate", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ location, soil })
    });

    const data = await res.json();
    resultText.textContent = data.recommendation;
  } catch (error) {
    resultText.textContent = "❌ Error: Could not get AI suggestions.";
  }
}
