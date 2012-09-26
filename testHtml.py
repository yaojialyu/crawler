# coding:utf8

testHtml = '''






<!DOCTYPE HTML>
<html lang="zh-CN" class="ua-linux ua-webkit">
<head>
<meta charset="UTF-8">
<meta content="提供图书、电影、音乐唱片的推荐、评论和价格比较，以及城市独特的文化生活。" name="description">
<title>豆瓣</title>
<script>
window.Douban=window.Douban||{};var Do=function(){Do.actions.push([].slice.call(arguments))};Do.ready=function(){Do.actions.push([].slice.call(arguments))};Do.add=Do.define=function(a,b){Do.mods[a]=b};Do.global=function(){Do.global.mods=Array.prototype.concat(Do.global.mods,[].slice.call(arguments))};Do.global.mods=[];Do.mods={};Do.actions=[];function set_cookie(g,f,d,e){var b=new Date(),a,c;b.setTime(b.getTime()+((f||30)*24*60*60*1000));a="; expires="+b.toGMTString();for(c in g){document.cookie=c+"="+g[c]+a+"; domain="+(d||"douban.com")+"; path="+(e||"/")}}function get_cookie(b){var e=b+"=",a=document.cookie.split(";"),d,f;for(d=0;d<a.length;d++){f=a[d];while(f.charAt(0)==" "){f=f.substring(1,f.length)}if(f.indexOf(e)===0){return f.substring(e.length,f.length).replace(/\"/g,"")}}return null}Douban.init_show_login=function(a){Do("dialog",function(){var b="/j/misc/login_form";dui.Dialog({title:"登录",url:b,width:/device-mobile/i.test(document.documentElement.className)?document.documentElement.offsetWidth*0.9:350,cache:true,callback:function(c,d){d.node.addClass("dialog-login");d.node.find("h2").css("display","none");d.node.find(".hd h3").replaceWith(d.node.find(".bd h3"));d.node.find("form").css({border:"none",width:"auto",padding:"0"});d.update()}}).open()})};Do(function(){$.ajax_withck=function(a){if(a.type=="POST"){a.data=$.extend(a.data||{},{ck:get_cookie("ck")})}return $.ajax(a)};$.postJSON_withck=function(a,b,c){$.post_withck(a,b,c,"json")};$.post_withck=function(a,c,d,b){if($.isFunction(c)){b=d;d=c;c={}}return $.ajax({type:"POST",url:a,data:$.extend(c,{ck:get_cookie("ck")}),success:d,dataType:b||"text"})};$("html").click(function(c){var a=$(c.target),b=a.attr("class");if(!b){return}$(b.match(/a_(\w+)/gi)).each($.proxy(function(d,f){var e=Douban[f.replace(/^a_/,"init_")];if(typeof e==="function"){c.preventDefault();e.call(this,c)}},a[0]))})});
    Do.add('dialog', {path: 'http://img3.douban.com/js/ui/packed_dialog429925323.js', type: 'js', requires: ['http://img3.douban.com/css/ui/packed_dialog4563741467.css']});
    Do.global('http://img3.douban.com/js/sns/fp/packed_base6505908882.js', 'dialog');
</script>
<link rel="stylesheet" href="http://img3.douban.com/css/core/packed__init_8673671899.css">
<link rel="stylesheet" href="http://img3.douban.com/css/sns/fp/packed__init_3814380766.css">
<link rel="stylesheet" href="http://img3.douban.com/css/sns/packed_boutique3347530513.css">
<style>
h1 { display:none; }
.site-nav-items li { position:relative; }
.site-nav-items .tips-overly { top:35px; }
.side .enter { position:relative;margin: 0 0 20px;padding:5px 15px;background:#ebf8f9; }
.enter h2 { margin-bottom:0;line-height:2.2;color:#333;font-size:13px;font-weight:800; }
.enter .text { line-height:1.62;margin:0; }
.enter .lnk-close { position:absolute;top:5px;right:5px;padding:0 2px;line-height:1;  }
.enter .lnk-close:link,
.enter .lnk-close:visited { color:#ccc; }
.enter .lnk-close:hover,
.enter .lnk-close:active { color:#fff;background-color:#ccc; }

.site-nav { margin-bottom: 6px }

.tips-overly{position:absolute;z-index:99;width:320px;top:0;left:0;background:#fff;border:1px solid #bfddb7}.tips-overly .tips-bd{padding:12px 15px;color:#333;line-height:1.62}.tips-overly h2{margin-bottom:6px;font-size:12px;font-weight:800;color:#333}.tips-overly p{margin:0 0 12px 0}.tips-overly .lnk-bn{display:inline-block;*display:inline;zoom:1;padding:2px 8px;line-height:1.4;font-size:12px}.tips-overly a.lnk-bn:link,.tips-overly a.lnk-bn:visited{color:#fff;background-color:#4aac66;font-size:12px}.tips-overly a.lnk-bn:hover,.tips-overly a.lnk-bn:active{color:#fff;background-color:#4dc36f;font-size:12px}.back-old{padding-bottom:5px;text-align:right;margin-top:-24px;zoom:1;_margin-top:0}.back-old .lnk-back-old:link{color:#bbb}.back-old .lnk-back-old:hover{background:#bbb;color:#fff}.tips-overly .tips-hd{position:absolute;top:-6px;top:-8px\9;left:8px;background:#fff;width:10px;height:10px;overflow:hidden;line-height:10em;border-left:1px solid #bfddb7;border-top:1px solid #bfddb7;zoom:1;-webkit-transform:rotate(45deg);-moz-transform:rotate(45deg);-o-transform:rotate(45deg);transform:rotate(45deg);filter:progid:DXImageTransform.Microsoft.Matrix(M11=0.707,M12=-0.707,M21=0.707,M22=0.707,sizingMethod=\'auto expand\')}
</style>
<style type="text/css">
.suggest-overlay{position:absolute;z-index:10001;width:auto;background:#fff;border:1px solid #c5c7d2;-moz-border-radius:3px;-webkit-border-radius:3px;border-radius:3px}.suggest-overlay .bd{min-width:220px;line-height:1;background:#fafafa;color:#b3b3b3;padding:5px;-moz-border-radius:3px;-webkit-border-radius:3px;border-radius:3px}.suggest-overlay ul{color:#333;padding:3px 0;min-width:214px}.suggest-overlay li{margin:0;padding:0}.suggest-overlay li b{font-weight:bold}.suggest-overlay li span{color:#999}.suggest-overlay img{margin-right:5px;width:20px;height:20px;vertical-align:middle}.suggest-overlay li.on{background:#e9f0f8}.suggest-overlay li a{display:block;padding:3px 7px;color:#333}.suggest-overlay li a:hover,.suggest-overlay li a:focus,.suggest-overlay li a:active{outline:0;color:#333;background:0;background:#e9f0f8}

    .boutique{margin-bottom:40px}.boutique h2{color:#40834a;font-weight:bold;position:relative;margin:0 0 5px 0;font-size:16px}.boutique .lnk-close{position:absolute;right:0;top:9px;outline:0;width:10px;height:10px;background:url(http://img3.douban.com/pics/boutique_close.gif) top right no-repeat;_filter:expression(document.execCommand("BackgroundImageCache",false,true))}.boutique .book-showcase{background:#f7fbf7;border:1px solid #e2eee2;padding:25px 30px}.boutique .book-showcase ul{font-size:0;letter-spacing:-4px;word-spacing:-4px}.boutique .book-list{margin-left:-35px}.boutique .book-list .item{width:174px;padding-left:35px;vertical-align:top;display:inline-block;*display:inline;*zoom:1;letter-spacing:normal;word-spacing:normal}.boutique .book-list .cover{float:left;_margin-right:-3px}.boutique .book-list .buy-btn{margin-top:6px}.boutique .book-list .info{overflow:hidden;_zoom:1;padding-left:10px;font-size:12px}.boutique .book-list .title a{color:#333;outline:0}.boutique .book-list .title a:hover{background:0;color:#000}.boutique .book-list .author{color:#666}.boutique .book-list .status{color:#73aed1}.buy-btn a{color:#589c66;background:#d1e5d4;border:1px solid #bad9bf;font-size:12px;padding:0 8px;display:inline-block;*display:inline;*zoom:1;letter-spacing:normal;word-spacing:normal;border-radius:2px;-moz-border-radius:2px;-webkit-border-radius:2px;outline:0}.buy-btn a:active,.buy-btn a:link,.buy-btn a:visited{color:#589c66;background:#d1e5d4;border:1px solid #bad9bf}.buy-btn a:hover{color:#589c66;border:1px solid #bad9bf;background:#deede0}.buy-btn a i{font-style:normal;font-weight:normal}
  
.notify-mod { clear:both;margin:0 0 20px;padding:12px 0;background:#f5f4f6;line-height:1.2;overflow:hidden;text-align:center; }

.mobile-app-entrance { overflow: hidden; }
.mobile-app-entrance .entrance-link { display: block; position: relative; padding: 10px; height: 50px; margin-top: 10px; -webkit-border-radius: 5px; -moz-border-radius: 5px; border-radius: 5px; }
.mobile-app-entrance .entrance-link.first-link { margin-top: 0; }
.mobile-app-entrance .entrance-link,
.mobile-app-entrance .entrance-link:link,
.mobile-app-entrance .entrance-link:visited,
.mobile-app-entrance .entrance-link:active,
.mobile-app-entrance .entrance-link:hover { background: #f1f1f1 url("http://img3.douban.com/pics/app/arrw.png") no-repeat scroll 97% 50%; outline: none; color: #4e4e4e; }
.mobile-app-entrance .app-icon { width: 50px; height: 50px; float: left; margin-right: 13px; background: url("http://img1.douban.com/pics/app/app_icons_50.1.png") no-repeat; -webkit-border-radius: 10px; -moz-border-radius: 10px; border-radius: 10px; -webkit-box-shadow: 1px 1px 2px #999; -moz-box-shadow: 1px 1px 2px #999; box-shadow: 1px 1px 2px #999; }
.mobile-app-entrance .main-title,
.mobile-app-entrance .sub-title { display: block; }
.mobile-app-entrance .main-title { color: #204d92; font-size: 16px; font-weight: bold; line-height: 1; padding-top: 9px; }
.mobile-app-entrance .app-list { background: #f1f1f1; padding: 14px 21px 8px; font-size: 0; }
.mobile-app-entrance .app-list .app-item { display: inline-block; *display: inline; *zoom: 1; width: 50px; margin-right: 25px; }
.mobile-app-entrance .app-item .app-link { display: block; text-align: center; color: #4e4e4e; font-size: 12px; }
.mobile-app-entrance .app-item .app-link:hover { background: transparent; color: #4e4e4e; }
.mobile-app-entrance .app-item .app-icon { margin-right: none; float: none; display: block; margin: 0 0 8px 0; }

/* SNS Index */
.mobile-app-entrance.app-main .entrance-link { background-image: none; height: 57px; padding: 15px 15px 15px 21px; -webkit-border-radius: 0; -moz-border-radius: 0; border-radius: 0; }
.mobile-app-entrance.app-main .main-title { font-size: 18px; padding-top: 10px; }
.mobile-app-entrance.app-main .sub-title { font-size: 14px; }
.mobile-app-entrance.app-main .app-icon { width: 72px; height: 58px; background: url("http://img3.douban.com/pics/app/mobile_app_icon.png") no-repeat; float: right; -webkit-border-radius: 0; -moz-border-radius: 0; border-radius: 0; -webkit-box-shadow: none; -moz-box-shadow: none; box-shadow: none; }

/* Update */
.mobile-app-entrance.app-update { margin-top: 20px; }

/* Movie */
.mobile-app-entrance.app-movie { margin-top: 20px; }

/* App Icons */
.mobile-app-entrance .app-icon.icon-read { background-position: 0 0; }
.mobile-app-entrance .app-icon.icon-update { background-position: 0 -150px; }
.mobile-app-entrance .app-icon.icon-fm { background-position: 0 -250px; }
.mobile-app-entrance .app-icon.icon-fm-ipad { background-position: 0 -300px; }
.mobile-app-entrance .app-icon.icon-movie { background-position: 0 -350px; }
.mobile-app-entrance .app-icon.icon-artists { background-position: 0 -50px; }
.mobile-app-entrance .app-icon.icon-cart { background-position: 0 -200px; }
.mobile-app-entrance .app-icon.icon-location { background-position: 0 -100px; }
.mobile-app-entrance .app-icon.icon-read-notes { background-position: 0 -400px; }
.mobile-app-entrance .app-icon.icon-online { background-position: 0 -450px; }
</style>
</head>

<body>
<link rel="prerender" href="http://www.douban.com/update"/>




<div class="top-nav">
  <div class="bd">
    






<div class="top-nav-info">
    
    <!-- _performtips_ -->
    <a href="http://www.douban.com/doumail/">豆邮</a>
    <a target="_blank" href="http://www.douban.com/accounts/">行之的帐号</a>
    <a href="http://www.douban.com/accounts/logout?ck=38ij">退出</a>
</div>


    <div class="top-nav-items">
        <ul>
                
                    
                    <li class="on">
                    <a href="http://www.douban.com/">豆瓣社区</a>
                    </li>
                
                    
                    <li>
                    <a href="http://book.douban.com/">豆瓣读书</a>
                    </li>
                
                    
                    <li>
                    <a href="http://movie.douban.com/">豆瓣电影</a>
                    </li>
                
                    
                    <li>
                    <a href="http://music.douban.com/">豆瓣音乐</a>
                    </li>
                
                    
                    <li>
                    <a href="http://www.douban.com/location/">豆瓣同城</a>
                    </li>
                
                    
                    <li>
                    <a href="http://douban.fm/" target="_blank">豆瓣FM</a>
                    </li>
                
                    <li class="top-nav-more">
                        <div class="top-nav-more-items">
                            <a href="#more" class="more">更多 <span class="arrow">&nbsp;</span>&nbsp;</a>
                            <ul>
                            
                            <li><a href="http://9.douban.com" target="_blank">九点</a></li>
                            
                            <li><a href="http://alphatown.com" target="_blank">阿尔法城</a></li>
                            
                            <li><a href="http://www.douban.com/mobile/" target="_blank">移动应用</a></li>
                            </ul>
                        </div>
                    </li>
        </ul>
    </div>
  </div>
</div>



<div id="wrapper">
<div id="header">






<div id="db-nav-main" class="site-nav">
    <div class="site-nav-logo">
        <a href="http://www.douban.com"><img src="http://img1.douban.com/pics/nav/lg_main_a10.png" alt="豆瓣"></a>
    </div>
    <div class="bd">
    <div class="nav-srh">
        <form name="ssform" method="get" action="http://www.douban.com/search">
            <div class="inp">
                <span><input id="search_text" name="search_text" type="text" title="成员、小组、音乐人、主办方" size="22" maxlength="60" value=""/></span>
                <span><input class="bn-srh" type="submit" value="搜索"/></span>
            </div>
        </form>
        
    </div>
    <div class="site-nav-items nav-logged-in">
     <ul>
      <li><a href="http://www.douban.com/">首页</a></li>
          <li><a href="http://www.douban.com/update/">友邻广播</a></li>
          <li><a href="http://www.douban.com/mine/">我的豆瓣</a></li>
          <li><a href="http://www.douban.com/group/">小组</a>
          </li>
          <li><a href="http://www.douban.com/site/">小站</a></li>
      <li style="position:relative;"><a href="http://www.douban.com/tribe/">部落</a><img style="top:6px;left:2.2em;position:absolute;" src="http://img3.douban.com/pics/new_menu.gif"></li>
     </ul>
    </div>
    </div>
    <div class="ext"></div>
</div>







</div>


<div id="bd">
    <h1>行之，新版豆瓣猜</h1>
    <div class="main">
        












  <div class="boutique">
    <h2>豆瓣小卖部<a class="lnk-close"></a></h2>
    
<div class="book-showcase">
  <ul class="book-list">
    

  
  <li class="item">
    <div class="cover">
      <a href="/shop/33207866/" class="pic" target="_blank">
        <img src="http://img3.douban.com/view/ark_article_cover/cut/public/89814.jpg?v=1343891567.0" width="56px" height="80px" alt="幻影之痛 封面" />
      </a>
    </div>
    <div class="info">
      <div class="title">
        <a href="/shop/33207866/" target="_blank">
          幻影之痛
        </a>
      </div>
      <div class="author">〔美〕莉迪娅·皮尔</div>
      <div class="status">
        美国 外国文学
      </div>
      <div class="buy-btn">
        <a href="/shop/33207866/" target="_blank">
            <i>&yen;</i> 1.99
        </a>
      </div>
    </div>
  </li>

    

  
  <li class="item">
    <div class="cover">
      <a href="/shop/33207867/" class="pic" target="_blank">
        <img src="http://img3.douban.com/view/ark_article_cover/cut/public/277532.jpg?v=1346809439.0" width="56px" height="80px" alt="两分铜币 封面" />
      </a>
    </div>
    <div class="info">
      <div class="title">
        <a href="/shop/33207867/" target="_blank">
          两分铜币
        </a>
      </div>
      <div class="author">〔日〕江户川乱步</div>
      <div class="status">
        新上架
      </div>
      <div class="buy-btn">
        <a href="/shop/33207867/" target="_blank">
            <i>&yen;</i> 7.00
        </a>
      </div>
    </div>
  </li>

    

  
  <li class="item">
    <div class="cover">
      <a href="/shop/33207865/" class="pic" target="_blank">
        <img src="http://img3.douban.com/view/ark_article_cover/cut/public/283379.jpg?v=1346652526.0" width="56px" height="80px" alt="山海境界·苦春 封面" />
      </a>
    </div>
    <div class="info">
      <div class="title">
        <a href="/shop/33207865/" target="_blank">
          山海境界·苦春
        </a>
      </div>
      <div class="author">厄梵</div>
      <div class="status">
        207 人试读
      </div>
      <div class="buy-btn">
        <a href="/shop/33207865/" target="_blank">
            <i>&yen;</i> 1.99
        </a>
      </div>
    </div>
  </li>

  </ul>
</div>

  </div>
  
  


        <div class="guess-list">
            
    
        
        <span class="section-state">刚刚更新</span>

        <h2>全站热点</h2>
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/5374383/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-5374383', section:'all_hot', row:0, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="我的黑色小礼服" src="http://img3.douban.com/lpic/s6389625.jpg">
        </div>

    <div class="title">
        <h3>我的黑色小礼服</h3>
            <span class="artist">导演: 许仁茂</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.1</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/10731595/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-10731595', section:'all_hot', row:0, index:1, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="Moonrise Kingdom" src="http://img3.douban.com/lpic/s9086567.jpg">
        </div>

    <div class="title">
        <h3>Moonrise Kingdom</h3>
            <span class="artist">表演者: Various Artists</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>9.4</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/10541180/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-10541180', section:'all_hot', row:0, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="フジテレビ系ドラマ「リーガル・ハイ」オリジナルサウンドトラック" src="http://img1.douban.com/lpic/s10413922.jpg">
        </div>

    <div class="title">
        <h3>フジテレビ系ドラマ「リーガル・ハイ」オリジナルサウンドトラック</h3>
            <span class="artist">表演者: 林ゆうき</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.3</b>
                </div>
    </div>



</a>
  </div>

              </div>
              
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/4836985/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-4836985', section:'all_hot', row:1, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="我们都为比尔着盛装" src="http://img3.douban.com/lpic/s4615415.jpg">
        </div>

    <div class="title">
        <h3>我们都为比尔着盛装</h3>
            <span class="artist">导演: 理查德·普莱斯</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>9.0</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item">
        <a hidefocus href="http://www.douban.com/note/237366885/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1015-237366885', section:'all_hot', row:1, index:1, random_key:'13484688338ddb6db1'})">
    


    <div class="title">
        <h3>情绪低落期可以试试的食物列表</h3>
            <div class="source">
                    雲生 的日记
            </div>
    </div>


      <div class="desc">
          <div class="inner">回帖之前请看完这七条谢谢！！！！！<span class="br"></span>1、列表是本人备份用，我没责任考虑到别的人怎样。欢迎大家归纳各自身体喜爱的食物。<span class="br"></span>2、入选条目都是经过...</div>
      </div>

</a>
    
    <div class="fav-btn">
                <a data-tkind="1015" data-tid="237366885" href="http://www.douban.com/note/237366885/" >1697 <i>&hearts;</i></a>
    </div>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/11599756/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-11599756', section:'all_hot', row:1, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="&gt;Album Title Goes Here&lt;" src="http://img3.douban.com/lpic/s11195045.jpg">
        </div>

    <div class="title">
        <h3>&gt;Album Title Goes Here&lt;</h3>
            <span class="artist">表演者: Deadmau5</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.3</b>
                </div>
    </div>



</a>
  </div>

              </div>
              
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/19898339/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-19898339', section:'all_hot', row:2, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="Magpies On Fire / Victorian Machinery - Single" src="http://img3.douban.com/lpic/s11368945.jpg">
        </div>

    <div class="title">
        <h3>Magpies On Fire / Victorian Machinery - Single</h3>
            <span class="artist">表演者: Red Hot Chili Peppers</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.5</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/6791675/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-6791675', section:'all_hot', row:2, index:1, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="日本列岛 动物物语" src="http://img3.douban.com/lpic/s6938735.jpg">
        </div>

    <div class="title">
        <h3>日本列岛 动物物语</h3>
            <span class="artist"></span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.6</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://book.douban.com/subject/11589941/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1001-11589941', section:'all_hot', row:2, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1001">
                <img alt="皮克斯：关于童心、勇气、创意和传奇" src="http://img1.douban.com/lpic/s11195863.jpg">
        </div>

    <div class="title">
        <h3>皮克斯：关于童心、勇气、创意和传奇</h3>
            <span class="artist">作者: [美]比尔•卡波达戈利,琳恩•杰克逊</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.8</b>
                </div>
    </div>



</a>
  </div>

              </div>
              
        

        <h2>猜你喜欢的音乐</h2>
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/10604934/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-10604934', section:'music_guess', row:3, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="你" src="http://img1.douban.com/lpic/s9063071.jpg">
        </div>

    <div class="title">
        <h3>你</h3>
            <span class="artist">表演者: 曹轩宾</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.8</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/11620718/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-11620718', section:'music_guess', row:3, index:1, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="天才与尘埃" src="http://img1.douban.com/lpic/s11241291.jpg">
        </div>

    <div class="title">
        <h3>天才与尘埃</h3>
            <span class="artist">表演者: 李泉</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.6</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/10828214/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-10828214', section:'music_guess', row:3, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="Observator" src="http://img3.douban.com/lpic/s10414245.jpg">
        </div>

    <div class="title">
        <h3>Observator</h3>
            <span class="artist">表演者: The Raveonettes</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.8</b>
                </div>
    </div>



</a>
  </div>

              </div>
              
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/10809706/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-10809706', section:'music_guess', row:4, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="Beacon" src="http://img1.douban.com/lpic/s10420230.jpg">
        </div>

    <div class="title">
        <h3>Beacon</h3>
            <span class="artist">表演者: Two Door Cinema Club</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.7</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/19928786/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-19928786', section:'music_guess', row:4, index:1, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="The Truth About Love (Deluxe Edition)" src="http://img1.douban.com/lpic/s11424600.jpg">
        </div>

    <div class="title">
        <h3>The Truth About Love (Deluxe Edition)</h3>
            <span class="artist">表演者: 粉红佳人 P!nk</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.4</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://music.douban.com/subject/14329294/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1003-14329294', section:'music_guess', row:4, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1003">
                <img height="90" alt="战马" src="http://img1.douban.com/lpic/s16792011.jpg">
        </div>

    <div class="title">
        <h3>战马</h3>
            <span class="artist">表演者: 铁骑 Tengger Cavalry</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.0</b>
                </div>
    </div>



</a>
  </div>

              </div>
              
        

        <h2>猜你喜欢的图书</h2>
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://book.douban.com/subject/11605940/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1001-11605940', section:'book_guess', row:5, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1001">
                <img alt="倒转红轮" src="http://img1.douban.com/lpic/s11317174.jpg">
        </div>

    <div class="title">
        <h3>倒转红轮</h3>
            <span class="artist">作者: 金雁</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>9.4</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://book.douban.com/subject/10570061/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1001-10570061', section:'book_guess', row:5, index:1, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1001">
                <img alt="他乡:寻找生活的坐标(单向街004)" src="http://img5.douban.com/lpic/s9021709.jpg">
        </div>

    <div class="title">
        <h3>他乡:寻找生活的坐标(单向街004)</h3>
            <span class="artist">作者: 郭玉洁 编</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.3</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://book.douban.com/subject/7153418/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1001-7153418', section:'book_guess', row:5, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1001">
                <img alt="富士山禁恋" src="http://img3.douban.com/lpic/s11089947.jpg">
        </div>

    <div class="title">
        <h3>富士山禁恋</h3>
            <span class="artist">作者: (日)松本清张</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.2</b>
                </div>
    </div>



</a>
  </div>

              </div>
              
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://book.douban.com/subject/11577232/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1001-11577232', section:'book_guess', row:6, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1001">
                <img alt="社会心理学（插图第7版）" src="http://img1.douban.com/lpic/s11161973.jpg">
        </div>

    <div class="title">
        <h3>社会心理学（插图第7版）</h3>
            <span class="artist">作者: 埃利奥特·阿伦森（Elliot Aronson),蒂姆·威尔逊（Tim Wilson)...</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>9.0</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://book.douban.com/subject/11588782/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1001-11588782', section:'book_guess', row:6, index:1, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1001">
                <img alt="愤怒的城堡" src="http://img1.douban.com/lpic/s11171912.jpg">
        </div>

    <div class="title">
        <h3>愤怒的城堡</h3>
            <span class="artist">作者: （意）亚历山德罗•巴里科</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.8</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://book.douban.com/subject/19899834/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1001-19899834', section:'book_guess', row:6, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1001">
                <img alt="只愿你曾被这世界温柔相待" src="http://img1.douban.com/lpic/s16240274.jpg">
        </div>

    <div class="title">
        <h3>只愿你曾被这世界温柔相待</h3>
            <span class="artist">作者: 水木丁</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.6</b>
                </div>
    </div>



</a>
  </div>

              </div>
              
        

        <h2>猜你喜欢的电影</h2>
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/3395373/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-3395373', section:'movie_guess', row:7, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="蝙蝠侠：黑暗骑士崛起" src="http://img1.douban.com/lpic/s9127643.jpg">
        </div>

    <div class="title">
        <h3>蝙蝠侠：黑暗骑士崛起</h3>
            <span class="artist">导演: 克里斯托弗·诺兰</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.4</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/4086853/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-4086853', section:'movie_guess', row:7, index:1, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="忧郁症" src="http://img1.douban.com/lpic/s6886464.jpg">
        </div>

    <div class="title">
        <h3>忧郁症</h3>
            <span class="artist">导演: 拉斯·冯·提尔</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>6.7</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/2999913/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-2999913', section:'movie_guess', row:7, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="保罗" src="http://img1.douban.com/lpic/s4540021.jpg">
        </div>

    <div class="title">
        <h3>保罗</h3>
            <span class="artist">导演: 格雷格·莫托拉</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>7.5</b>
                </div>
    </div>



</a>
  </div>

              </div>
              
              <div class="section">
              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/5964718/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-5964718', section:'movie_guess', row:8, index:0, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="纳德和西敏：一次别离" src="http://img3.douban.com/lpic/s7006217.jpg">
        </div>

    <div class="title">
        <h3>纳德和西敏：一次别离</h3>
            <span class="artist">导演: 阿斯哈·法哈蒂 </span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>8.8</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/10597950/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-10597950', section:'movie_guess', row:8, index:1, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="大西洋帝国 第三季" src="http://img3.douban.com/lpic/s11181738.jpg">
        </div>

    <div class="title">
        <h3>大西洋帝国 第三季</h3>
            <span class="artist">导演: 蒂莫西·范·帕腾</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9733;&#9734;</span><b>9.4</b>
                </div>
    </div>



</a>
  </div>

              
    

    <div class="guess-item item-subject">
        <a hidefocus href="http://movie.douban.com/subject/5028536/" class="item" target="_blank" 
            onclick="moreurl(this,{newguess:'1002-5028536', section:'movie_guess', row:8, index:2, random_key:'13484688338ddb6db1'})">
    

        
        <div class="pic pic-1002">
                <img alt="哥伦比亚人" src="http://img3.douban.com/lpic/s6329217.jpg">
        </div>

    <div class="title">
        <h3>哥伦比亚人</h3>
            <span class="artist">导演: 奥利维尔·米加顿</span>
            
                
                <div class="rating">
                  <span class="rating-stars rating-star4">&#9733;&#9733;&#9733;&#9734;&#9734;</span><b>6.8</b>
                </div>
    </div>



</a>
  </div>

              </div>
              

        </div>
    </div>
    <div class="side">
        
    
    <div class="back-old"><a href="" class="lnk-back-old">&gt;回旧版</a></div>

    

<div class="notify-mod">
    <a href="/subject/explore">发现喜欢的东西</a>
</div>

    




    
    <div id="db-reply-notify" class="mod">
    









    </div>

        
<div class="mod" id="db-online-events">
    <div class="hd">
            <span class="func">
                <a class="bn-create" href="http://www.douban.com/online/create"><span>创建线上活动</span></a>
            </span>
        
    <h2>
        线上活动
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                    <a href="http://www.douban.com/online/?g=d">更多</a>
                ) </span>
    </h2>

    </div>
    <div class="bd">
        
        
        
<ul class="clearbox">
        <li class="block clearfix">
            <div class="title">
                <a href="http://www.douban.com/online/11283986/">截图，猜电影，交朋友</a>
            </div>
            <div class="desc">
                时间：9月12日 - 11月30日
                <br><span class="num">3765人参加</span>
            </div>
        </li>
        <li class="block clearfix">
            <div class="title">
                <a href="http://www.douban.com/online/11295506/">我最中意的专辑封面</a>
            </div>
            <div class="desc">
                时间：9月22日 - 11月22日
                <br><span class="num">108人参加</span>
            </div>
        </li>
        <li class="block clearfix">
            <div class="title">
                <a href="http://www.douban.com/online/11207051/">你最喜爱哪对银幕情侣~!?</a>
            </div>
            <div class="desc">
                时间：7月25日 - 9月30日
                <br><span class="num">2226人参加</span>
            </div>
        </li>
        <li class="block clearfix">
            <div class="title">
                <a href="http://www.douban.com/online/11294214/">截吻图，猜电影</a>
            </div>
            <div class="desc">
                时间：9月21日 - 10月21日
                <br><span class="num">43人参加</span>
            </div>
        </li>
        <li class="block clearfix">
            <div class="title">
                <a href="http://www.douban.com/online/11187632/">晒晒各位做的美食吧~</a>
            </div>
            <div class="desc">
                时间：9月22日 - 11月30日
                <br><span class="num">1536人参加</span>
            </div>
        </li>
        <li class="block clearfix">
            <div class="title">
                <a href="http://www.douban.com/online/11296111/">晒晒你的爪~~</a>
            </div>
            <div class="desc">
                时间：9月23日 - 10月23日
                <br><span class="num">130人参加</span>
            </div>
        </li>
        <li class="block clearfix">
            <div class="title">
                <a href="http://www.douban.com/online/11291375/">晒合照 感谢那些曾陪我走过一段旅程的你</a>
            </div>
            <div class="desc">
                时间：9月19日 - 11月19日
                <br><span class="num">1543人参加</span>
            </div>
        </li>
        <li class="block clearfix">
            <div class="title">
                <a href="http://www.douban.com/online/11296061/">晒出你最喜欢的3/4/5...人组！</a>
            </div>
            <div class="desc">
                时间：9月23日 - 11月30日
                <br><span class="num">35人参加</span>
            </div>
        </li>
        <li class="block clearfix">
          <div id="dale_homepage_online_activity_promo_1"></div>
        </li>
        <li class="block clearfix">
          <div id="dale_homepage_online_activity_promo_2"></div>
        </li>
</ul>

        
    </div>
</div>

        <div class="mod">
            

<div id="db-sites">
    <div class="hd">
        
    <h2>
        发现小组
            &nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;&nbsp;&middot;
            <span class="pl">&nbsp;(
                    <a href="http://www.douban.com/explore/group">更多</a>
                ) </span>
    </h2>

    </div>
    <div class="bd">
        <div class="content">
            
        <div class="item">
            <div class="pic">
                <a href="http://www.douban.com/group/231101/">
                    <img src="http://img3.douban.com/icon/g231101-1.jpg" alt="我只是偶尔抽疯" width="48" height="48" />
                </a>
            </div>
            <div class="info">
                <h3><a href="http://www.douban.com/group/231101/">我只是偶尔抽疯</a></h3>
                5000成员
            </div>
        </div>
        <div class="item">
            <div class="pic">
                <a href="http://www.douban.com/group/fractal/">
                    <img src="http://img3.douban.com/icon/g72141-1.jpg" alt="大自然的分形几何学" width="48" height="48" />
                </a>
            </div>
            <div class="info">
                <h3><a href="http://www.douban.com/group/fractal/">大自然的分形几何学</a></h3>
                1668成员
            </div>
        </div>
        <div class="item">
            <div class="pic">
                <a href="http://www.douban.com/group/twohours/">
                    <img src="http://img3.douban.com/icon/g188367-2.jpg" alt="和当地人时差2小时" width="48" height="48" />
                </a>
            </div>
            <div class="info">
                <h3><a href="http://www.douban.com/group/twohours/">和当地人时差2小时</a></h3>
                2736成员
            </div>
        </div>
        <div class="item">
            <div class="pic">
                <a href="http://www.douban.com/group/PedalFreaks/">
                    <img src="http://img3.douban.com/icon/g78881-28.jpg" alt="Pedal Freaks" width="48" height="48" />
                </a>
            </div>
            <div class="info">
                <h3><a href="http://www.douban.com/group/PedalFreaks/">Pedal Freaks</a></h3>
                1741成员
            </div>
        </div>

        </div>
    </div>
</div>

        </div>
       <!-- douban app begin -->
       





<div class="mobile-app-entrance block5 app-main">

    <a class="entrance-link first-link" href="http://www.douban.com/mobile/">
        <span class="app-icon icon-main"></span>
        <span class="main-title">豆瓣移动应用</span>
        <span class="sub-title">点击下载</span>
    </a>
</div>

       <!-- douban app end -->
    </div>
</div>

<div id="ft">


<span id="icp" class="fleft gray-link">
    &copy; 2005－2012 douban.com, all rights reserved
  <br />
  <a href="http://www.miibeian.gov.cn/">京ICP证090015号</a>&nbsp;&nbsp;京ICP备11027288号&nbsp;&nbsp;网络视听许可证<a href="http://www.douban.com/about?topic=licence" target="_blank">0110418</a>号&nbsp;&nbsp;文网文[2009]267号&nbsp;<img src="http://img3.douban.com/pics/biaoshi.gif" align="absmiddle" /><br> 京公网安备110105000728&nbsp;&nbsp;新出网证(京)字129号
</span>

<span class="fright">
    <a href="http://www.douban.com/about">关于豆瓣</a>
    · <a href="http://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="http://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="http://www.douban.com/about?policy=disclaimer">免责声明</a>
    
    · <a href="http://www.douban.com/help/">帮助中心</a>
    · <a href="http://developers.douban.com/" target="_blank">开发者</a>
    · <a href="http://www.douban.com/mobile/">移动应用</a>
    · <a href="http://www.douban.com/partner/">豆瓣广告</a>
</span>


</div>
</div>

<script src="http://img3.douban.com/js/core/do/packed__init_7701316160.js" data-cfg-corelib="http://img3.douban.com/js/packed_jquery.min6301986802.js"></script>
<script type="text/javascript">
  Do(function(){var a=$(".top-nav-more a.more").click(function(d){d.preventDefault();var b=$(d.currentTarget),c=b.parent();c.toggleClass("on");return false});$("body").click(function(){a.parent().removeClass("on")})});

        Do(function(){
            var t = $('#search_text');
            $("form[name=ssform]").submit(function(){
              if(t.val()==="成员、小组、音乐人、主办方") return false;
            })
        })
        
Do(function(){
$('#db-nav-main .nav-srh form').prettyField();
$('#db-nav-main .guide .lnk-close').click(function(e) {
  e.preventDefault();
  $.post_withck('/j/accounts/hidetip',{kind:5,show_to_all:'Y'}, function(){});
  $(this).closest('.tips-overly').fadeOut(300);
});
});

var tagsug_src = "http://img3.douban.com/js/lib/packed_tagsug2640635463.js";
window.Do=window.Do||function(a){typeof a=="function"&&setTimeout(a,0)};Do.add_js=function add_js(b){var a=document.createElement("script");a.src=b;document.getElementsByTagName("head")[0].appendChild(a)};Do.add_css=function add_css(c,b){var a=document.createElement("link");a.rel="stylesheet";a.href=c;document.getElementsByTagName("head")[0].appendChild(a)};Do.check_js=function check_js(a,c){var b=a();if(b){c(b)}else{setTimeout(function(){check_js(a,c)},33)}};Do(function(){var a=$("#search_text");a.one("focus",function(){Do.add_js(tagsug_src);Do.check_js(function(){return $.fn.tagsug&&window.Mustache},function(){a.tagsug({max:8,useUid:true,tips:"@某人，直达其个人主页"});var b=a._tagsug_api[0];b.on("choose",function(d,c){window.location="/people/"+c+"/"});a.tagsug({wordLimit:30,url:"",max:null,haltLink:false,customData:{cls:"sug-quick-search",items:[{name_cn:"图书",url:"http://book.douban.com/subject_search?cat=1003&search_text="},{name_cn:"电影",url:"http://movie.douban.com/subject_search?cat=1002&search_text="},{name_cn:"音乐",url:"http://movie.douban.com/subject_search?cat=1001&search_text="},{name_cn:"同城活动",url:"http://www.douban.com/event/search?search_text="}]},listTmpl:'<ul class="{{cls}}">{{#items}}<li><a href="{{url}}{{q}}">搜索 <b>{{q}}</b> 的{{name_cn}}</a></li>{{/items}}</ul>',leadChar:"%",tips:null})})})});

    Do(function(){$(".boutique a.lnk-close").click(function(){$.post_withck("/shop/hide",function(){$(".boutique").slideUp()})})});
  
    ;(function(){ var NEW_HOME_TIP=9;
Do(function(){$("#db-tip-renew .lnk-close").click(function(a){a.preventDefault();$.post_withck("/j/accounts/hidetip",{kind:NEW_HOME_TIP,show_to_all:"Y"},function(){});$(this).parent().fadeOut(300)});$(".lnk-back-old").click(function(a){a.preventDefault();$.post_withck("/j/remain_oldstyle",{oldstyle:"1"},function(){location.href="/"})})}); })();
    
Do(function() {
    var CK='38ij';
var DOUBAN='http://www.douban.com';
var TARGET_NODE='#bd .guess-list';
var guessList=$(TARGET_NODE),handleFavIt=function(b){if(b.hasClass("processing")){return}var e=parseInt(b.text(),10),d=b.hasClass("selected")?1:0,a={tid:b.data("tid"),tkind:b.data("tkind"),ck:CK},c=function(f,h,g){h=(h+g<=0)?"0":h+g;f.html(h+f.text().match(/\D+/)[0])};if(isNaN(e)){e=0}b.addClass("processing");$.ajax({type:d?"delete":"post",url:"/j/like",data:a,success:function(){b.removeClass("processing");if(d){b.removeClass("selected");c(b,e,-1)}else{b.addClass("selected");c(b,e,1)}},dataType:"json"})};guessList.find(".item").hover(function(){$(this).addClass("mover")},function(){$(this).removeClass("mover")}).end().find(".fav-btn a").click(function(a){handleFavIt($(a.currentTarget));return false});
});
Do.ready(function(){
    Do.preload(['http://img3.douban.com/js/separation/packed__all295341955.js','http://img3.douban.com/js/packed_douban7786199553.js']);
});
</script>

<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-7019765-1']);
_gaq.push(['_addOrganic', 'baidu', 'word']);
_gaq.push(['_addOrganic', 'soso', 'w']);
_gaq.push(['_addOrganic', '3721', 'name']);
_gaq.push(['_addOrganic', 'youdao', 'q']);
_gaq.push(['_addOrganic', 'so.360.cn', 'q']);
_gaq.push(['_addOrganic', 'vnet', 'kw']);
_gaq.push(['_addOrganic', 'sogou', 'query']);
_gaq.push(['_addIgnoredOrganic', '豆瓣']);
_gaq.push(['_addIgnoredOrganic', 'douban']);
_gaq.push(['_addIgnoredOrganic', '豆瓣网']);
_gaq.push(['_addIgnoredOrganic', 'www.douban.com']);
_gaq.push(['_setDomainName', '.douban.com']);


    _gaq.push(['_setCustomVar', 1, 'responsive_view_mode', 'desktop', 3]); 

_gaq.push(['_trackPageview']);
_gaq.push(['_trackPageLoadTime']);
    _gaq.push(['_setVar', '153']);


(function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
})();
</script>







<!-- gardner5-->

    <!-- douban ad begin -->
    




<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = 'http://erebor.douban.com/',
            userId = '1539016',
            browserId = 'sXP/lxGdf/o',
            ipAddress = '221.4.220.86',
            criteria = '3:/',
            preview = '',
            debug = false,
            adSlots = ['dale_homepage_online_activity_promo_1', 'dale_homepage_online_activity_promo_2'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, ip: ipAddress, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', 'http://img3.douban.com/js/packed_ad2101514973.js');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>




    <!-- douban ad end -->

<script>var _check_hijack = function () {
            var _sig = "sXP/lxGd", _login = true, bid = get_cookie('bid');
            if (location.protocol != "file:" && (typeof(bid) != "string" && _login || typeof(bid) == "string" && bid.substring(0,8) != _sig)) {
                location.href+=(/\?/.test(location.href)?"&":"?") + "_r=" + Math.random().toString(16).substring(2);
            }};
            if (typeof(Do) != 'undefined') Do(_check_hijack);
            else if (typeof(get_cookie) != 'undefined') _check_hijack();
            </script>



</body>
</html>





'''