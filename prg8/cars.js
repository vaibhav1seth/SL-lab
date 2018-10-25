	function merc(){

        document.getElementById("all").style.display="block";

        var mercedes={
                color: ["black","white"],
                model: ["SLS","CLA","GLA","Maybach"]
        };

        document.getElementById("models").innerHTML=mercedes.model;
        document.getElementById("colors").innerHTML=mercedes.color;
        document.getElementById("img").src="merced.jpg";
        document.getElementById("img").style.height="250px";
        document.getElementById("img").style.width="250px";
}

function aud(){


        document.getElementById("all").style.display="block";

        var aud={
                color: ["blue","red"],
                model: ["A3","R8"]
        };
        document.getElementById("models").innerHTML=aud.model;
        document.getElementById("colors").innerHTML=aud.color;
        document.getElementById("img").src="audi.jpg";
        document.getElementById("img").style.height="250px";
        document.getElementById("img").style.width="250px";
}


function lamb(){

        document.getElementById("all").style.display="block";

        var lambor={
                color: ["black","red","yellow","green"],
                model: ["Aventador","Diablo","Gallardo","Countach"],
        };
        document.getElementById("models").innerHTML=lambor.model;
        document.getElementById("colors").innerHTML=lambor.color;
        document.getElementById("img").src="lambo.jpg";
        document.getElementById("img").style.height="250px";
        document.getElementById("img").style.width="250px";
}


function bmw(){

        document.getElementById("all").style.display="block";

        var bm={
                color: ["black","white","silver"],
                model: ["X3","X5","i8","Z4"]
        };
        document.getElementById("models").innerHTML=bm.model;
        document.getElementById("colors").innerHTML=bm.color;
        document.getElementById("img").src="bmw.jpg";
        document.getElementById("img").style.height="250px";
        document.getElementById("img").style.width="250px";
}
