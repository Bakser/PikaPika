The 163 Chinese News Dataset 2011

---------------------------------------------------
1. DATA DESCRIPTION

We are happy to announce that the "163 Chinese News Dataset 2011" is now available for download. The dataset contains 13703 news articles crawled from news.163.com. Each article consists of a title, a summary and a set of keyphrases. The summaries and keyphrases are manually annotated by 163.com editors. To use this data, please follow the following guidelines:
   (1) For research only.  
   (2) Do not re-distribute.  
   (3) If you decide to use this work in your publication, please cite the following paper:
	  @inproceedings{liu2011conll, 
		  author = "Zhiyuan Liu and Xinxiong Chen and Yabin Zheng and Maosong Sun", 
		  title = "Automatic Keyphrase Extraction by Bridging Vocabulary Gap", 
		  booktitle = "Proceedings of The 15th Conference on Computational Natural Language Learning (CoNLL)",
		  year =  "2011",
	  }
---------------------------------------------------

2. DATA FORMAT

The data is recorded in Json format (http://json.org/), which is easy for humans to read and write. Each article contains the following fields:
-	date: the publication date of the article;
-	summary: The short summary of the article;
-	source: The URL of the article;;
-	id: The Unique ID of the article in this dataset;
-	content: The main body of the article;
-	title: The title of the article;
-	tags: The keyphrases of the article.

Here is an example of a record for a news article:

{"date":"2010-6-12 9:16:00","summary":"核心提示：据美国波士顿顾问集团的调查报告显示，2009年全球百万美元富豪数目增加14%，其中中国增加了31%，增速排全球第四位。","source":"http://news.163.com/10/0612/09/68VG9IS3000146BD.html","id":"7","content":"美国波士顿顾问集团最新的研究报告显示，香港百万美元富户占全港家庭总数的比例，名列全球第二\n中新网6月12日报道 据香港星岛日报报道，美国波士顿顾问集团最新的研究报告显示，香港百万美元富户占全港家庭总数的比例，名列全球第二。以家庭比例计算，香港是全世界百万美元富户密度最高的地区之一，去年的百万富户数目占全港家庭总数8.8%，仅次于经济竞争对手新加坡的11.4%。\n该集团表示，去年全世界百万富翁数目增加约14%，以新加坡及马来西亚为首，全球财富回复至金融危机前的水平。而全球财富增加了11.5%，资产管理规模上升至111.5万亿美元(约868.9万亿港元)，接近2007年纪录性的111.6万亿美元。\n全世界的百万美元富户数目，达到1120万户，其中美国拥有最多，共472万户。现时全球百万富户大约等于2007年底时的数目，2008年百万富户一度减少约14%，至980万户。去年新加坡百万富户数目增长最多，达35%，其次为马来西亚的33%，中国以31%排名第四位。\n","title":"报告称2009年中国百万美元富豪增加31%","timestamp":0,"resourceKey":"","userId":"","tags":["富户密集度","富豪"],"extras":""}
---------------------------------------------------

For more information, please visit: http://nlp.csai.tsinghua.edu.cn/~lzy
