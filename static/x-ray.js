console.log("JS loaded");

document.getElementById("uploadForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const fileInput = document.getElementById("fileInput");
  const preview = document.getElementById("previewArea");
  const allowedTypes = [
    "image/jpeg",
    "image/jpg",
    "image/png",
    "application/pdf",
  ];

  const message = document.createElement("div");
  message.id = "message";
  preview.innerHTML = ""; // Clear previous preview and message

  if (fileInput.files.length > 0) {
    const file = fileInput.files[0];

    if (!allowedTypes.includes(file.type)) {
      message.textContent =
        "Invalid file type. Please upload a .pdf, .jpg, .jpeg, or .png.";
      message.style.color = "red";
      preview.appendChild(message);
      return;
    }

    const reader = new FileReader();

    reader.onload = function (e) {
      const result = file.type.startsWith("image/")
        ? `<img src="${e.target.result}" alt="Scan Image" style="max-width:300px;" />`
        : `<p>PDF Uploaded: ${file.name}</p>`;

      preview.innerHTML = `
        <p>Uploaded File:</p>
        ${result}
      `;

      message.textContent = "Successfully uploaded!";
      message.style.color = "green";
      preview.appendChild(message);
    };

    reader.readAsDataURL(file);
  }
});

// Dropdown toggle function
function toggleDrop(dropElement) {
  dropElement.classList.toggle("active");
}
