var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/text', function(req, res, next) {
		err = new Error('Post entry closed.');
		next(err);
		return ;
		res.render('post-form', {post_type: 'text' });
});

router.post('/text', function(req, res, next) {
		var text = req.body.text;
		var title = req.body.title;
		var fs = require('fs');
		var exec = require('child_process').exec;
		var execSync = require('child_process').execSync;
		fs.writeFileSync("./data/text/"+title+'.txt',text);
		execSync("dos2unix './data/text/"+title+".txt'");
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
		console.log('./utils/Textrank/main.py "./data/text/'+title+'.txt" "./data/cloud/'+title+'.json" "./data/tree/'+title+'.csv"');
		cmd = exec('python3 ./utils/Textrank/main.py "./data/text/'+title+'.txt" "./data/cloud/'+title+'.json" "./data/tree/'+title+'_t.csv"');
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
				execSync('python3 ./utils/trs.py "./data/tree/'+title+'_t.csv" "./data/tree/'+title+'.csv"');
		});
		res.redirect('/');
});

module.exports = router;
