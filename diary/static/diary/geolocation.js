
function checkLocation(infoText) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                var request = new XMLHttpRequest();

                var APIkey = 'pk.bed5305a2a6bf4f89206a15ce7b08170';
                var url = 'https://eu1.locationiq.com/v1/reverse.php'
                    +'?key='+APIkey
                    +'&lat='+position.coords.latitude+'&lon='+position.coords.longitude
                    +'&format=json&postaladdress=1&normalizeaddress=1&zoom=18';

                /*var APIkey = 'AIzaSyBOIOzXhsIXYWNHe4DYxkkAzrhj3iOziyM';
                var url = 'https://maps.googleapis.com/maps/api/geocode/json'
                    +'?latlng='+position.coords.latitude+','+position.coords.longitude
                    +'&key='+APIkey;*/

                request.open('GET', url, true);
                request.onreadystatechange = function(){
                    if (request.readyState == 4 && request.status == 200){
                        var data = JSON.parse(request.responseText);
                        displayLocation(data, infoText);
                    }
                    else {
                        handleLocationError(true, infoText);
                    }
                };
                request.send();
            },
            () => { handleLocationError(true, infoText); }
        );
    }
    else {
        handleLocationError(false, infoText);
    }
}

function displayLocation(data, infoText) {
    //var address = data.results[0];
    //infoText.text = address.formatted_address;
    // road suburb city country | city_district locality state_district
    var address = data.address;
    var name = address.road ? address.road+', ' : '';
    //name += address.suburb ? address.suburb+', ' : '';
    name += address.city ? address.city+', ' : '';
    name += address.country ? address.country : '';
    infoText.innerHTML = name;
}

function handleLocationError(browserHasGeolocation, infoText) {
    infoText.innerHTML = browserHasGeolocation
        ? "Error: The Geolocation service failed."
        : "Error: Your browser doesn't support geolocation.";
}

window.onload = () => {
    var infoText = document.getElementById("location-text");
    var button = document.getElementById("location-button");
    button.addEventListener("click", () => {checkLocation(infoText)});
};
