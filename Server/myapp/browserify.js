var d3 = require("d3"),
	cloud = require("./utils/d3-cloud");

//var fill = d3.schemeCategory20();
var fill = d3.scaleOrdinal(d3.schemeCategory20);

var layout = cloud()
	.size([500, 500])
	.words(
		JSON.parse(document.getElementById('wordlist').innerHTML)
		.map(function(d) {
			return {text: d[0], size: 10 + d[1], test: "haha"};
		}))
	.padding(1)
	.rotate(function() { return ~~((Math.random()-.5) * 7) * 20; })
	.font("Impact")
	.fontSize(function(d) { return d.size; })
	.on("end", draw);
layout.start();

function draw(words) {
	d3.select(".svg-point").append("svg")
		.attr("width", layout.size()[0])
		.attr("height", layout.size()[1])
		.append("g")
		.attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
		.selectAll("text")
		.data(words)
		.enter().append("text")
		.style("font-size", function(d) { return d.size + "px"; })
		.style("font-family", "Impact")
		.style("fill", function(d, i) { return fill(i); })
		.attr("text-anchor", "middle")
		.attr("transform", function(d) {
			return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
		})
		.text(function(d) { return d.text; });
}
