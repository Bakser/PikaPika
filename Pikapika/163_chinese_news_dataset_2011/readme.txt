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

{"date":"2010-6-12 9:16:00","summary":"������ʾ����������ʿ�ٹ��ʼ��ŵĵ��鱨����ʾ��2009��ȫ�������Ԫ������Ŀ����14%�������й�������31%��������ȫ�����λ��","source":"http://news.163.com/10/0612/09/68VG9IS3000146BD.html","id":"7","content":"������ʿ�ٹ��ʼ������µ��о�������ʾ����۰�����Ԫ����ռȫ�ۼ�ͥ�����ı���������ȫ��ڶ�\n������6��12�ձ��� ������ǵ��ձ�������������ʿ�ٹ��ʼ������µ��о�������ʾ����۰�����Ԫ����ռȫ�ۼ�ͥ�����ı���������ȫ��ڶ����Լ�ͥ�������㣬�����ȫ���������Ԫ�����ܶ���ߵĵ���֮һ��ȥ��İ��򸻻���Ŀռȫ�ۼ�ͥ����8.8%�������ھ��þ��������¼��µ�11.4%��\n�ü��ű�ʾ��ȥ��ȫ�����������Ŀ����Լ14%�����¼��¼���������Ϊ�ף�ȫ��Ƹ��ظ�������Σ��ǰ��ˮƽ����ȫ��Ƹ�������11.5%���ʲ������ģ������111.5������Ԫ(Լ868.9���ڸ�Ԫ)���ӽ�2007���¼�Ե�111.6������Ԫ��\nȫ����İ�����Ԫ������Ŀ���ﵽ1120�򻧣���������ӵ����࣬��472�򻧡���ʱȫ����򸻻���Լ����2007���ʱ����Ŀ��2008����򸻻�һ�ȼ���Լ14%����980�򻧡�ȥ���¼��°��򸻻���Ŀ������࣬��35%�����Ϊ�������ǵ�33%���й���31%��������λ��\n","title":"�����2009���й�������Ԫ��������31%","timestamp":0,"resourceKey":"","userId":"","tags":["�����ܼ���","����"],"extras":""}
---------------------------------------------------

For more information, please visit: http://nlp.csai.tsinghua.edu.cn/~lzy
