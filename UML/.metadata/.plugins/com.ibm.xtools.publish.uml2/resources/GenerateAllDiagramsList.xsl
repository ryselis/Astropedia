<?xml version="1.0"?>
<!--                                                                        -->
<!-- Licensed Materials - Property of IBM                                   -->
<!-- Copyright IBM Corp. 2003, 2009.  All Rights Reserved.                  -->
<!--                                                                        -->
<!-- US Government Users Restricted Rights - Use, duplication or disclosure -->
<!-- restricted by GSA ADP Schedule Contract with IBM Corp.                 -->
<!--                                                                        -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
    xmlns:uml="http://www.eclipse.org/uml2/1.0.0/UML"
    xmlns:xmi="http://www.omg.org/XMI"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:publish="http://www.ibm.com/Rational/XTools/Publish"
	xmlns:redirect="http://xml.apache.org/xalan/redirect"
    extension-element-prefixes="redirect"
    exclude-result-prefixes="xmi uml xsi publish">
    
    <!-- ======================================================================================== -->
    <!-- Generate the all elements list html file for the lower left navigation window -->
    <!-- ======================================================================================== -->
    <xsl:template match="uml:Model|packagedElement|uml:Profile" mode="createAllElementsList">
        <xsl:param name="titlePattern" select="@name"/>
        <xsl:param name="descriptionPattern">
            <xsl:call-template name="getLocalizedString">
                <xsl:with-param name="key" select="'Description.AllElements'"/>
            </xsl:call-template>
        </xsl:param>
        <xsl:param name="keywordsWithPatterns" select="''"/>
        <!-- Perform pattern replacement for any '#name' with the attribute 'name' -->
        <xsl:variable name="masterDocTitle">
            <xsl:call-template name="replaceSubString">
                <xsl:with-param name="theString">
                    <xsl:value-of select="$titlePattern"/>
                </xsl:with-param>
                <xsl:with-param name="matchSubString">
                    <xsl:text>#name</xsl:text>
                </xsl:with-param>
                <xsl:with-param name="replaceWith">
                    <xsl:value-of select="@name"/>
                </xsl:with-param>
            </xsl:call-template>
        </xsl:variable>
        <!--Generate the file names needed for referencing -->
        <xsl:variable name="allDiagramsFileName">
            <xsl:call-template name="createAllDiagramsFileName"/>
        </xsl:variable>
        <!-- Generate the file name needed for output -->
        <xsl:variable name="allDiagramsFullPathName">
            <xsl:call-template name="prependFullPathToFileName">
                <xsl:with-param name="fileName" select="$allDiagramsFileName"/>
            </xsl:call-template>
        </xsl:variable>
        <!-- Localized strings -->
        <xsl:variable name="allElementsHeading">
            <xsl:call-template name="getLocalizedString">
                <xsl:with-param name="key" select="'Heading.AllElements'"/>
            </xsl:call-template>
        </xsl:variable>
        <xsl:variable name="allDiagramsHeading">
            <xsl:call-template name="getLocalizedString">
                <xsl:with-param name="key" select="'Heading.AllDiagrams'"/>
            </xsl:call-template>
        </xsl:variable>
        <xsl:message terminate="no">
            <xsl:value-of select="$newLine"/>
            <xsl:text>Values for variables and parameters</xsl:text>
            <xsl:value-of select="$newLine"/>
            <xsl:text>The value of allDiagramsFileName is: "</xsl:text>
            <xsl:value-of select="$allDiagramsFileName"/>
            <xsl:text>"</xsl:text>
            <xsl:value-of select="$newLine"/>
            <xsl:text>The value of allDiagramsFullPathName is: "</xsl:text>
            <xsl:value-of select="$allDiagramsFullPathName"/>
            <xsl:text>"</xsl:text>
            <xsl:value-of select="$newLine"/>
            <xsl:text>There are </xsl:text>
            <xsl:value-of select="count ($globalTopLevelAllSupportedElementTypes)"/>
            <xsl:text> elements.</xsl:text>
            <xsl:text>There are </xsl:text>
            <xsl:value-of select="count (//contents[@xsi:type='notation:Diagram'])"/>
            <xsl:text> diagrams.</xsl:text>
            <xsl:value-of select="$newLine"/>
        </xsl:message>
        <!-- Open a file for the all elements list (and fill it with an href pointing to the content 
         page for each element - in the for-each below) -->
        <xsl:if test="element-available('redirect:open')">
        	<redirect:open file="{$allDiagramsFullPathName}" />
        </xsl:if>
        <redirect:write file="{$allDiagramsFullPathName}">
            <html>
                <xsl:call-template name="outputHTMLHeader">
                    <xsl:with-param name="titlePattern">
                        <xsl:text>#name (</xsl:text>
                        <xsl:value-of select="$masterDocTitle"/>
                        <xsl:text>)</xsl:text>
                    </xsl:with-param>
                    <xsl:with-param name="titleReplaceToken">
                        <xsl:text>#name</xsl:text>
                    </xsl:with-param>
                    <xsl:with-param name="titleReplaceWith" select="'All Elements'"/>
                    <xsl:with-param name="descriptionPattern" select="$descriptionPattern"/>
                    <xsl:with-param name="descriptionReplaceToken">
                        <xsl:text>#name</xsl:text>
                    </xsl:with-param>
                    <xsl:with-param name="descriptionReplaceWith" select="@name"/>
                    <xsl:with-param name="keywordsPattern" select="$keywordsWithPatterns"/>
                    <xsl:with-param name="keywordsReplaceToken">
                        <xsl:text>#name</xsl:text>
                    </xsl:with-param>
                    <xsl:with-param name="keywordsReplaceWith" select="@name"/>
                </xsl:call-template>
                <body>
                    <table border="0" width="100%">
                        <tr>
                            <td nowrap="">
                                <b>
                                    <xsl:copy-of select="$allDiagramsHeading"/>
                                </b>
                                <br/>
                                <!-- Loop for each contained element creating an entry in the list -->
                                <xsl:for-each select="//contents[@xsi:type='notation:Diagram']">
                                    <xsl:sort select="@name"/>
                                    <xsl:sort select="@publish:qualifiedname"/>
                                    <xsl:variable name="elementContentFileName">
                                        <xsl:call-template name="createElementContentFileName"/>
                                    </xsl:variable>
                                    <xsl:variable name="iconImageFileName">
                                        <xsl:call-template name="createElementIconFileName"/>
                                    </xsl:variable>
                                    <!-- Create a reference to each element's content HTML file -->
                                    <xsl:call-template name="outputImageAndTextLinkHTML">
                                        <xsl:with-param name="link" select="$elementContentFileName"/>
                                        <xsl:with-param name="image">
	                                        <xsl:if test="@publish:icon != ''">
	                                        	<xsl:value-of select="$iconImageFileName"/>
	                                        </xsl:if>
                                        </xsl:with-param>
                                        <xsl:with-param name="text" select="@name"/>
                                        <xsl:with-param name="target" select="'elementFrame'"/>
                                    </xsl:call-template>
                                    <br/>
                                    <!-- Create the content HTML for the element -->
                                    <xsl:apply-templates
                                        mode="createElementContent" select=".">
                                        <xsl:with-param name="titlePattern" select="$masterDocTitle"/>
                                    </xsl:apply-templates>
                                </xsl:for-each>
                            </td>
                        </tr>
                    </table>
                </body>
            </html>
		</redirect:write>            
        <xsl:if test="element-available('redirect:close')">
        	<redirect:close file="{$allDiagramsFullPathName}" />
        </xsl:if>
    </xsl:template>
    
    <!-- Create the navigation page for the lower left hand all elements/diagrams navigation frame page
      This includes generation of contents for xxx-allelements.html -->
    <xsl:template name="createAllDiagramsNavigationHtml" match="packagedElement[@xsi:type='uml:Package'] | uml:Model | uml:Profile" mode="SplitMode_AllDiagramsNavigationHtml">
        <xsl:param name="titlePattern" select="@name"/>
        <xsl:param name="descriptionPattern">
            <xsl:call-template name="getLocalizedString">
                <xsl:with-param name="key" select="'Description.AllElements'"/>
            </xsl:call-template>
        </xsl:param>
        <xsl:param name="keywordsWithPatterns" select="''"/>
        <!-- Perform pattern replacement for any '#name' with the attribute 'name' -->
        <xsl:variable name="masterDocTitle">
            <xsl:call-template name="replaceSubString">
                <xsl:with-param name="theString">
                    <xsl:value-of select="$titlePattern"/>
                </xsl:with-param>
                <xsl:with-param name="matchSubString">
                    <xsl:text>#name</xsl:text>
                </xsl:with-param>
                <xsl:with-param name="replaceWith">
                    <xsl:value-of select="@name"/>
                </xsl:with-param>
            </xsl:call-template>
        </xsl:variable>
        <!--Generate the file names needed for referencing -->
        <xsl:variable name="allDiagramsFileName">
            <xsl:call-template name="createAllDiagramsFileName"/>
        </xsl:variable>
        <!-- Generate the file name needed for output -->
        <xsl:variable name="allDiagramsFullPathName">
            <xsl:call-template name="prependFullPathToFileName">
                <xsl:with-param name="fileName" select="$allDiagramsFileName"/>
            </xsl:call-template>
        </xsl:variable>
        <!-- Localized strings -->
        <xsl:variable name="allElementsHeading">
            <xsl:call-template name="getLocalizedString">
                <xsl:with-param name="key" select="'Heading.AllElements'"/>
            </xsl:call-template>
        </xsl:variable>
        <xsl:variable name="allDiagramsHeading">
            <xsl:call-template name="getLocalizedString">
                <xsl:with-param name="key" select="'Heading.AllDiagrams'"/>
            </xsl:call-template>
        </xsl:variable>
        <xsl:message terminate="no">
            <xsl:value-of select="$newLine"/>
            <xsl:text>Values for variables and parameters</xsl:text>
            <xsl:value-of select="$newLine"/>
            <xsl:text>The value of allDiagramsFileName is: "</xsl:text>
            <xsl:value-of select="$allDiagramsFileName"/>
            <xsl:text>"</xsl:text>
            <xsl:value-of select="$newLine"/>
            <xsl:text>The value of allDiagramsFullPathName is: "</xsl:text>
            <xsl:value-of select="$allDiagramsFullPathName"/>
            <xsl:text>"</xsl:text>
            <xsl:value-of select="$newLine"/>
            <xsl:text>There are </xsl:text>
            <xsl:value-of select="count ($globalTopLevelAllSupportedElementTypes)"/>
            <xsl:text> elements.</xsl:text>
            <xsl:text>There are </xsl:text>
            <xsl:value-of select="count (//contents[@xsi:type='notation:Diagram'])"/>
            <xsl:text> diagrams.</xsl:text>
            <xsl:value-of select="$newLine"/>
        </xsl:message>
        <!-- Open a file for the all elements list (and fill it with an href pointing to the content 
         page for each element - in the for-each below) -->
        <xsl:if test="element-available('redirect:open')">
        	<redirect:open file="{$allDiagramsFullPathName}" />
        </xsl:if>
        <redirect:write file="{$allDiagramsFullPathName}">
            <html>
                <xsl:call-template name="outputHTMLHeader">
                    <xsl:with-param name="titlePattern">
                        <xsl:text>#name (</xsl:text>
                        <xsl:value-of select="$masterDocTitle"/>
                        <xsl:text>)</xsl:text>
                    </xsl:with-param>
                    <xsl:with-param name="titleReplaceToken">
                        <xsl:text>#name</xsl:text>
                    </xsl:with-param>
                    <xsl:with-param name="titleReplaceWith" select="'All Elements'"/>
                    <xsl:with-param name="descriptionPattern" select="$descriptionPattern"/>
                    <xsl:with-param name="descriptionReplaceToken">
                        <xsl:text>#name</xsl:text>
                    </xsl:with-param>
                    <xsl:with-param name="descriptionReplaceWith" select="@name"/>
                    <xsl:with-param name="keywordsPattern" select="$keywordsWithPatterns"/>
                    <xsl:with-param name="keywordsReplaceToken">
                        <xsl:text>#name</xsl:text>
                    </xsl:with-param>
                    <xsl:with-param name="keywordsReplaceWith" select="@name"/>
                </xsl:call-template>
                <body>
                    <table border="0" width="100%">
                        <tr>
                            <td nowrap="">
                                <b>
                                    <xsl:copy-of select="$allDiagramsHeading"/>
                                </b>
                                <br/>
                                <!-- use xxx-diagrams.xml file for the top level element -->
                                <xsl:variable name="allDiagramsFilePath">
                                    <xsl:call-template name="constructAuxilliaryXmlFilepath">
                                        <xsl:with-param name="guid" select="@xmi:id"/>
                                        <xsl:with-param name="suffix" select="'diagrams.xml'"/>
                                    </xsl:call-template>
                                </xsl:variable>
                                <xsl:variable name="allDiagrams" select="document($allDiagramsFilePath)/publish:diagrams"/>
                                <!-- Loop for each contained element creating an entry in the list -->
                                <xsl:for-each select="$allDiagrams/publish:diagram">
                                    <xsl:sort select="@name"/>
                                    <xsl:sort select="@publish:qualifiedname"/>
                                    <xsl:variable name="elementContentFileName">
                                        <xsl:call-template name="createElementContentFileName"/>
                                    </xsl:variable>
                                    <xsl:variable name="iconImageFileName">
                                        <xsl:call-template name="createElementIconFileName"/>
                                    </xsl:variable>
                                    <!-- Create a reference to each element's content HTML file -->
                                    <xsl:call-template name="outputImageAndTextLinkHTML">
                                        <xsl:with-param name="link" select="$elementContentFileName"/>
                                        <xsl:with-param name="image">
	                                        <xsl:if test="@publish:icon != ''">
	                                        	<xsl:value-of select="$iconImageFileName"/>
	                                        </xsl:if>
                                        </xsl:with-param>
                                        <xsl:with-param name="text" select="@name"/>
                                        <xsl:with-param name="target" select="'elementFrame'"/>
                                        <xsl:with-param name="ttip" select="@publish:qualifiedname"/>
                                    </xsl:call-template>
                                    <br/>
                                </xsl:for-each>
                            </td>
                        </tr>
                    </table>
                </body>
            </html>
        </redirect:write>
        <xsl:if test="element-available('redirect:close')">
        	<redirect:close file="{$allDiagramsFullPathName}" />
        </xsl:if>
    </xsl:template>
</xsl:stylesheet>
