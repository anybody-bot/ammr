﻿<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="3.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="text" indent="no" encoding="utf-8"/>

  <xsl:template match="/">
.. Do not edit this file. It is generated automatically 
   by body/AAUHuman/BuildTools/anyxdefs.bat

All BodyModel constants
------------------------ 
<xsl:apply-templates select="anyxdefs/constant" />
</xsl:template>


<xsl:template match="constant">
.. ammr:bm_constant:: <xsl:value-of select="@name"/>
    :value: <xsl:value-of select="@default"/> 
<xsl:if test="@deprecated='true'">
    :deprecated:</xsl:if><xsl:text>

    </xsl:text><xsl:value-of select="@descr"/><xsl:text>
</xsl:text>
                
</xsl:template>

</xsl:stylesheet>