var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	var fs = require('fs');
	fs.readFile("./data/cloud.json","utf-8",function(err,data){
		if (err)
			console.log(err);
		console.log(data);
		data = JSON.parse(data);
		res.render('cloud',{"title":'Pikapika',"data":JSON.stringify(data),"board":{'height':960,'width':500}});
	});
});

module.exports = router;
