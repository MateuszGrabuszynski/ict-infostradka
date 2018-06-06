//TODOS: 1) Adaptation to net loss
//       2) First run loading time

//to be filled before use:
apiUrl = '/v1/api';
jsonPath = '/display'

//dont mess with the stuff below though
//downloading json from API
function getJson(){
        console.log('inside getJson')
        currentJson = jQuery.getJSON(apiUrl + jsonPath);

        console.log(currentJson);
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
		console.log('puszczam');
		return false;
	}else{
		console.log('smierdzisz STARYM kapciem');
		return true;
	}
}

//helps to put best fit on first screen instead of waiting
function firstRun(){
	console.log('ruszylem jako pierwszy!');
	if(typeof currentJson.responseJSON != 'undefined'){
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
	}
}

function rotator(){
	if(typeof currentJson.responseJSON != 'undefined'){ //indentation retardo
//	console.log(currentLeftTimer);
//	console.log(JSON.stringify(currentJson['responseJSON']['left'][leftN]['duration']));
//	console.log(JSON.stringify(Number(currentJson['responseJSON']['left'][leftN]['duration'])));

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
				console.log('jestem madry!');
				console.log(leftN);
				console.log(Object.keys(currentJson['responseJSON']['left']).length-1);
				console.log('baaaardzo...');
			}
			else{
				leftN++;
			}
		}
		console.log('rotator/changeLeft');
		$('#top-left').attr('src', Object(currentJson['responseJSON']['left'][leftN]['content']['source'])); /*iframe src compatible only for now*/
		currentLeftTimer = 0;
	}
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
		console.log('rotator/changeRight');
		$('#top-right').attr('src', Object(currentJson['responseJSON']['right'][rightN]['content']['source']));
		currentRightTimer = 0;
	}
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
		console.log('rotator/changeNews');
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
	} //typeof if (the retardo one)
	
	//adding to timers
	currentLeftTimer++;
	currentRightTimer++;
	currentNewsTimer++;
	console.log('tick');
}


//clock
$(document).ready(function() {
        $('#bottom-left').simpleClock();
        setInterval(getJson, 100000); //call for changes every 5 min
        setInterval(rotator, 1000);
        getJson();
	firstRun();
});

