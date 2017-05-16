var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
		var fs = require('fs');
		fs.readFile('./data/list.json','utf-8',function(err,data){
				if (err)console.log(err);
				var list = JSON.parse(data);
				console.log(list);
				res.render('index', { title: 'Pikapika',list : list});
		});
});

module.exports = router;
