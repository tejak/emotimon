$( document ).ready(function() {


    // For extracting date info from JSON
    function getDate(dateString) {
	return new Date(dateString).getTime();
    }
    
    // For x-axes of all graphs
    var dayOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"];
    
    function heartGraph() {
	// Defining days of the week
	
	$.getJSON("/emotimon/watch/data/heart", function(data) {
	    var d1 = [];
	    $.each( data.data, function( dataId, plotData ) {
		plotData[0] = getDate(plotData[0]);
		d1.push(plotData);
	    });

	    // Customizing graph
	    var options = {
		grid: {
		    markings: [
                        {xaxis: { from: 0, to: 6 },color: "#C11B17"},
                        {xaxis: { from: 6, to: 100},color: "#FDD017"}]
                },
            

		axisLabels: {
		    show: true
		},
		xaxes: [
		    {
			mode: "time",
			tickFormatter: function (val, axis) {                                    
                            return new Date(val).getHours();                 
			},  
			timeformat: "%m/%d %H:%M",
			tickSize: [1, "hour"],
			color: "black",        
			axisLabel: "Time (Hours)",
			axisLabelUseCanvas: true,
			axisLabelFontSizePixels: 12,
			axisLabelFontFamily: 'Verdana, Arial',
			axisLabelPadding: 10
		    }],
		yaxes: [{
		    position: 'left',
		    axisLabel: 'Heartbeat (Beats per minute)',
		    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 10
		}]
	    };
	    
	    
	    $.plot($("#heartGraph"), [d1], options);
	});
    };

    function heartGraphDay() {
	$.getJSON("/emotimon/watch/data/heart", function(data) {
	    var d1 = [];
	    $.each( data.data, function( dataId, plotData ) {
		curr = new Date(plotData[0]);
                plotData[0] = curr.getHours()*3600 + curr.getMinutes()*60 + curr.getSeconds();
		d1.push(plotData);
	    });
            $.plot($("#heartGraphDay"), [d1], {
                series: {
              	    points: {
                      radius: 3,
                      show: true,
                      fill: true,
                      fillColor: "#058DC7"
                    },
                    color: "#058DC7"
                }, axisLabels: {
                    show: true
                },
                xaxes: [
                    {
                        axisLabel: "Time (Seconds staring 12 AM ending 11:59 PM)",
                        axisLabelUseCanvas: true,
                        axisLabelFontSizePixels: 12,
                        axisLabelFontFamily: 'Verdana, Arial',
                        axisLabelPadding: 10
                    }],
                yaxes: [{
                    position: 'left',
                    axisLabel: 'Heartbeat (Beats per minute)',
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 10
                }]

            });
       });
    };

    function watchAccGraph() {
	$.getJSON("/emotimon/watch/data/acc", function(data) {
	    var dx = [];
	    var dy = [];
	    var dz = [];
	    $.each( data.data, function( dataId, plotData ) {
		dx.push([getDate(plotData[0]),plotData[1]]);
		dy.push([getDate(plotData[0]),plotData[2]]);
		dz.push([getDate(plotData[0]),plotData[3]]);
	    });
	    acc_data = [{ data:dx, label:"x-axis", lines:{show:true}},
			{ data:dy, label:"y-axis", lines:{show:true}},
			{ data:dz, label:"z-axis", lines:{show:true}}];
	    
	    var options = {
                grid: {
		    markings: [
                        {xaxis: { from: 0, to: 6 },color: "#C11B17"},
                        {xaxis: { from: 6, to: 100},color: "#FDD017"}]
                },
		
		
                axisLabels: {
		    show: true
                },
                xaxes: [
		    {
                        mode: "time",
                        tickFormatter: function (val, axis) {
			    return dayOfWeek[new Date(val).getDay()];
                        },
                        timeformat: "%m/%d %H:%M",
                        tickSize: [1, "day"],
                        color: "black",
                        axisLabel: "Time (Day of the Week)",
                        axisLabelUseCanvas: true,
                        axisLabelFontSizePixels: 12,
                        axisLabelFontFamily: 'Verdana, Arial',
                        axisLabelPadding: 10
		    }],
		yaxes: [{
                    position: 'left',
		    axisLabel: 'Acceleration (m/sec^2)',
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 10
                }]
            };
		
	    $.plot($("#watchAccGraph"), acc_data, options);
	});
    };
    
    function watchAccGraphDay() {
	$.getJSON("/emotimon/watch/data/acc", function(data) {
	    var dx = [];
	    var dy = [];
	    var dz = [];
	    $.each( data.data, function( dataId, plotData ) {
		curr = new Date(plotData[0]);
                plotData[0] = curr.getHours()*3600 + curr.getMinutes()*60 + curr.getSeconds();
		dx.push([plotData[0],plotData[1]]);
		dy.push([plotData[0],plotData[2]]);
		dz.push([plotData[0],plotData[3]]);
	    });
	    acc_data = [{ data:dx, label:"x-axis", color:"#FFCC66", points: {fill: true, fillcolor:"#FFCC66"}},
			{ data:dy, label:"y-axis", color:"#66CCFF", points: {fill: true, fillcolor:"#66CCFF"}},
			{ data:dz, label:"z-axis", color:"#CC6666", points: {fill: true, fillcolor:"#CC6666"}}];
            $.plot($("#watchAccGraphDay"), acc_data, {
                series: {
              	    points: {
                      radius: 3,
                      show: true,
                      fill: true,
                      //fillColor: "#058DC7"
                    },
                   // color: "#058DC7"
                },


                axisLabels: {
                    show: true
                },
                xaxes: [
                    {
                        axisLabel: "Time (Seconds staring 12 AM ending 11:59 PM)",
                        axisLabelUseCanvas: true,
                        axisLabelFontSizePixels: 12,
                        axisLabelFontFamily: 'Verdana, Arial',
                        axisLabelPadding: 10
                    }],
                yaxes: [{
                    position: 'left',
                    axisLabel: 'Acceleration (m/sec^2)',
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 10
                }]

            });
       });
    };
    
    function micGraph() {
	// Defining days of the week
	
	$.getJSON("/emotimon/phone/data/mic", function(data) {
	    var d1 = [];
	    $.each( data.data, function( dataId, plotData ) {
		plotData[0] = getDate(plotData[0]);
		d1.push(plotData);
	    });

	    // Customizing graph
	    var options = {
		grid: {
		    markings: [
                        {xaxis: { from: 0, to: 6 },color: "#C11B17"},
                        {xaxis: { from: 6, to: 100},color: "#FDD017"}]
                },
            

		axisLabels: {
		    show: true
		},
		xaxes: [
		    {
			mode: "time",
			tickFormatter: function (val, axis) {                                    
			    return dayOfWeek[new Date(val).getDay()];
			},  
			timeformat: "%m/%d %H:%M",
			tickSize: [1, "day"],
			color: "black",        
			axisLabel: "Time (Day of the Week)",
			axisLabelUseCanvas: true,
			axisLabelFontSizePixels: 12,
			axisLabelFontFamily: 'Verdana, Arial',
			axisLabelPadding: 10
		    }],
		yaxes: [{
		    position: 'left',
		    axisLabel: 'Decibels',
		    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 10
		}]
	    };
	    
	    
	    $.plot($("#micGraph"), [d1], options);
	});
    };
    
    function micGraphDay() {
	$.getJSON("/emotimon/phone/data/mic", function(data) {
	    var d1 = [];
	    $.each( data.data, function( dataId, plotData ) {
		curr = new Date(plotData[0]);
                plotData[0] = curr.getHours()*3600 + curr.getMinutes()*60 + curr.getSeconds();
		d1.push(plotData);
	    });
            $.plot($("#micGraphDay"), [d1], {
                series: {
              	    points: {
                      radius: 3,
                      show: true,
                      fill: true,
                      fillColor: "#058DC7"
                    },
                    color: "#058DC7"
                },


                axisLabels: {
                    show: true
                },
                xaxes: [
                    {
                        axisLabel: "Time (Seconds staring 12 AM ending 11:59 PM)",
                        axisLabelUseCanvas: true,
                        axisLabelFontSizePixels: 12,
                        axisLabelFontFamily: 'Verdana, Arial',
                        axisLabelPadding: 10
                    }],
                yaxes: [{
                    position: 'left',
                    axisLabel: 'Decibels',
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 10
                }]

            });
       });
    };

    function accGraph() {
	$.getJSON("/emotimon/phone/data/acc", function(data) {
	    var dx = [];
	    var dy = [];
	    var dz = [];
	    $.each( data.data, function( dataId, plotData ) {
		dx.push([getDate(plotData[0]),plotData[1]]);
		dy.push([getDate(plotData[0]),plotData[2]]);
		dz.push([getDate(plotData[0]),plotData[3]]);
	    });
	    acc_data = [{ data:dx, label:"pitch (x-axis rotation)", lines:{show:true}},
			{ data:dy, label:"roll (y-axis rotation)", lines:{show:true}},
			{ data:dz, label:"azimuth (z-axis rotation)", lines:{show:true}}];
	    
	    var options = {
                grid: {
		    markings: [
                        {xaxis: { from: 0, to: 6 },color: "#C11B17"},
                        {xaxis: { from: 6, to: 100},color: "#FDD017"}]
                },
		
		
                axisLabels: {
		    show: true
                },
                xaxes: [
		    {
                        mode: "time",
                        tickFormatter: function (val, axis) {
			    return dayOfWeek[new Date(val).getDay()];
                        },
                        timeformat: "%m/%d %H:%M",
                        tickSize: [1, "day"],
                        color: "black",
                        axisLabel: "Time(Day of the Week)",
                        axisLabelUseCanvas: true,
                        axisLabelFontSizePixels: 12,
                        axisLabelFontFamily: 'Verdana, Arial',
                        axisLabelPadding: 10
		    }],
		yaxes: [{
                    position: 'left',
		    axisLabel: 'Angle (degrees)',
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 10
                }]
            };
		
	    $.plot($("#accGraph"), acc_data, options);
	});
    };
    
    function accGraphDay() {
	$.getJSON("/emotimon/phone/data/acc", function(data) {
	    var dx = [];
	    var dy = [];
	    var dz = [];
	    $.each( data.data, function( dataId, plotData ) {
		curr = new Date(plotData[0]);
                plotData[0] = curr.getHours()*3600 + curr.getMinutes()*60 + curr.getSeconds();
		dx.push([plotData[0],plotData[1]]);
		dy.push([plotData[0],plotData[2]]);
		dz.push([plotData[0],plotData[3]]);
	    });
	    acc_data = [{ data:dx, label:"pitch (x-axis rotation)", color:"#FFCC66", points: {fill: true, fillcolor:"#FFCC66"}},
			{ data:dy, label:"roll (y-axis rotation)", color:"#66CCFF", points: {fill: true, fillcolor:"#66CCFF"}},
			{ data:dz, label:"azimuth (z-axis rotation)", color:"#CC6666", points: {fill: true, fillcolor:"#CC6666"}}];
            $.plot($("#accGraphDay"), acc_data, {
                series: {
              	    points: {
                      radius: 3,
                      show: true,
                      fill: true,
                      //fillColor: "#058DC7"
                    },
                   // color: "#058DC7"
                },


                axisLabels: {
                    show: true
                },
                xaxes: [
                    {
                        axisLabel: "Time (Seconds staring 12 AM ending 11:59 PM)",
                        axisLabelUseCanvas: true,
                        axisLabelFontSizePixels: 12,
                        axisLabelFontFamily: 'Verdana, Arial',
                        axisLabelPadding: 10
                    }],
                yaxes: [{
                    position: 'left',
                    axisLabel: 'Angle (degrees)',
                    axisLabelFontSizePixels: 12,
                    axisLabelFontFamily: 'Verdana, Arial',
                    axisLabelPadding: 10
                }]

            });
       });
    };
    
    micGraph();
    micGraphDay();    
   
    accGraph();
    accGraphDay();    
    
    heartGraph();    
    heartGraphDay();

    watchAccGraph();
    watchAccGraphDay();    
});

