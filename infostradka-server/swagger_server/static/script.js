//TODOS: 1) Adaptation to net loss
//       2) First run loading time

//to be filled before use (only if necessary!):
apiUrl = '/v1/api';
jsonPath = '/display'

//dont mess with the stuff below though
//downloading json from API
function getJson(){
        //console.log('inside getJson')
        currentJson = jQuery.getJSON(apiUrl + jsonPath);
        //console.log(currentJson);
}

//global var helpers
currentLeftTimer = 0;
currentRightTimer = 0;
currentNewsTimer = 0;

leftN = 0;
rightN = 0;
newsN = 0;

function expired(since, to){
	var nowDate = new Date();
	var sinceDate = new Date(since);
	var toDate = new Date(to);
	if (nowDate > sinceDate && nowDate < toDate){
		//console.log('OK');
		return false;
	}else{
		//console.log('EXPIRED!');
		return true;
	}
}

//helps to put best fit on first screen instead of waiting (not really...)
function firstRun(){
	//if(typeof currentJson.responseJSON != 'undefined'){
		$('#top-left').attr('src', Object(currentJson['responseJSON']['left'][leftN]['content']['source']));
		$('#top-right').attr('src', Object(currentJson['responseJSON']['right'][rightN]['content']['source']));
		if(currentJson['responseJSON']['news'][newsN]['important'] == true){
                        $('#bottom-container').css('background-color', '#910000');
                }
                else{
                        $('#bottom-container').css('background-color', '#006991');
                }
                $('#info-title').html(Object(currentJson['responseJSON']['news'][newsN]['title']));
                $('#info-main').html(Object(currentJson['responseJSON']['news'][newsN]['content']));
	//}
}

function rotator(){
	if(typeof currentJson.responseJSON != 'undefined'){
		//left-rotator
		if(currentLeftTimer >= JSON.stringify(Number(currentJson['responseJSON']['left'][leftN]['duration']))){
			console.log('tu wlazlem');
			if(leftN >= Object.keys(currentJson['responseJSON']['left']).length-1){
				leftN = 0;
			}
			else{
				console.log('dlugosc ok')
				leftN++;
			}
			while(expired(currentJson['responseJSON']['left'][leftN]['since'],currentJson['responseJSON']['left'][leftN]['until'])){
				if(leftN >= Object.keys(currentJson['responseJSON']['left']).length-1){
					leftN = 0;
				}
				else{
					leftN++;
				}
			}
			console.log('rotator/changeLeft');
			if(currentJson['responseJSON']['left'][leftN]['type'] == "yt"){
				zlozony = 'https://www.youtube.com/embed/'+currentJson['responseJSON']['left'][leftN]['content']['source']+'?autoplay=1&frameborder="0"&rel=0&amp;controls=0&amp;showinfo=0';
				$('#top-left').attr('src', zlozony);
				$('#top-left').attr('allow', 'autoplay; encrypted media')
			}
			else if(currentJson['responseJSON']['left'][leftN]['type'] == "www"){
				$('#top-left').removeAttr('allow');
				$('#top-left').attr('src', Object(currentJson['responseJSON']['left'][leftN]['content']['source'])); /*iframe src compatible only for now*/
			}
			else{
				zlozony = "../static/files/"+currentJson['responseJSON']['left'][leftN]['content']['source'];
				$('#top-left').removeAttr('allow');
				$('#top-left').attr('src', zlozony);
			}
			currentLeftTimer = 0;
		}

		//right-rotator
		if(currentRightTimer >= JSON.stringify(Number(currentJson['responseJSON']['right'][rightN]['duration']))){
			console.log(Object.keys(currentJson['responseJSON']['right']).length);

			if(rightN >= Object.keys(currentJson['responseJSON']['right']).length-1){
				rightN = 0;
			}
			else{
				rightN++;
			}
			while(expired(currentJson['responseJSON']['right'][rightN]['since'],currentJson['responseJSON']['right'][rightN]['until'])){
				if(rightN >= Object.keys(currentJson['responseJSON']['right']).length-1){
					rightN = 0;
				}
				else{
					rightN++;
				}
			}
			//console.log('rotator/changeRight');
			if(currentJson['responseJSON']['right'][rightN]['type'] == "yt"){
				zlozony = 'https://www.youtube.com/embed/'+currentJson['responseJSON']['right'][rightN]['content']['source']+'?autoplay=1&frameborder="0"&rel=0&amp;controls=0&amp;showinfo=0';
				$('#top-right').attr('src', zlozony);
				$('#top-right').attr('allow', 'autoplay; encrypted media')
			}
			else if(currentJson['responseJSON']['right'][rightN]['type'] == "www"){
				$('#top-right').removeAttr('allow');
				$('#top-right').attr('src', Object(currentJson['responseJSON']['right'][rightN]['content']['source'])); /*iframe src compatible only for now*/
			}
			else{
				zlozony = "../static/files/"+currentJson['responseJSON']['right'][rightN]['content']['source'];
				$('#top-right').removeAttr('allow');
				$('#top-right').attr('src', zlozony);
			}
			currentRightTimer = 0;
		}

		//news-rotator
		if(currentNewsTimer >= JSON.stringify(Number(currentJson['responseJSON']['news'][newsN]['duration']))){
			if(newsN >= Object.keys(currentJson['responseJSON']['news']).length-1){
				newsN = 0;
			}
			else{
				newsN++;
			}
			while(expired(currentJson['responseJSON']['news'][newsN]['since'],currentJson['responseJSON']['news'][newsN]['until'])){
				if(newsN >= Object.keys(currentJson['responseJSON']['news']).length-1){
					newsN = 0;
				}
				else{
					newsN++;
				}
			}
			//console.log('rotator/changeNews');
			if(currentJson['responseJSON']['news'][newsN]['important'] == true){
				$('#bottom-container').css('background-color', '#910000');
			}
			else{
				$('#bottom-container').css('background-color', '#006991');
			}
			$('#info-title').html(Object(currentJson['responseJSON']['news'][newsN]['title']));
			$('#info-main').html(Object(currentJson['responseJSON']['news'][newsN]['content']));
			currentNewsTimer = 0;
		}
	}
	
	//adding to timers
	currentLeftTimer++;
	currentRightTimer++;
	currentNewsTimer++;
	//console.log('tick');
}


//clock
$(document).ready(function() {
        $('#bottom-left').simpleClock();
        setInterval(getJson, 300000); //check for changes every 5 min (5*60*1000 = 300000)
        setInterval(rotator, 1000);
        getJson();
	firstRun();
});

