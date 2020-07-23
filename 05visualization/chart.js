function renderChart(seriesData, currency) {
    Highcharts.chart('container', {

        title: {
            text: 'Exchange Currency'
        },
    
        subtitle: {
            text: ''
        },
    
        yAxis: {
            title: {
                text: 'Currency'
            }
        },
    
        xAxis: {
            type: 'datetime',
            accessibility: {
                rangeDescription: 'Range: 2018 to 2020'
            }
        },
    
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },
    
        plotOptions: {
            series: {
                label: {
                    connectorAllowed: false
                },
                pointStart: 2010
            }
        },
    
        series: [{
            name: currency,
            data: seriesData
        }],
    
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }
    
    });
}
