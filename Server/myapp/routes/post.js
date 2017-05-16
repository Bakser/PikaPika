var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/text', function(req, res, next) {
  res.render('post-form', {post_type: 'text' });
});

router.post('/text', function(req, res, next) {
		var text = req.body.text;
		var title = req.body.title;
		var fs = require('fs');
		fs.writeFileSync("./data/text/"+title,text);
		var list = JSON.parse(fs.readFileSync("./data/list.json",'utf-8'));
		var flag = false;
		console.log(JSON.stringify(list));
		for (var i=0;i<list.length;i++)
				if (list[i].title == title)
				{
						flag = true;
						list[i].status = "Computing..."
				}
		if (!flag)
				list = list.concat([{"title":title,"status":"Computing..."}]);
		console.log(JSON.stringify(list));
		fs.writeFileSync("./data/list.json",JSON.stringify(list));
		var exec = require('child_process').exec;
		console.log('./utils/Textrank/main.py ./data/text/'+title+' ./data/cloud/'+title+'.json ./data/tree/'+title+'.csv');
		cmd = exec('python3 ./utils/Textrank/main.py ./data/text/'+title+' ./data/cloud/'+title+'.json ./data/tree/'+title+'_t.csv');
		//cmd = exec('./utils/Textrank/main.py',['./data/text/'+title,'./data/cloud/'+title+'.json','./data/tree/'+title+'.csv']);
		cmd.stdout.on('data',function(data){
				console.log(data);
		});
		cmd.stderr.on('data',function(data){
				console.log(data);
		});
		cmd.on('close',function(code){
				console.log("Closed...")
						var list = JSON.parse(fs.readFileSync("./data/list.json",'utf-8'));
				for (var i=0;i<list.length;i++)
						if (list[i].title == title)
								list[i]['status'] = "Finish...";
				fs.writeFileSync("./data/list.json",JSON.stringify(list));
				var execSync = require('child_process').execSync;
				execSync('python3 ./utils/trs.py ./data/tree/'+title+'_t.csv ./data/tree/'+title+'.csv');
		});
		res.redirect('/');
});

module.exports = router;
