const closeBtn = document.getElementById('js-close-btn');
const deleteCancel = document.getElementById('js-delete-cancel');
const nodeDeletePopUp = document.querySelector('.delete-popup-bg');


function openDeletePopUP() {
    nodeDeletePopUp.classList.add('toggleBtn');
}

deleteCancel.onclick = function() {
    nodeDeletePopUp.classList.remove('toggleBtn');
}

closeBtn.onclick = function() {
    nodeDeletePopUp.classList.remove('toggleBtn');
}


const nodeBuyPopUp = document.querySelector('.buy-popup-bg');

function openBuyPopUp() {
    nodeBuyPopUp.classList.add('toggleBtn');
}

// window.onclick = function(event) {
//     if(event.target == nodeBuyPopUp)  {
//         nodeBuyPopUp.style.display = 'none';
//     }
//     if(event.target == nodeDeletePopUp)  {
//         nodeDeletePopUp.classList.remove('toggleBtn');
//     }
// }

