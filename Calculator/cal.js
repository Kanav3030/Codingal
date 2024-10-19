function getshow(){
return document.getElementById("show-value").innertext;
}
function printshow(num){
    document.getElementById("show-value").innertext=num;    
}
function getoutput() {
    return document.getElementById("output-value").innertext;
}
function printoutput(num) {
    if(num==""){
    document.getElementById("output-value").innertext = num;
}
else{
        document.getElementById("output-value").innertext =getFormattedNumber(num);
}
}
function getFormattedNumber(num){
    if(num=="-"){
        return "";
    }
    var n=Number(num);
    var value=n.toLocaleString("en");
    return value;
}
function reverseNumberFormat(num){
    return Number (num.replace(/,/g,""));
}
var operator = document.getElementsByClassName("operator");
for (var i=0;i<operator.length;i++){
    operator[i].addEventListener("click" ,function(){
        if(this.id=="clear"){
            printshow("");
            printoutput("");
        }
        else if(this.id=="backspace"){
            var output=reverseNumberFormat(getoutput()).toString();
            if(output){
                output=output.substring(0,output.length-1);
                printoutput(output);
            }
        }
        else {
            var output = getoutput();
            var history = getshow();
            if(output=="" && history !=""){
                if(isNaN(history[history.length-1])){
                    history = history.substring(0,history.length - 1);
                }
            }
            if(output!=""|| history!=""){
                output=output==""?output:reverseNumberFormat(output);
                history = history + output;
                if(this.id =="="){
                    var result = eval(history);
                    printoutput(result);
                    printshow("");
                }
                else{
                    history=history + this.id;
                    printshow(history);
                    printoutput("");
                }
            }
        }      
    });
var number = document.getElementsByClassName("number");
for (var i = 0; i < number.length; i++) {
    number[i].addEventListener('click', function () {
           if (output != NaN) {
   var output = reverseNumberFormat(getoutput());
              output = output + this.id;
            printOutput(output);
        }
    });
}