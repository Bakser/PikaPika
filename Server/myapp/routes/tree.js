var express = require('express');
var router = express.Router();
var path = require('path');

router.use(express.static(path.join(__dirname, '../data/tree')));

router.get('/', function(req, res, next) {
	console.log(res.query);
  res.render('tree', { title: req.query.title });
});

module.exports = router;
