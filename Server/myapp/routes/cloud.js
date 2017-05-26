var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
		title = req.query.title;
		if (title == undefined)
		{
				res.render('plain',{'title':'Word Cloud','content':require('fs').readFileSync('./public/cloud.txt')});
				return ;
		}
		var fs = require('fs');
		fs.readFile("./data/cloud/"+title+".json","utf-8",function(err,data){
				if (err)
						console.log(err);
				else{

				console.log(data);
				data = JSON.parse(data)
						.sort(function(a,b){return b[1]-a[1];}) 
						.slice(0,250);
				res.render('cloud',{"title":title,"data":JSON.stringify(data),"board":{'height':960,'width':500}});
				}
		});
});

module.exports = router;
