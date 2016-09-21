function doPostBack(cb) {
	var id=cb.id.substring(1);
	var el=document.getElementById(id);
	if(cb.checked){
		el.style.display = 'block';
	}else{
		el.style.display = 'none';
	}
}

function myload(){
	var all_classes = document.getElementsByClassName("school");
	var i;
	for (i = 0; i < all_classes.length; i++) {
		all_classes[i].style.display = "none";
	}
	all_classes = document.getElementsByClassName("mycheck");
	for (i = 0; i < all_classes.length; i++) {
		all_classes[i].style.zoom = "1.5";
	}
}
