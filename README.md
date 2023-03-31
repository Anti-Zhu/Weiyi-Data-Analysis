# -
项目是作者的课程作业，算是第一次简单的Python数据分析经历。  
基于Python的第三方库pyppeteer和pyquery对“微医”（https://www.wedoctor.com）中的医生信息按照各二级科室进行了爬取，然后对数据进行了分析。受限于网站的后台，医生列表页只能查看到第38页，39页以后的数据无法访问，因此各二级科室至多只能获取到608条的医生信息，数据截至2022年12月1日，共35439条。  
思路完全按照狗熊会人才计划作品平台型互联网医院医生问诊量影响因素研究（https://mp.weixin.qq.com/s/IRrpyLvv5_Qgbv0k1sNlbA）进行，算是进行了一次复现。  
差别在于本文的数据量更大，而且是从二级科室展开的研究，而狗熊会的作品是从一级科室展开的研究，两者做出来的结果其实差别比较大。  
数据集放在了项目中，但在爬取的时候就按照微医网站给出的二级科室对网站中1存储的医生信息中的二级科室信息进行了替换。此外，对于医生可能会出现在多个二级科室中这种情况，本文的处理是直接去重保留第一条数据。  
希望能够提供一个思路，帮助您做出更好的作品。
