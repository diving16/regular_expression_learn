import re

text=""" 

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="baidu-site-verification" content="m1imKvW1HK" />
  <link rel="shortcut icon" href="/Public/img/favicon.ico" type="image/x-icon">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="x-ua-compatible" content="ie=edge">
  <!-- Bootstrap CSS -->
  <!-- <link href="https://cdn.bootcss.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" rel="stylesheet"> -->
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1 user-scalable=no" />
<!-- 删除默认的苹果工具栏和菜单栏 ： 即启用 WebApp 全屏模式  -->
<meta name="apple-mobile-web-app-capable" content="yes" />
<!-- 在web app应用下状态条（屏幕顶部条）的颜色；默认值为default（白色），可以定为black（黑色）和black-translucent（灰色半透明）若值为“black-translucent”将会占据页面px位置，浮在页面上方（会覆盖页面20px高度–iphone4和itouch4的Retina屏幕为40px）。 -->
<meta name="apple-mobile-web-app-status-bar-style" content="black" />
<!-- 忽略数字自动识别为电话号码 ,忽略识别邮箱 -->
<meta name="format-detection" content="telephone=no, email=no" />
<!-- 启用360浏览器的极速模式(webkit) -->
<meta name="renderer" content="webkit">
<!-- 避免IE使用兼容模式 -->
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<!-- uc强制竖屏 -->
<meta name="screen-orientation" content="portrait" />
<!-- QQ强制竖屏 -->
<meta name="x5-orientation" content="portrait">
<!-- UC强制全屏 -->
<meta name="full-screen" content="true" />
<!-- QQ强制全屏 -->
<meta name="x5-fullscreen" content="true" />
<!-- 360强制全屏 -->
<meta name="360-fullscreen" content="true" />
<!-- 站内搜索站点验证 -->
<meta name="baidu-site-verification" content="m1imKvW1HK" />
<link rel="shortcut icon" href="/Public/img/favicon.ico" type="image/x-icon">
<script src="/Public/js/fontbase.js?v=12"></script>
<link href="/Public/css/lib/bootstrap.min.css?v=14" rel="stylesheet">
<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
      <script src="https://cdn.bootcss.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://cdn.bootcss.com/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
<link rel="stylesheet" href="/Public/css/common.css?v=16">
<script type="text/javascript">
var _bdhmProtocol = (("https:" == document.location.protocol) ? " https://" : " http://");
document.write(unescape("%3Cscript src='" + _bdhmProtocol + "hm.baidu.com/h.js%3Fb9a77820b2fa17d7223b50a01ab1aa7a' type='text/javascript'%3E%3C/script%3E"));
</script>

  <link href="/Public/css/slick.css?v=12" rel="stylesheet">
  <link href="/Public/css/slick-theme.css?v=12" rel="stylesheet">
  <link rel="stylesheet" href="/Public/css/contactUs.css?v=16">
  <title>联系百度</title>
  <meta name="description" content='总机：(+86 10)5992 8888 TEL: (+86 10)5992 8888传真：(+86 10)5992 0000 FAX:(+86 10)5992 0000'>
  <meta name="keywords" content="百度办公地址、百度联系方式、联系百度、如何联系百度、怎么联系百度">
</head>

<body id="contactUs">
  <div class="main">
    <div class="bd-content-nav nav-show J-bd-nav">
  <div class="section nav-section">
    <div class="nav-box">
      <div class="row">
        <div class="col-sm-2 col-xs-12">
          <a href="/home/index">
            <img src="/Public/img/logo.png?v=15" alt="" class="logo">
          </a>
        </div>
        <div class="col-sm-10 col-xs-12">
          <ul class="bd-nav">
            <li class="nav-bd-link active"><a href="/home/index" target="_blank">关于百度</a></li>
            <li class="nav-bd-link"><a href="//www.baidu.com/more/" target="_blank">关于产品</a></li>
            <li class="nav-bd-link"><a href="/home/index/join_us" target="_blank">加入我们</a></li>
            <li class="nav-bd-link"><a href="/home/index/contact_us" target="_blank">联系我们</a></li>
            <div class="sideline"></div>
          </ul>
        </div>
        <div class="bd-content-fun">
          <div class="home-div">
            <span class="cn-home-link">中文</span>|
            <a href="//ir.baidu.com/phoenix.zhtml?c=188488&p=irol-irhome" class="en-home-link" target="_blank">EN</a>
          </div>
          <script type="text/javascript">(function(){document.write(unescape('%3Cdiv id="bdcs"%3E%3C/div%3E'));var bdcs = document.createElement('script');bdcs.type = 'text/javascript';bdcs.async = true;bdcs.src = 'http://znsv.baidu.com/customer_search/api/js?sid=6706059176758103565' + '&plate_url=' + encodeURIComponent(window.location.href) + '&t=' + Math.ceil(new Date()/3600000);var s = document.getElementsByTagName('script')[0];s.parentNode.insertBefore(bdcs, s);})();</script>


        </div>
      </div>
    </div>
  </div>
</div>
<div class="h5-nav-bar J-bd-nav">
  <!-- <div class="h5-nav-search-btn"></div> -->
  <div class="logo-box">
    <img src="/Public/img/logo.png?v=15" alt="" class="h5-nav-logo">
  </div>
  <svg id="list" class="h5-nav-toggle-box" width="44" height="44" viewBox="0, 0, 44, 44"></svg>
  <div class="h5-nav-list">
    <a href="/home/index" class="h5-nav h5-active" target="_blank">关于百度</a>
    <a href="//www.baidu.com/more/" class="h5-nav" target="_blank">关于产品</a>
    <a href="/home/index/join_us" class="h5-nav" target="_blank">加入我们</a>
    <a href="/home/index/contact_us" class="h5-nav" target="_blank">联系我们</a>
    <a href="//ir.baidu.com/phoenix.zhtml?c=188488&p=irol-irhome" class="h5-nav" target="_blank">ENGLISH</a>
  </div>
</div>
<div class="h5-nav-mask"></div>

    <div class="main-body">
      <div class="left-box">
        <div class="bg-box hidden-xs">
          <img src="http://static.home.baidu.com/homebd/hmkljbndfacgie1496931590.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A19%3A51Z%2F-1%2F%2Fb22b9cafba3b3aa07aa331fb038d0c6df9eaa1c7aae35bae4281357217f0dba1" class="background">
          <div class="phone-title">
            <p style="text-align: center;"><span style="font-size: 44px;">联系我们</span></p>          </div>
          <div class="contact-phone">
            <p class="phone-num-line">

              <span class="line-ch">总机：(+86 10)5992 8888</span><span class="line-ch">TEL: (+86 10)5992 8888</span><span class="line-ch">传真：(+86 10)5992 0000</span><span class="line-ch">FAX:(+86 10)5992 0000</span>            </p>
          </div>
        <div class="map-content">
            <div class="map-content-title">
              <img src="http://static.home.baidu.com/homebd/bhgdjmlcfkaien1496931694.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A21%3A34Z%2F-1%2F%2Ff26a3d3d9eaa094ed1006bc2efae1f1cd3cf40261cffd6e835704e20d4faec1b" class="map-content-flag">
              <span class="map-content-country">北京</span>
              <p class="map-content-line"></p>
            </div>
            <div class="map-all-box">
                <div data-href="http://map.baidu.com/?newmap=1&amp;ie=utf-8&amp;s=s%26wd%3D%E7%99%BE%E5%BA%A6%E5%A4%A7%E5%8E%A6" class="contact-list">
                  <img src="http://static.home.baidu.com/homebd/jhmlgefinkadbc1496932028.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A27%3A08Z%2F-1%2F%2F3d81f1beeb8a94b113e4fffd76669f666547f9de7d60fd28ebc4126339f92536" class="map-img">
                  <div class="contact-address">
                      百度大厦                      <p style="text-align: left;">北京市海淀区上地十街10号百度大厦<br/></p><p style="text-align: left;">Baidu Campus, No. 10 Shangdi 10th Street, Haidian District, Beijing, China<br/></p><p style="text-align: left;">邮 编：100085<br/></p><p style="text-align: left;">Post Code：100085<br/></p>                  </div>
                </div>
              </div><div class="map-all-box">
                <div data-href="http://map.baidu.com/?newmap=1&amp;ie=utf-8&amp;s=s%26wd%3D%E7%99%BE%E5%BA%A6%E7%A7%91%E6%8A%80%E5%9B%AD" class="contact-list">
                  <img src="http://static.home.baidu.com/homebd/imcefadbhklgjn1496932068.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A27%3A48Z%2F-1%2F%2Fcaa7741d5985e46d3a432c780821ed7b87c966510642a579a7d251b151585f8d" class="map-img">
                  <div class="contact-address">
                      百度科技园                      <p style="text-align: left;">北京市海淀区西北旺东路10号院百度科技园1号楼－5号楼</p><p style="text-align: left;">Baidu Technology Park Building No.1－No.5 No.10 Xibeiwang East Road,Haidian District, Beijing, China</p><p style="text-align: left;">邮 编：100193</p><p style="text-align: left;">Post Code：100193</p>                  </div>
                </div>
              </div><div class="map-all-box">
                <div data-href="http://map.baidu.com/?newmap=1&amp;ie=utf-8&amp;s=s%26wd%3D%E9%B9%8F%E5%AF%B0%E5%9B%BD%E9%99%85%E5%A4%A7%E5%8E%A6" class="contact-list">
                  <img src="http://static.home.baidu.com/homebd/enhgmifdkabclj1496932352.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A32%3A33Z%2F-1%2F%2F7182432f1fbc5b1107c36818ff6fdf8a3909a756747f1311efab5626f881ecd1" class="map-img">
                  <div class="contact-address">
                      鹏寰办公区                      <p style="text-align: left;">北京市海淀区上地东路1号盈创动力园区D座</p><p style="text-align: left;">POWER CREATIVE D, No.1 Shangdi East Road, Haidian District, Beijing, China</p><p style="text-align: left;">邮 编：100085</p><p style="text-align: left;">Post Code：100085</p>                  </div>
                </div>
              </div><div class="map-all-box">
                <div data-href="http://map.baidu.com/?newmap=1&amp;ie=utf-8&amp;s=s%26wd%3D%E8%85%BE%E9%A3%9E%E9%AB%98%E7%A7%91%E5%B2%AD" class="contact-list">
                  <img src="http://static.home.baidu.com/homebd/gdjmeblhancikf1496932567.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A36%3A08Z%2F-1%2F%2Fe1de1cd613b4596d207258579a3168c23a7478cb4c111ff2844c73d4886b9fae" class="map-img">
                  <div class="contact-address">
                      凯龙办公区                      <p style="text-align: left;">北京市海淀区东北旺西路8号中关村软件园17号北楼3层</p><p style="text-align: left;">No.17 Building, Zhongguancun Software Park, 8 Dongbeiwang West Road,Haidian District, Beijing, China</p><p style="text-align: left;">邮 编：100193</p><p style="text-align: left;">Post Code：100193</p>                  </div>
                </div>
              </div>            </div><div class="map-content">
            <div class="map-content-title">
              <img src="http://static.home.baidu.com/homebd/bhgdjmlcfkaien1496931694.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A21%3A34Z%2F-1%2F%2Ff26a3d3d9eaa094ed1006bc2efae1f1cd3cf40261cffd6e835704e20d4faec1b" class="map-content-flag">
              <span class="map-content-country">上海</span>
              <p class="map-content-line"></p>
            </div>
            <div class="map-all-box">
                <div data-href="http://map.baidu.com/?newmap=1&amp;s=inf%26uid%3D70b23e86c6e7113e58f6befd%26wd%3D%E7%99%BE%E5%BA%A6%E4%B8%8A%E6%B5%B7%E7%A0%94%E5%8F%91%E4%B8%AD%E5%BF%83%26all%3D1%26c%3D131&amp;from=alamap&amp;tpl=map_singlepoint" class="contact-list">
                  <img src="http://static.home.baidu.com/homebd/cbnkgjalheifdm1496932591.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A36%3A32Z%2F-1%2F%2F05c732c3a54381182d8e28f51d9709ac2fd4983b5aa9c0f602e1ab35d3d652cc" class="map-img">
                  <div class="contact-address">
                      上海研发中心                      <p style="text-align: left;">上海市浦东新区纳贤路701号百度上研大厦</p><p style="text-align: left;">701 Na Xian Road, Pudong ,Shanghai,China</p><p style="text-align: left;">邮　编：201210</p><p style="text-align: left;">Post Code: 201210</p>                  </div>
                </div>
              </div>            </div><div class="map-content">
            <div class="map-content-title">
              <img src="http://static.home.baidu.com/homebd/bhgdjmlcfkaien1496931694.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A21%3A34Z%2F-1%2F%2Ff26a3d3d9eaa094ed1006bc2efae1f1cd3cf40261cffd6e835704e20d4faec1b" class="map-content-flag">
              <span class="map-content-country">深圳</span>
              <p class="map-content-line"></p>
            </div>
            <div class="map-all-box">
                <div data-href="http://map.baidu.com/?newmap=1&amp;ie=utf-8&amp;s=s%26wd%3D%E6%B7%B1%E5%9C%B3%E5%B8%82%E5%8D%97%E5%B1%B1%E5%8C%BA%E5%AD%A6%E5%BA%9C%E8%B7%AF%E4%B8%9C%E7%99%BE%E5%BA%A6%E5%9B%BD%E9%99%85%E5%A4%A7%E5%8E%A6" class="contact-list">
                  <img src="http://static.home.baidu.com/homebd/fbgdlkacjeihnm1496932612.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A36%3A52Z%2F-1%2F%2Ff1d0e0c33568ee527713199dcce81e2b1914dd30e6c5d1703780febe21eb8d8b" class="map-img">
                  <div class="contact-address">
                      深圳研发中心                      <p style="text-align: left;">深圳市南山区学府路东百度国际大厦</p><p style="text-align: left;">Baidu International Building, Xuefu Road East,Nanshan District,ShenZhen</p><p style="text-align: left;">邮　编：518000</p><p style="text-align: left;">Post Code: 518000</p>                  </div>
                </div>
              </div>            </div><div class="map-content">
            <div class="map-content-title">
              <img src="http://static.home.baidu.com/homebd/jabedcimgnlhkf1496931818.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A23%3A39Z%2F-1%2F%2F88ac2e4ae707978be6afc511c9689042e42c905a1339023839f5d8f2439703bb" class="map-content-flag">
              <span class="map-content-country">森尼韦尔</span>
              <p class="map-content-line"></p>
            </div>
            <div class="map-all-box">
                <div data-href="http://j.map.baidu.com/nDI-e" class="contact-list">
                  <img src="http://static.home.baidu.com/homebd/hicbldjfagknem1496932625.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A37%3A06Z%2F-1%2F%2F1f2c046e3869909b15e4c92eb16664d1b0e727d3e15799650520b01b96c9c5b2" class="map-img">
                  <div class="contact-address">
                      Baidu USA                      <p style="text-align: left;">1195 Bordeaux Drive Sunnyvale</p><p style="text-align: left;">Post Code: CA 94089</p>                  </div>
                </div>
              </div>            </div>

        <div class="foot-box">
          <p class="map-content-line-footer"></p>
          <div class="contact-mail">
            <div class="mail-box">
                <div class="mail-title">
                  合作联系                </div>
                <div class="mail-content">
                  <span class="mail-content-text">
                      市场合作：upmco@baidu.com                  </span><span class="mail-content-text">
                      校园合作：campusmaster@baidu.com                  </span><span class="mail-content-text">
                      战略合作：zhanzhangpingtai@baidu.com                  </span>                </div>
              </div><div class="mail-box">
                <div class="mail-title">
                  业务联系                </div>
                <div class="mail-content">
                  <span class="mail-content-text">
                      百度无线：mbaidu@baidu.com                  </span><span class="mail-content-text">
                      百度推广售后热线：400-921-9999                  </span><span class="mail-content-text">
                      百度推广销售热线：400-800-8888                  </span>                </div>
              </div><div class="mail-box">
                <div class="mail-title">
                  投诉中心                </div>
                <div class="mail-content">
                  <span class="mail-content-text">
                      投诉中心网址： http://help.baidu.com                  </span>                </div>
              </div>          </div>
        </div>
        </div>





      <!-- 移动端 -->
      <div class="m-box visible-xs-block">
        <img src="http://static.home.baidu.com/homebd/hmkljbndfacgie1496931590.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A19%3A51Z%2F-1%2F%2Fb22b9cafba3b3aa07aa331fb038d0c6df9eaa1c7aae35bae4281357217f0dba1" class="m-background">
        <div class="m-phone-title">
          <p style="text-align: center;"><span style="font-size: 44px;">联系我们</span></p>        </div>
        <div class="m-contact-phone">
          <p class="m-phone-num-line">
              <span class="m-line-ch">总机：(+86 10)5992 8888</span><span class="m-line-ch">TEL: (+86 10)5992 8888</span><span class="m-line-ch">传真：(+86 10)5992 0000</span><span class="m-line-ch">FAX:(+86 10)5992 0000</span>          </p>
        </div>

      <div class="m-map-content">
            <div class="m-map-content-title">
              <img src="http://static.home.baidu.com/homebd/bhgdjmlcfkaien1496931694.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A21%3A34Z%2F-1%2F%2Ff26a3d3d9eaa094ed1006bc2efae1f1cd3cf40261cffd6e835704e20d4faec1b" class="m-map-content-flag">
              <span class="m-map-content-country">北京</span>
              <p class="m-map-content-line"></p>
            </div>
          <div class="m-map-all-box">
              <a href="//rc.mbd.baidu.com/zgks4zo">
                <p class="m-address-title">百度大厦</p>
                <img src="http://static.home.baidu.com/homebd/jhmlgefinkadbc1496932028.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A27%3A08Z%2F-1%2F%2F3d81f1beeb8a94b113e4fffd76669f666547f9de7d60fd28ebc4126339f92536" class="m-map-img">
                <div class="m-contact-address">
                      <p style="text-align: left;">北京市海淀区上地十街10号百度大厦<br/></p><p style="text-align: left;">Baidu Campus, No. 10 Shangdi 10th Street, Haidian District, Beijing, China<br/></p><p style="text-align: left;">邮 编：100085<br/></p><p style="text-align: left;">Post Code：100085<br/></p>                </div>
              </a>
            </div><div class="m-map-all-box">
              <a href="//rc.mbd.baidu.com/xx7k3fy">
                <p class="m-address-title">百度科技园</p>
                <img src="http://static.home.baidu.com/homebd/imcefadbhklgjn1496932068.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A27%3A48Z%2F-1%2F%2Fcaa7741d5985e46d3a432c780821ed7b87c966510642a579a7d251b151585f8d" class="m-map-img">
                <div class="m-contact-address">
                      <p style="text-align: left;">北京市海淀区西北旺东路10号院百度科技园1号楼－5号楼</p><p style="text-align: left;">Baidu Technology Park Building No.1－No.5 No.10 Xibeiwang East Road,Haidian District, Beijing, China</p><p style="text-align: left;">邮 编：100193</p><p style="text-align: left;">Post Code：100193</p>                </div>
              </a>
            </div><div class="m-map-all-box">
              <a href="//rc.mbd.baidu.com/x4hpfyf">
                <p class="m-address-title">鹏寰办公区</p>
                <img src="http://static.home.baidu.com/homebd/enhgmifdkabclj1496932352.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A32%3A33Z%2F-1%2F%2F7182432f1fbc5b1107c36818ff6fdf8a3909a756747f1311efab5626f881ecd1" class="m-map-img">
                <div class="m-contact-address">
                      <p style="text-align: left;">北京市海淀区上地东路1号盈创动力园区D座</p><p style="text-align: left;">POWER CREATIVE D, No.1 Shangdi East Road, Haidian District, Beijing, China</p><p style="text-align: left;">邮 编：100085</p><p style="text-align: left;">Post Code：100085</p>                </div>
              </a>
            </div><div class="m-map-all-box">
              <a href="//rc.mbd.baidu.com/vmclz03">
                <p class="m-address-title">凯龙办公区</p>
                <img src="http://static.home.baidu.com/homebd/gdjmeblhancikf1496932567.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A36%3A08Z%2F-1%2F%2Fe1de1cd613b4596d207258579a3168c23a7478cb4c111ff2844c73d4886b9fae" class="m-map-img">
                <div class="m-contact-address">
                      <p style="text-align: left;">北京市海淀区东北旺西路8号中关村软件园17号北楼3层</p><p style="text-align: left;">No.17 Building, Zhongguancun Software Park, 8 Dongbeiwang West Road,Haidian District, Beijing, China</p><p style="text-align: left;">邮 编：100193</p><p style="text-align: left;">Post Code：100193</p>                </div>
              </a>
            </div>        </div><div class="m-map-content">
            <div class="m-map-content-title">
              <img src="http://static.home.baidu.com/homebd/bhgdjmlcfkaien1496931694.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A21%3A34Z%2F-1%2F%2Ff26a3d3d9eaa094ed1006bc2efae1f1cd3cf40261cffd6e835704e20d4faec1b" class="m-map-content-flag">
              <span class="m-map-content-country">上海</span>
              <p class="m-map-content-line"></p>
            </div>
          <div class="m-map-all-box">
              <a href="//rc.mbd.baidu.com/jyo1jvd">
                <p class="m-address-title">上海研发中心</p>
                <img src="http://static.home.baidu.com/homebd/cbnkgjalheifdm1496932591.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A36%3A32Z%2F-1%2F%2F05c732c3a54381182d8e28f51d9709ac2fd4983b5aa9c0f602e1ab35d3d652cc" class="m-map-img">
                <div class="m-contact-address">
                      <p style="text-align: left;">上海市浦东新区纳贤路701号百度上研大厦</p><p style="text-align: left;">701 Na Xian Road, Pudong ,Shanghai,China</p><p style="text-align: left;">邮　编：201210</p><p style="text-align: left;">Post Code: 201210</p>                </div>
              </a>
            </div>        </div><div class="m-map-content">
            <div class="m-map-content-title">
              <img src="http://static.home.baidu.com/homebd/bhgdjmlcfkaien1496931694.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A21%3A34Z%2F-1%2F%2Ff26a3d3d9eaa094ed1006bc2efae1f1cd3cf40261cffd6e835704e20d4faec1b" class="m-map-content-flag">
              <span class="m-map-content-country">深圳</span>
              <p class="m-map-content-line"></p>
            </div>
          <div class="m-map-all-box">
              <a href="//rc.mbd.baidu.com/86vj0xr">
                <p class="m-address-title">深圳研发中心</p>
                <img src="http://static.home.baidu.com/homebd/fbgdlkacjeihnm1496932612.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A36%3A52Z%2F-1%2F%2Ff1d0e0c33568ee527713199dcce81e2b1914dd30e6c5d1703780febe21eb8d8b" class="m-map-img">
                <div class="m-contact-address">
                      <p style="text-align: left;">深圳市南山区学府路东百度国际大厦</p><p style="text-align: left;">Baidu International Building, Xuefu Road East,Nanshan District,ShenZhen</p><p style="text-align: left;">邮　编：518000</p><p style="text-align: left;">Post Code: 518000</p>                </div>
              </a>
            </div>        </div><div class="m-map-content">
            <div class="m-map-content-title">
              <img src="http://static.home.baidu.com/homebd/jabedcimgnlhkf1496931818.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A23%3A39Z%2F-1%2F%2F88ac2e4ae707978be6afc511c9689042e42c905a1339023839f5d8f2439703bb" class="m-map-content-flag">
              <span class="m-map-content-country">森尼韦尔</span>
              <p class="m-map-content-line"></p>
            </div>
          <div class="m-map-all-box">
              <a href="http://j.map.baidu.com/yvPQe">
                <p class="m-address-title">Baidu USA</p>
                <img src="http://static.home.baidu.com/homebd/hicbldjfagknem1496932625.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A37%3A06Z%2F-1%2F%2F1f2c046e3869909b15e4c92eb16664d1b0e727d3e15799650520b01b96c9c5b2" class="m-map-img">
                <div class="m-contact-address">
                      <p style="text-align: left;">1195 Bordeaux Drive Sunnyvale</p><p style="text-align: left;">Post Code: CA 94089</p>                </div>
              </a>
            </div>        </div>        <p class="m-line"></p>
        <div class="m-mail-box">
              <div class="m-mail-title">
                合作联系              </div>
              <div class="m-mail-content">
                <div class="m-mail-content-text">
                      市场合作：upmco@baidu.com                  </div><div class="m-mail-content-text">
                      校园合作：campusmaster@baidu.com                  </div><div class="m-mail-content-text">
                      战略合作：zhanzhangpingtai@baidu.com                  </div>              </div>
            </div><div class="m-mail-box">
              <div class="m-mail-title">
                业务联系              </div>
              <div class="m-mail-content">
                <div class="m-mail-content-text">
                      百度无线：mbaidu@baidu.com                  </div><div class="m-mail-content-text">
                      百度推广售后热线：400-921-9999                  </div><div class="m-mail-content-text">
                      百度推广销售热线：400-800-8888                  </div>              </div>
            </div><div class="m-mail-box">
              <div class="m-mail-title">
                投诉中心              </div>
              <div class="m-mail-content">
                <div class="m-mail-content-text">
                      投诉中心网址： http://help.baidu.com                  </div>              </div>
            </div>        <div class="full-section bottom-section">
  <div class="section">
    <div class="bd-home-bottom">
      <div class="bd-bottom-share">
        <span>实时资讯请关注：</span>


        <div class="share-wechat">
                    <img src="http://static.home.baidu.com/homebd/canbfldghejikm1496932813.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A40%3A14Z%2F-1%2F%2Fa795f1f97d12e2a8c9da9862672bd4fec4a887237ec8883e8a3974e9a52b3624" class="share-wechat-img" alt="">
                    <img src="http://static.home.baidu.com/homebd/djkgaclebfhnim1496932814.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A40%3A14Z%2F-1%2F%2F9dfa094e984958f1fefb4c3a95b5f8da3e60c759c30442b2479559bfbcdacf2c" class="share-wechat-qrcode">
                  </div>
                        <a href="http://weibo.com/baiduguanfang?refer_flag=1001030101_&amp;is_hot=1" target="_blank">
                  <img src="http://static.home.baidu.com/homebd/fnejlmkaghcdib1496932842.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A40%3A43Z%2F-1%2F%2F5907b18db08f16dba8613f5117fa9c699a09ac79273e32ef0a1f114b7bdd6e55" alt="">
                </a>                <a href="https://www.facebook.com/BaiduIncorporated" target="_blank">
                  <img src="http://static.home.baidu.com/homebd/ldmfajnhcbkegi1496932864.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A41%3A05Z%2F-1%2F%2F2a180dd88df9a8a7af776fd7239773fab056d1af32cf701e234f5664133a559b" alt="">
                </a>                <a href="https://twitter.com/Baidu_Inc" target="_blank">
                  <img src="http://static.home.baidu.com/homebd/ldgjhfknbaicem1496932883.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A41%3A23Z%2F-1%2F%2F9ec183749754c187c58c2d5b66a8d2f4bd59f6258188aae327addba639a1631d" alt="">
                </a>
      </div>

      <div class="bd-bottom-moremsg">
        <div class="bd-more-msg">合作联系</div>
        <a href="�" class="bd-more-duty bottom-cooperation" target="_blank">�</a><a href="�" class="bd-more-duty bottom-cooperation" target="_blank">�</a><a href="�" class="bd-more-duty bottom-cooperation" target="_blank">�</a>      </div><div class="bd-bottom-moremsg">
        <div class="bd-more-msg">业务联系</div>
        <a href="�" class="bd-more-duty bottom-cooperation" target="_blank">�</a><a href="�" class="bd-more-duty bottom-cooperation" target="_blank">�</a><a href="�" class="bd-more-duty bottom-cooperation" target="_blank">�</a>      </div><div class="bd-bottom-moremsg">
        <div class="bd-more-msg">投诉中心</div>
        <a href="�" class="bd-more-duty bottom-cooperation" target="_blank">�</a>      </div>      <div class="bd-bottom-icp">&copy; Baidu <a href="//www.baidu.com/duty/" target="_blank">使用百度前必读</a> 京ICP证030173号</div>
    </div>
  </div>
</div>

<div class="return-top">
  <img src="/Public/img/return-top.png?v=12" alt="" class="return-img">
</div>
<div class="pc-return">
  <img src="/Public/img/pc-backtop.png?v=12" alt="" class="pc-return-img">
</div>
<div class="mobile-bd-home-bottom">
  <div class="bd-bottom-share">
    <span>实时资讯请关注：</span>



    <div class="share-wechat">
                <img src="http://static.home.baidu.com/homebd/canbfldghejikm1496932813.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A40%3A14Z%2F-1%2F%2Fa795f1f97d12e2a8c9da9862672bd4fec4a887237ec8883e8a3974e9a52b3624" class="share-wechat-img" alt="">
                <img src="http://static.home.baidu.com/homebd/djkgaclebfhnim1496932814.jpg?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A40%3A14Z%2F-1%2F%2F9dfa094e984958f1fefb4c3a95b5f8da3e60c759c30442b2479559bfbcdacf2c" class="m-share-wechat-qrcode">
              </div>
                     <a href="http://weibo.com/baiduguanfang?refer_flag=1001030101_&amp;is_hot=1" target="_blank">
              <img src="http://static.home.baidu.com/homebd/fnejlmkaghcdib1496932842.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A40%3A43Z%2F-1%2F%2F5907b18db08f16dba8613f5117fa9c699a09ac79273e32ef0a1f114b7bdd6e55" alt="">
            </a>           <a href="https://www.facebook.com/BaiduIncorporated" target="_blank">
              <img src="http://static.home.baidu.com/homebd/ldmfajnhcbkegi1496932864.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A41%3A05Z%2F-1%2F%2F2a180dd88df9a8a7af776fd7239773fab056d1af32cf701e234f5664133a559b" alt="">
            </a>           <a href="https://twitter.com/Baidu_Inc" target="_blank">
              <img src="http://static.home.baidu.com/homebd/ldgjhfknbaicem1496932883.png?authorization=bce-auth-v1%2Fe6803def36ae467f81ebdb4bdc75f119%2F2017-06-08T14%3A41%3A23Z%2F-1%2F%2F9ec183749754c187c58c2d5b66a8d2f4bd59f6258188aae327addba639a1631d" alt="">
            </a>
  </div>
  <div class="mobile-flex">
    <div class="mobile-bd-bottom-moremsg mobile-flex-box">
           <div class="mobile-bd-bottom-content">公司介绍<img src="/Public/img/mobile-arrow-up.png?v=12" class="mobile-arrow-up"><img src="/Public/img/mobile-arrow-down.png?v=12" class="mobile-arrow-down"></div>
           <ul class="mobile-bd-detail">
            <li><a href="http://home.baidu.com/home/index/company_culture" target="_blank">核心价值观</a></li><li><a href="http://home.baidu.com/home/index/company" target="_blank">百度简介</a></li><li><a href="http://home.baidu.com/home/index/baidu_road" target="_blank">百度大事记</a></li><li><a href="http://home.baidu.com/home/index/management_team" target="_blank">管理团队</a></li>        </ul>
      </div><div class="mobile-bd-bottom-moremsg mobile-flex-box">
           <div class="mobile-bd-bottom-content">更多信息<img src="/Public/img/mobile-arrow-up.png?v=12" class="mobile-arrow-up"><img src="/Public/img/mobile-arrow-down.png?v=12" class="mobile-arrow-down"></div>
           <ul class="mobile-bd-detail">
            <li><a href="http://csr.baidu.com/" target="_blank">社会责任</a></li><li><a href="http://home.baidu.com/home/index/contact_us" target="_blank">联系我们</a></li>        </ul>
      </div><div class="mobile-bd-bottom-moremsg mobile-flex-box">
           <div class="mobile-bd-bottom-content">商业合作<img src="/Public/img/mobile-arrow-up.png?v=12" class="mobile-arrow-up"><img src="/Public/img/mobile-arrow-down.png?v=12" class="mobile-arrow-down"></div>
           <ul class="mobile-bd-detail">
            <li><a href="http://e.baidu.com/?subsite=bj" target="_blank">百度推广</a></li><li><a href="http://union.baidu.com/customerLogin.html?fromu=http%3A%2F%2Funion.baidu.com%2F" target="_blank">百度联盟</a></li><li><a href="http://pro.baidu.com/" target="_blank">营销中心</a></li>        </ul>
      </div>
  </div>
  <div class="mobile-bd-bottom-icp">&copy; Baidu <a href="//www.baidu.com/duty/" target="_blank">使用百度前必读</a> 京ICP证030173号</div>
</div>
<div class="loading"></div>

      </div>
      </div>
    </div>
  </div>
  <!-- <script src="/Public/js/jquery.min.js"></script> -->
  <script src="/Public/js/lib/jquery.min.js?v=16"></script>
<script src="/Public/js/rem.min.js?v=16"></script>
<script src="/Public/js/lib/bootstrap.min.js?v=16"></script>
<script src="/Public/js/lib/snap.svg-min.js?v=16"></script>
<script src="/Public/js/lib/mustache.min.js?v=16"></script>
<!-- <script src="/Public/js/scroll.js"></script> -->
<script src="/Public/js/common.js?v=16"></script>
<script>
var width = $(window).width();
if (width > 768) {
  window._hmt && window._hmt.push(['_trackEvent', '入口统计','pc端']);
  var height = $(window).height();
  $(window).scroll(function() {
    var top = $(window).scrollTop();
    if (top > height) {
      $(".pc-return").show();
    } else {
      $(".pc-return").hide();
    }
  });
  $("body").on("click", ".pc-return", function() {
    $('body,html').animate({
      scrollTop: 0
    }, 300);
  });
} else {
  window._hmt && window._hmt.push(['_trackEvent', '入口统计','手机端']);
  $(".main").on("click", ".return-img", function() {
    $('body,html').animate({
      scrollTop: 0
    }, 300);
  });
}
</script>
<script type="text/javascript">
var GV = {
  ROOT: "/",
};
</script>

  <script src="/Public/js/slick.min.js?v=13"></script>
  <!-- <script src="/Public/js/index.js"></script> -->
</body>

</html>
"""

#find_phone_number=re.compile(r'\d{3}-\d{3}-\d{4}')

find_phone_number=re.compile(r'(\d{3})-(\d{3})-(\d{4})')

match_list=find_phone_number.findall(text)

print(match_list[2][1])

