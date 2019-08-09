window.onload=function(){
	var pass=document.getElementById('res_pass');
	var over=document.getElementById('res_over');
	var pass_information=document.getElementById('res_pass_information');
	var over_infomation=document.getElementById('res_over_information');
	pass.onclick = show;
	over.onclick=hide;
	function show(){
		pass_information.style.display='block';
		pass.style.color='#3E90FF';
		over.style.color='#404040';
		over_infomation.style.display='none';
	}
	function hide(){
		pass_information.style.display='none';
		pass.style.color='#404040';
		over.style.color='#3E90FF';
		over_infomation.style.display='block';
	}

}