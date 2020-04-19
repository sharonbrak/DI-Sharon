
function myAge(p) {
    var mumage = 2*p;
    var dadage = 1.2*mumage;
    var goodmumage = mumage.toFixed(0)
    var gooddadage = dadage.toFixed(0)
    console.log(goodmumage);
    console.log(gooddadage);
}
myAge(36);