// from data.js
var tableData = data;
var tbody = d3.select("tbody")

// YOUR CODE HERE!
function createTable(data) {
    data.forEach((obj) => {
        var row = tbody.append("tr");
        Object.values(obj).forEach((value) => {
          var cell = row.append("td");
          cell.text(value);
        });
      });   
}

createTable(data);

var button = d3.select("#filter-btn");



// Create event handlers 
button.on("click", runEnter);



// Event handler 
function runEnter() {

    // Prior data removal
    tbody.html("");

    // Page prevention (refreshing)
    d3.event.preventDefault();

    // Input element and get the raw HTML node &  Property of the input element
    var inputElement = d3.select ("#datetime").property("value")
    var filterdata = data.filter(obj=> obj.datetime == inputElement)
    createTable(filterdata) 



    
} 