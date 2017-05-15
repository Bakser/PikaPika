var gen = require('./cloud-gen');
gen(['abc','cba','asd','das','asdasd','asdasdas'],100,100,end);
function end(a)
{
	console.log(a);
}
