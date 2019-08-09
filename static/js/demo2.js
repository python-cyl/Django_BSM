
window.onload=function(){
	var menu=document.getElementById('menu');
	var ull=document.getElementById('ull');
	var tri=document.getElementById('tri');
	var con=document.getElementById('blank');
	menu.onclick = show;
	con.onclick=hide;
	function show(){
		ull.style.display='block';
		tri.style.display='block';
	}
	function hide(){
		ull.style.display='none';
		tri.style.display='none';
	}

}