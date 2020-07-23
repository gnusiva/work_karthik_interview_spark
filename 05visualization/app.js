

function fetchData() {
    let currency = document.getElementById("dropdown").value;
    fetch('http://localhost:5000/exchangeData?currency=' + currency).then( resp => {
        resp.json().then( data => {
            // console.log(data);
            let mData = data.map( singlePoint => [ (new Date(singlePoint[0]).getTime()) , singlePoint[1] ]);
            renderChart(mData, currency);
        })
    });
}
