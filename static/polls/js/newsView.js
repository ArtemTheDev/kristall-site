// User Interactive buttons
const userActivityBtns = document.querySelector( '.userActivity' );

const liked = target => {
    target.classList.add('fa-heart');
    target.classList.remove('fa-heart-o');

    let likeTitle = $(target).siblings();

    likeTitle[0].style.color = 'red';
    likeTitle[0].style.transition = '.3s';
};

const disliked = target => {
    target.classList.remove('fa-heart');
    target.classList.add('fa-heart-o');

    let likeTitle = $(target).siblings();

    likeTitle[0].style.color = '';
    likeTitle[0].style.transition = '.3s';
};

AllNews.onclick = function(event) {
    let target = event.target;
    if (target.classList.contains('LikeBtn')) {
        if (target.classList.contains('fa-heart-o')) {
            liked(target);
        } else {
            disliked(target);
        }
    }
};

$(document).ready(function(){
    $('.newsIMG').each(function(){
        $(this).error(function(){
            $(this).remove();
        });
    });
});