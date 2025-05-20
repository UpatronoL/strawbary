window.enlargeGraph = function (graphId) {
    const modal = document.getElementById('graph-modal');
    const modalImg = document.getElementById('modal-img');
    const graph = document.getElementById(graphId);

    if (modal && modalImg && graph) {
        const originalWidth = graph.naturalWidth;
        const originalHeight = graph.naturalHeight;

        modalImg.src = graph.src; 
        modalImg.style.width = `${originalWidth * 1.50}px`;
        modalImg.style.height = `${originalHeight * 1.50}px`;

        modal.style.display = 'flex'; 
    } else {
        console.error("Modal elements or graph not found!");
    }
};

window.closeModal = function () {
    const modal = document.getElementById('graph-modal');
    if (modal) {
        modal.style.display = 'none'; 
    } else {
        console.error("Modal not found!");
    }
};

window.onload = function () {
    const modal = document.getElementById('graph-modal');
    if (modal) {
        modal.style.display = 'none';
    }
};

