function startTime() {
    var x = moment().format(Do MMMM YYYY)
	var today = new Date();
	
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
	var yr = today.getYear();
	var mn = today.getMonth();
	var dy = today.getDay();
	
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('time').innerHTML = x;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}