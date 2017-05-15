var Canvas = require("canvas");
var cloud = require("./d3-cloud");

module.exports = function (words,sizX,sizY,callback)
{
	var words = words.slice(0,10)
		.map(function(d) {
			console.log(">>>>",d[0],d[1]);
			return {text: d[0], size: 10 + d[1]};
		});
	console.log(">>>",sizX,sizY);
	cloud().size([sizX, sizY])
		.canvas(function() { return new Canvas(1, 1); })
		.words(words)
		.padding(5)
		.rotate(function() { return ~~((Math.random()) * 2) * 90; })
		.font("Impact")
		.fontSize(function(d) { return d.size; })
		.on("end",function(){callback(words);})
		.start();
}
