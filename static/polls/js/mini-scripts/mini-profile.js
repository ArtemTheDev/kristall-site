let profileName = document.querySelector('.username');
let menu = document.querySelector('.profMenu');

// profileName.onclick = function() {
// 	menu.classList.toggle('active');
// }

profileName.onclick = function() {
	if  (!menu.classList.contains('active')){
		$(menu).fadeIn('fast');
		menu.classList.add('active');
	}
	else {
		$(menu).fadeOut('fast');
		menu.classList.remove('active');
	}
}