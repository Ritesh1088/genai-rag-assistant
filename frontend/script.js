async function askQuestion() {
  const q = document.getElementById("question").value;
  const loader = document.getElementById("loader");
  const card = document.getElementById("card");

  if (!q) return;

  loader.style.display = "block";
  card.style.display = "none";

  try {
    const res = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ question: q })
    });

    const data = await res.json();

    document.getElementById("answer").innerText =
      data.answer || "No answer received";

    document.getElementById("sources").innerHTML =
      "<b>Sources:</b><ul>" +
      (data.sources || []).map(s => `<li>${s}</li>`).join("") +
      "</ul>";

  } catch {
    document.getElementById("answer").innerText =
      "Backend not reachable (Offline mode)";
    document.getElementById("sources").innerHTML = "";
  }

  loader.style.display = "none";
  card.style.display = "block";
}
