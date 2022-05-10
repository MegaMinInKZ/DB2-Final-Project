const closeBtn = document.getElementById('js-close-btn');
const deleteCancel = document.getElementById('js-delete-cancel');
const nodeDeletePopUp = document.querySelector('.delete-popup-bg');


function openDeletePopUP(button) {
    nodeDeletePopUp.classList.add('toggleBtn');
    document.getElementById("cart_id_delete").value = button.getAttribute("cart_id")

}

deleteCancel.onclick = function() {
    nodeDeletePopUp.classList.remove('toggleBtn');
}

closeBtn.onclick = function() {
    nodeDeletePopUp.classList.remove('toggleBtn');
}

// buy popup 
const nodeBuyPopUp = document.querySelector('.buy-popup-bg');

function openBuyPopUp(button) {
    nodeBuyPopUp.classList.add('toggleBtn');
    document.getElementById("cart_id_buy").value = button.getAttribute("cart_id")
}
// buy popup 


// checkout popup 
const nodeCheckoutPopUp = document.querySelector('.checkout-popup-bg');

function openCheckoutPopUp(button) {
    nodeCheckoutPopUp.classList.add('toggleBtn');
    document.getElementById("cart_id_update").value = button.getAttribute("cart_id")
    document.getElementById("amount_input").setAttribute('max', button.getAttribute("amount"))
    document.querySelector(".checkout-max-amount").innerHTML = "Max: " + button.getAttribute("amount")
}

// checkout popup 




window.onclick = function(event) {
    if(event.target == nodeCheckoutPopUp)  {
        nodeCheckoutPopUp.classList.remove('toggleBtn');
    }
    if(event.target == nodeDeletePopUp)  {
        nodeDeletePopUp.classList.remove('toggleBtn');
    }
}

