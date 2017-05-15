var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/text', function(req, res, next) {
  res.render('post-form', {post_type: 'text' });
});

router.post('/text', function(req, res, next) {
	data = JSON.parse(req.body.data);
	console.log(data);
	res.end(data);
});

module.exports = router;
