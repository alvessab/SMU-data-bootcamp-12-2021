// Store our API endpoint as queryUrl.
//var queryUrl = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2021-01-01&endtime=2021-01-02&maxlongitude=-69.52148437&minlongitude=-123.83789062&maxlatitude=48.74894534&minlatitude=25.16517337";

$(document).ready(function() {
    doWork();

    // Event Listener
    $("#filter").on("click", function() {
        doWork();
    });
});

function doWork() {
    var time = $("#time").val();

    var url = `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_${time}.geojson`;

    // clear out the old map 
    $("#map-container").empty();
    $("#map-container").append('<div id="map" style="height:700px"></div>');

    requestAjax(url);
}


function requestAjax(url) {
    $.ajax({
        type: "GET",
        url: url,
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            console.log(data);
            createMap(data);
        },
        error: function(textStatus, errorThrown) {
            console.log("FAILED to get data");
            console.log(textStatus);
            console.log(errorThrown);
        }
    });
}

//Pop up Information
function onEachFeature(feature, layer) {
    if (feature.properties) {
        layer.bindPopup(`<h3>${ feature.properties.title }</h3><hr><p>${new Date(feature.properties.time)}</p >`);
    }
}



// 3.
// createMap() takes the earthquake data and incorporates it into the visualization:

function createMap(data) {


    // get earthquake data
    var earthquakes = data.features;

    // layers
    var dark_layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/dark-v10',
        accessToken: API_KEY
    });

    var light_layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/light-v10',
        accessToken: API_KEY
    });

    var street_layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/streets-v11',
        accessToken: API_KEY
    });

    var outdoors_layer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/outdoors-v11',
        accessToken: API_KEY
    });


    // Create an overlays object.
    var earthquakeLayer = L.geoJSON(earthquakes, {
        onEachFeature: onEachFeature
    });

    //Create circle overlay option
    var circles= [] //declare variable
    for (let i = 0; i< earthquakes.length; i++) {
        let earthquake = earthquakes[i];

        let location = [earthquake.geometry.coordinates[1], earthquake.geometry.coordinates[0]]
        let mag = earthquake.properties.mag

    //avoid records without magnitude, which is present in last month and last week data
        let circle= L.circle(location, {
            fillOpacity: 0.75,
            color: getColor(mag),
            fillColor: getColor(mag),
            radius: getRadius(mag)
            }).bindPopup(`<h3>${ earthquake.properties.title }</h3><hr><p>${new Date(earthquake.properties.time)}</p >`);
    
            //add to variables
            circles.push(circle)
        
      }


    //function to determine marker radius
      function getRadius(mag){
          return Math.sqrt(mag) * 100000
          }
        
      
    //function to determine marker color
    function getColor(mag) {
        let color = "red"
    
      if (mag <= 1){
        color = '#12c42c';
      }else if (mag <= 3) {
        color = '#929f00';
      } else if (mag <= 5) {
        color = '#b98000';
      } else if (mag <= 7) {
        color = '#c86d00';
      } else if (mag <= 9) {
        color = '#dc4000';
      } else if (mag > 9) {
        color = '#e11c1c';
      } 
      
        return(color);
    }

    // Create an overlays object (without geojson)
    var magnitudeLayer = L.layerGroup(circles);

    // add legend



    // Create a baseMaps object.
    var baseMaps = {
        "Dark": dark_layer,
        "Light": light_layer,
        "Street": street_layer,
        "Outdoors": outdoors_layer
    };

    // Overlays that can be toggled on or off
    var overlayMaps = {
        Earthquake: earthquakeLayer,
        Magnitude: magnitudeLayer
    };

    // Create a new map.
    // Edit the code to add the earthquake data to the layers.
    var myMap = L.map("map", {
        center: [
            34.09, 3.058756
        ],
        zoom: 2,
        layers: [dark_layer, magnitudeLayer]
    });

    // Create a layer control that contains our baseMaps.
    // Be sure to add an overlay Layer that contains the earthquake GeoJSON.
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);

}