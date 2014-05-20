<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="violation_record">
	<html>
		<head>
			<title>
				Generated Report
			</title>
			<script src="config/standard.js" type="text/javascript"></script>
			<link rel="stylesheet" type="text/css" href="config/standard.css" />
			<link>
				<xsl:attribute name="rel">stylesheet</xsl:attribute>
				<xsl:attribute name="type">text/css</xsl:attribute>
				<xsl:attribute name="href"><xsl:value-of select="viocss"/></xsl:attribute>
			</link>
			
		</head>
		<body onload="print_me()">
			<div id="DATE">
				<p>
					<xsl:value-of select="Date/Month"/>
					<xsl:value-of select="Date/Day"  />
					<xsl:value-of select="Date/Year" />
				</p>
			</div>
			<div id="NAME">
				<p>
					<xsl:value-of select="Prefix" />
					<xsl:value-of select="FName" />
					<xsl:value-of select="MINIT" />
					<xsl:value-of select="LName" />
				</p>
			</div>
			<div id="Address">
				<p>
					<xsl:value-of select="Addr1" />
					<xsl:value-of select="Addr2" />
					<xsl:value-of select="City"  />
					<xsl:value-of select="State" />
					<xsl:value-of select="Zip"   />
				</p>
			</div>
			<div id="MailAddress">
				<p>
					<xsl:value-of select="MAddr1" />
					<xsl:value-of select="MAddr2" />
					<xsl:value-of select="MCity"  />
					<xsl:value-of select="MState" />
					<xsl:value-of select="MZip"	  />
				</p>
			</div>
			<div id="Violation">
				<p>
					<xsl:value-of select="viocss" />
					<xsl:value-of select="Violation" />
					<xsl:value-of select="Map"	/>
				</p>
			</div>
		</body>
    </html>
</xsl:template>
</xsl:stylesheet>
