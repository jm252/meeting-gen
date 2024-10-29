// static/index.js

const uploadArea = document.getElementById('upload-area');
const fileInput = document.getElementById('file-input');
const fileSelect = document.getElementById('file-select');
const fileList = document.getElementById('file-list');
const generateBtn = document.getElementById('generate-btn');

// Open file dialog when "Choose File" button is clicked
fileSelect.addEventListener('click', () => fileInput.click());

// Handle file selection via the input field
fileInput.addEventListener('change', handleFiles);

// Highlight area when file is dragged over it
uploadArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    uploadArea.classList.add('drag-over');
});

// Remove highlight when file is dragged out
uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('drag-over');
});

// Handle file drop
uploadArea.addEventListener('drop', (event) => {
    event.preventDefault();
    uploadArea.classList.remove('drag-over');

    const files = event.dataTransfer.files;
    handleFiles({ target: { files } });
});

// Display selected files (only MP4) and enable generate button
function handleFiles(event) {
    const files = event.target.files;
    fileList.innerHTML = ''; // Clear the list

    const validFiles = Array.from(files).filter(file => file.type === 'video/mp4');

    if (validFiles.length === 0) {
        fileList.textContent = 'Please select only MP4 files.';
        disableGenerateButton();
    } else {
        validFiles.forEach((file) => {
            const listItem = document.createElement('p');
            listItem.textContent = `🎥 ${file.name}`;
            fileList.appendChild(listItem);
        });
        enableGenerateButton();
    }
}

// Enable the "Generate" button
function enableGenerateButton() {
    generateBtn.disabled = false;
    generateBtn.classList.add('active');
}

// Disable the "Generate" button
function disableGenerateButton() {
    generateBtn.disabled = true;
    generateBtn.classList.remove('active');
}
