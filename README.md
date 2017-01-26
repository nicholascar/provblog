# ProvBlog
This is the source code for ProvBlog,m the provenance blog, which you can find at http://provblog.org. 

Individual posts can be found in the posts directory.

It is a Python Flask app, hosted on a specialised Flask hosting service: http://pythonanywhere.com. 

### Licensing,  copyright and attribution
This site's code and all the textual content are licensed for reuse under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license. If you'd like to republish this material, please do the best attribution job you can and please, if possible, be [PROV-O](https://www.w3.org/TR/prov-o/)-compliant! For example, if referring to the post "The Start" (the first blog post on this site) on some other website, please provide a hyperlink to the posts' persistent URI ([http://provblog.org/post/2017-01-26-The-Start](http://provblog.org/post/2017-01-26-The-Start)), marked up with [RDFa](https://rdfa.info/):

```
<div 
  xmlns:prov="hhttp://www.w3.org/ns/prov#"
  resource="{YOUR_REPUBLICATIONS_URI}" 
  typeof="prov:Entity">
     <a 
       property="prov:wasDerivedFrom"
       href="http://provblog.org/post/2017-01-26-The-Start">
         YOUR_REPUBLICATIONS_TITLE
     </a>
</div>
```
RDFa for attribution of works, quotations etc. are all demonstrated at [https://www.w3.org/2011/prov/wiki/PROV-O_as_RDFa]. 

If you're really keen, you could try and send me a pingback! See this site for descriptions of pingbacks.

### Author and contact

Nicholas Car  
nick@kurrawong.net  
http://github.com/nicholascar  
