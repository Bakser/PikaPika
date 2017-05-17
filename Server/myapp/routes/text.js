var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
		var fs = require('fs');
		fs.readFile('../data/text/'+req.query.title,'utf-8',function(err,data){
				console.log(err);
				res.render('plain', { title: req.query.title, content : data});
		});
});

module.exports = router;
