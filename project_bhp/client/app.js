function getBathValue(){
    var uiBathrooms = document.getElementsByName("uiBathrooms");
    for(var i in uiBathrooms){
        if(uiBathrooms[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1; // invalid value
}

function getBedroomValue(){
    var uiBed = document.getElementsByName("uiBHK");
    for(var i in uiBHK){
        if(uiBHK[i].checked){
            return parseInt(i)+1;
        }
    }
    return -1; // invalid value
}

function onClickedEstimatePrice(){
    
}

function onPageLoad(){
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data,status){
        console.log("got response for get_location_names request");
        if(data){
            var locations = data.locations;
            var uilocations = document.getElementById("uiLocations");
            $('#uiLocations').empty();
            for(var i in locations){
                var opt = new Option(locations[i]);
                $('#uiLocations').append(opt);
            }
        }
    }
    );

}

window.onload = onPageLoad;