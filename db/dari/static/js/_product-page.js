var nodeCommentBtn = document.querySelector('.js-comment');
var nodeFeedbackBtn = document.querySelector('.js-feedback');
var nodeComment = document.querySelector('.input-comment');
var nodeFeedback = document.querySelector('.input-feedback');

console.log(nodeCommentBtn);

function showComment() {
    nodeCommentBtn.classList.remove('display');
    nodeFeedbackBtn.classList.add('display');

    nodeComment.classList.add('bb');
    nodeFeedback.classList.remove('bb');
};

function showFeedback() {
    nodeCommentBtn.classList.add('display');
    nodeFeedbackBtn.classList.remove('display');

    nodeComment.classList.remove('bb');
    nodeFeedback.classList.add('bb');
};   