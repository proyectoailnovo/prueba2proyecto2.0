/*Esto es un test*/
function search_product() { 
    let input = document.getElementById('searchbar').value 
    input=input.toLowerCase(); 
    let x = document.getElementsByClassName('item');
    let results=false;

    for (i = 0; i < x.length; i++) {  
        if (!x[i].innerHTML.toLowerCase().includes(input)) { 
            x[i].style.display="none";
            
        } 
        else { 
            x[i].style.display="block";
            results=true;
                           
        }
    }
    if (results){
        $(".mensajevacio").css("display","none");   
    } 
    else{
        $(".mensajevacio").css("display","block");
    }
}
/*Término del test*/ 
function refreshcheckbox(){
    numbeer=$('body').find(".item").length;

    $('body').find(".item").each(function(index,element) {
        console.log($(element).children());
        if($(element).children()[1].checked==false){
        numbeer--;
        }   
    });
    if (numbeer==0) {
        $("#buybtton").prop("disabled",true);
    }
    else{
        $("#buybtton").prop("disabled",false);
    }
}
function bruteforce(id_num){
    verific=$("#num"+id_num).val();
    if (verific=="") {
        verific=1;
    }
    if(verific>30){
        verific=30;
    }
    if(verific<0){
        verific=1;
    }
    $("#num"+id_num).val(parseInt(verific));

}