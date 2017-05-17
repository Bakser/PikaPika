var express = require('express');
var router = express.Router();
var path = require('path');

router.use(express.static(path.join(__dirname, '../data/tree')));

router.get('/', function(req, res, next) {
		if (req.query.title == undefined)
		{
				res.render('plain',{title:'Tree',content:require('fs').readFileSync('./public/tree.txt')});
				return ;
		}
		console.log(res.query);
		var height = require('fs').readFileSync('./data/tree/'+req.query.title+'_t.csv','utf-8').split('\n').length * 20;
		var width = 1300;
		res.render('tree', { title: req.query.title ,height : height,width:width});
});

module.exports = router;
