//to be filled before use:
var apiUrl = '/api';
var etagPath = "/etag";
var jsonPath = '/json'

//clock
$(document).ready(function() {
	$('#bottom-left').simpleClock();
	getEtag();
	setInterval(getEtag, 0.1*60*1000); //call for changes every 5 min
	setInterval(rotator, 1000);
});

//global var helpers
var currentEtag = '';

var currentLeftTimer = 0;
var currentRightTimer = 0;
var currentNewsTimer = 0;

var currentLeft = {};
var currentRight = {};
var currentNews = {};

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
	//currentJson = {"left":[{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":5,"type":"video","content":{"source":"http://distribution.bbb3d.renderfarming.net/video/mp4/bbb_sunflower_1080p_60fps_normal.mp4","subtitles":""}},{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":15,"type":"www","content":{"source":"https://www.youtube.com/embed/ZY3J3Y_OU0w"}},{"since":"2018-04-10 22:00","until":"2019-04-11 22:00","duration":15,"type":"www","content":{"source":"https://www.tutorialspoint.com/index.htm"}}],"right":[{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":5,"source":"https://c1cleantechnicacom-wpengine.netdna-ssl.com/files/2018/02/Wind-Power-Birds.jpg"}],"news":[{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":15,"title":"Aaa, kotki jeden","content":"...szarobure obydwa czy coś tam jakoś tam coś.<br><br>BARDZO DUŻO TEKSTU TUTAJ...","important":0},{"since":"2018-04-10 22:00","until":"2019-04-10 22:00","duration":5,"title":"News2","content":"Lill news numero due","important":1}]}
	
	console.log(currentJson);
}

var leftN = 0;
var rightN = 0;
var newsN = 0;

function expired(since, to){
	var nowDate = new Date();
	var sinceDate = new Date(since);
	var toDate = new Date(to);
	if (nowDate > sinceDate && nowDate < toDate){
		return false;
	}else{
		return true;
	}
}

function rotator(){
	//checking weather to change or not to change (that is the question)
	//console.log('currentLeftTimer: ' + currentLeftTimer + ' / ' + Object(currentJson['left'][leftN]['duration']));
	console.log(JSON.stringify(currentJson['right'][rightN]['duration']));
	
	
	if(currentLeftTimer >= JSON.stringify(currentJson['left'][leftN]['duration'])){
		
		if(leftN >= Object.keys(currentJson['left']).length-1){
			leftN = 0;
		}
		else{
			leftN++;
		}
		while(expired(currentJson['left'][leftN]['since'],currentJson['left'][leftN]['until'])){
			if(leftN >= Object.keys(currentJson['left']).length-1){
				leftN = 0;
			}
			else{
				leftN++;
			}
		}
		console.log('rotator/changeLeft');
		$('#top-left').attr('src', Object(currentJson['left'][leftN]['content']['source'])); /*iframe src compatible only for now*/
		currentLeftTimer = 0;
	}
	if(currentRightTimer >= JSON.stringify(currentJson['right'][rightN]['duration'])){
		console.log(Object.keys(currentJson['right']).length);

		if(rightN >= Object.keys(currentJson['right']).length-1){
			rightN = 0;
		}
		else{
			rightN++;
		}
		while(expired(currentJson['right'][rightN]['since'],currentJson['right'][rightN]['until'])){
			if(rightN >= Object.keys(currentJson['right']).length-1){
				rightN = 0;
			}
			else{
				rightN++;
			}
		}
		console.log('rotator/changeRight');
		$('#top-right').attr('src', Object(currentJson['right'][rightN]['source']));
		currentRightTimer = 0;
	}
	if(currentNewsTimer >= JSON.stringify(currentJson['news'][newsN]['duration'])){

		if(newsN >= Object.keys(currentJson['news']).length-1){
			newsN = 0;
		}
		else{
			newsN++;
		}
		while(expired(currentJson['news'][newsN]['since'],currentJson['news'][newsN]['until'])){
			if(newsN >= Object.keys(currentJson['news']).length-1){
				newsN = 0;
			}
			else{
				newsN++;
			}
		}
		console.log('rotator/changeNews');
		$('#info-title').html(Object(currentJson['news'][newsN]['title']));
		$('#info-main').html(Object(currentJson['news'][newsN]['content']));
		currentNewsTimer = 0;
	}
	
	//adding to timers
	currentLeftTimer++;
	currentRightTimer++;
	currentNewsTimer++;
	console.log('tick');
}
