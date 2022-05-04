$(document).ready(function() {
    
    //  Read in data
    let url = "static/data/samples.json";
    requestAjax(url);


    // EVENT LISTENERS
    $("#sel").on("change", function() {
        //DO WORK
        requestAjax(url);
    })

});

// AJAX request 
function requestAjax(url) {
    $.ajax({
        type: "GET",
        url: url,
        contentType: "application/json; charset=utf-8",
        success: function(data) {
            console.log(data);
            // ID
            getID(data);
            //make charts 
            getDataAndPlot(data);
        },
        error: function(textStatus, errorThrown) {
            console.log("FAILED to get data");
            console.log(textStatus);
            console.log(errorThrown);
        }
    });
}

//POPULATE ID DROPDOWN (Day 3, activity 4)
function getID(data) {
    var names= data.names;

    for (let i = 0; i < names.length; i++){
        let row = names[i];

        let html = `<option>${row}</option>`;

        $("#sel").append(html);
    }

    // var filter_ID = $("#sel").val();
    // var demographics = data.metadata.filter(x => x.filter_ID == filter_ID)[0]; //grab first value
    // $("#info")
}   
    

// 

// CHARTS
function getDataAndPlot(data) {
    console.log(data);

    // grab selected value
    //var filter_ID = $("#sel").val();
    var filter_ID = 1236

    // Horizontal Bar Chart    

        let sample = data.samples.filter(x => x.id == filter_ID).sort(function compareFunction(firstNum, secondNum) {
            return secondNum - firstNum;
          });;
        console.log(sample)

        //create list of top 10 OTUs

        let sample_values = sample.map(row => row.sample_values);

        let otu_ids= sample.map(row => row.otu_ids);
        let otu_labels= sample.map(row => row.otu_labels);
          console.log(otu_ids)

        //make plot
        horzBar(sample_values, otu_ids);
};






// Make Plotly items
function horzBar(sample_values, otu_ids) {
    var trace1 = {
        x: sample_values,
        y: otu_ids,
        name: 'Top 10 OTUs',
        type: 'bar',
        orientation: 'h'
    };

    var data = [trace1];

    var layout = { barmode: 'group', title: "Top 10 OTUs" };

    Plotly.newPlot('bar', data, layout) 
};