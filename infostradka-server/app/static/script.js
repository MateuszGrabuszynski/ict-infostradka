//to be filled before use:
var apiUrl = '';
var etagPath = "/etag";
var jsonPath = '/api'

//clock
$(document).ready(function() {
	$('#bottom-left').simpleClock();
	getEtag();
	setInterval(getEtag, 60*1000); //call for changes every 1 min
	setInterval(rotator, 1000);
});

//global var helpers
var currentEtag = '';

var currentLeftTimer = 0;
var currentRightTimer = 0;
var currentNewsTimer = 0;

var currentJson = {};

//downloading etag from API
function getEtag(){
	console.log('inside getEtag');
	var downloadedEtag = 'barbra?'
	//var downloadedEtag = jQuery.get(apiUrl + etagPath);
	if (currentEtag != downloadedEtag){
		getJson();
	}
}

//downloading json from API
function getJson(){
	console.log('inside getJson')
	currentJson = jQuery.getJSON(apiUrl + jsonPath);
	
	//console.log(currentJson);
}

var leftN = 0;
var rightN = 0;
var newsN = 0;

function rotator(){
	//checking weather to change or not to change (that is the question)
	//console.log('currentLeftTimer: ' + currentLeftTimer + ' / ' + Object(currentJson['left'][leftN]['duration']));
	//console.log(currentJson['responseJSON']['right'][rightN]['duration']);
	date = new Date()
	now = date.getTime()
	
	/*niby miało robić since/until
	while(
	(now <= JSON.stringify(currentJson['responseJSON']['left'][leftN]['since'])) || (now >= JSON.stringify(currentJson['responseJSON']['left'][leftN]['until']))
	){
		console.log('lewy rotator napotkał element spoza zakresu czasowego')
		leftN++;
	}*/
	if(currentLeftTimer >= JSON.stringify(currentJson['responseJSON']['left'][leftN]['duration'])){
		//console.log('leftN: ' + leftN);
		if(leftN >= Object.keys(currentJson['responseJSON']['left']).length-1){
			leftN = 0;
		}
		else{
			leftN++;
		}
		console.log('rotator/changeLeft');
		$('#top-left').attr('src', Object(currentJson['responseJSON']['left'][leftN]['content']['source'])); /*iframe src compatible only for now*/
		currentLeftTimer = 0;
	}
	
	if(currentRightTimer >= JSON.stringify(currentJson['responseJSON']['right'][rightN]['duration'])){
		//console.log(Object.keys(currentJson['responseJSON']['right']).length);
		if(rightN >= Object.keys(currentJson['responseJSON']['right']).length-1){
			rightN = 0;
		}
		else{
			rightN++;
		}
		console.log('rotator/changeRight');
		$('#top-right').attr('src', Object(currentJson['responseJSON']['right'][rightN]['source']));
		currentRightTimer = 0;
	}
	if(currentNewsTimer >= JSON.stringify(currentJson['responseJSON']['news'][newsN]['duration'])){
		if(newsN >= Object.keys(currentJson['responseJSON']['news']).length-1){
			newsN = 0;
		}
		else{
			newsN++;
		}
		console.log('rotator/changeNews');
		if(currentJson['responseJSON']['news'][newsN]['important']){
			$('#bottom-container').css('background-color', '#910000');
		}
		else{
			$('#bottom-container').css('background-color', '#006991');
		}
		$('#info-title').html(Object(currentJson['responseJSON']['news'][newsN]['title']));
		$('#info-main').html(Object(currentJson['responseJSON']['news'][newsN]['content']));
		currentNewsTimer = 0;
	}
	
	//adding to timers
	currentLeftTimer++;
	currentRightTimer++;
	currentNewsTimer++;
	console.log('tick');
}