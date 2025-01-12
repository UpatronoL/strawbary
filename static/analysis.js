window.enlargeGraph = function (graphId) {
    const modal = document.getElementById('graph-modal');
    const modalImg = document.getElementById('modal-img');
    const graph = document.getElementById(graphId);

    if (modal && modalImg && graph) {
        // Get the original image dimensions
        const originalWidth = graph.naturalWidth;
        const originalHeight = graph.naturalHeight;

        // Set the modal image dimensions to twice the original size
        modalImg.src = graph.src; // Set the image source
        modalImg.style.width = `${originalWidth * 1.50}px`;
        modalImg.style.height = `${originalHeight * 1.50}px`;

        modal.style.display = 'flex'; // Show the modal
    } else {
        console.error("Modal elements or graph not found!");
    }
};


// Function to close the modal
window.closeModal = function () {
    const modal = document.getElementById('graph-modal');
    if (modal) {
        modal.style.display = 'none'; // Hide the modal
    } else {
        console.error("Modal not found!");
    }
};

// Ensure modal is hidden on page load
window.onload = function () {
    const modal = document.getElementById('graph-modal');
    if (modal) {
        modal.style.display = 'none';
    }
};

