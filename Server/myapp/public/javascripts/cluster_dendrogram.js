var svg = d3.select("svg"),
	width = +svg.attr("width"),
	height = +svg.attr("height"),
	g = svg.append("g").attr("transform", "translate(200,0)");

var tree = d3.cluster()
	.size([height, width - 360]);

var stratify = d3.stratify()
	.parentId(function(d) { return d.parentid; });


d3.csv("flare2.csv", function(error, data) {
	if (error) throw error;

	var root = stratify(data)
		.sort(function(a, b) { return (a.height - b.height) || a.id.localeCompare(b.id); });

	tree(root);

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
		.attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

	node.append("circle")
		.attr("r", 2.5);

	node.append("text")
		.attr("dy", 3)
		.attr("x", function(d) { return d.children ? -8 : 8; })
		.style("text-anchor", function(d) { return d.children ? "end" : "start"; })
		.text(function(d) {return d.data.text });
});

