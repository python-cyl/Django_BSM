window.onload=function(){
	var input1=document.getElementById('input1');
	var input2=document.getElementById('input2');
	// var dj=document.getElementById('dj');
	// var incon_eye=document.getElementById('incon_eye');
	input1.onclick = show1;
	input2.onclick=show2;
	// dj.onclick=show3;
	function show1(){
		input1.style.borderBottom='2px solid #ffffff';
		input2.style.borderBottom='none';
	}
	function show2(){
		input1.style.borderBottom='none';
		input2.style.borderBottom='2px solid #ffffff';
	}
	// function show3{
	// 	if(input2.attr("type")=="text"){
 //            input2.attr("type","password");
 //            incon_eye.css("opacity",0.5);
 //        }
 //        else{
 //            input2.attr("type","text");
 //            incon_eye.css("opacity",1);
 //        }
	// }

   
}   