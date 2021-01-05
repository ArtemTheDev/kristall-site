const liked = target => {
    target.classList.toggle('fa-heart');
    target.classList.toggle('fa-heart-o');

    let likeTitle = $(target).siblings();

    if (target.classList.contains ( 'fa-heart' )) {likeTitle[0].style.color = 'red'; likeTitle[0].style.transition = '.3s';}
    else {likeTitle[0].style.color = '';}
};

AllNews.onclick = function(event) {
    let target = event.target;
    if (target.classList.contains ( 'LikeBtn' )) {
       liked(target);
  }
};