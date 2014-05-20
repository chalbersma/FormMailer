<?xml version="1.0" encoding="ISO-8859-1"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:template match="/">
    <html>
      <head>
	<meta http-equiv="content-type" content="text/html; charset=utf-8" />
	<title>SAE Mo-Gamma: Officers</title>
	<meta name="sae" content="" />
	<meta name="description" content="" />
	<link href="default.css" rel="stylesheet" type="text/css" media="screen" />
      </head>
      <body>
	<script type="text/javascript" src="js_functions.js" ></script>
	<script type="text/javascript" >
	  page_name=-1;
	  logomenu(page_name);
	</script>
	<div id="latest-post" class="wide-post">
	  <h1 class="title"><a href="#">Officer Info</a></h1>
	  <div class="entry">
	    <table border="1">
	      <tr>
		<th>Office</th>
		<th>Name</th>
		<th>Email</th>
	      </tr>
	      <xsl:for-each select="officers/office">
		<tr>
		  <td><xsl:value-of select="name_long"/></td>
		  <td><xsl:value-of select="current_person"/></td>
		  <td><xsl:value-of select="email"/></td>
		</tr>
	      </xsl:for-each>
	    </table>
	  </div>
	  <div class="bottom"></div>
	</div>
	<script type="text/javascript" >
	  draw_bottom_bits();
	</script>
      </body>
    </html>
</xsl:template>
</xsl:stylesheet>
