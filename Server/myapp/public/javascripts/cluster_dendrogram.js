var svg = d3.select("svg"),
	width = +svg.attr("width"),
	height = +svg.attr("height"),
	g = svg.append("g").attr("transform", "translate(300,0)");


var stratify = d3.stratify()
	.parentId(function(d) { return d.parentid; });

d3.csv('/tree/'+document.getElementById('infopath').innerHTML+'_t.csv', function(error, data) {
	if (error) throw error;

	var mxdepth = 0;

	root = stratify(data).sort(function(a, b) {return a.id - b.id; });


	d3.cluster().size([height,root.height*200])(root);

	var link = g.selectAll(".link")
		.data(root.descendants().slice(1))
		.enter().append("path")
		.attr("class", function(d){ return d.children?"link":"link-leaf";})
		.attr("d", function(d) {
			if (!d.children)
				return "M" + d.y + "," + d.x
					+ "C" + (d.parent.y + 100) + "," + d.x
					+ " " + (d.parent.y + 100) + "," + (d.x+d.parent.x)/2
					+ " " + d.parent.y + "," + d.parent.x;
			else
				return "M" + d.y + "," + d.x
					+ "C" + (d.parent.y + 100) + "," + d.x
					+ " " + (d.parent.y + 100) + "," + d.parent.x
					+ " " + d.parent.y + "," + d.parent.x;
		});

	var node = g.selectAll(".node")
		.data(root.descendants())
		.enter().append("g")
		.attr("class", function(d) { return "node" + (d.children ? " node--internal" : " node--leaf"); })
		.attr("transform", function(d) { return d.children?
				"translate(" + d.y + "," + d.x + ")" :
				"translate(" + d.y + "," + d.x + ")"; });

	node.append("circle")
		.attr("r", 2.5);

	node.append("text")
		.style('font-size',13)
		.attr("dy", 3)
		.attr("x", function(d) { return d.children ? -8 : 8; })
		.style("text-anchor", function(d) { return d.children ? "end" : "start"; })
		.text(function(d) {return d.data.text });
});

