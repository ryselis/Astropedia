<?xml version="1.0"?>
<!--                                                                        -->
<!-- Licensed Materials - Property of IBM                                   -->
<!-- Copyright IBM Corp. 2003, 2011.  All Rights Reserved.                  -->
<!--                                                                        -->
<!-- US Government Users Restricted Rights - Use, duplication or disclosure -->
<!-- restricted by GSA ADP Schedule Contract with IBM Corp.                 -->
<!--                                                                        -->
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
	xmlns:xmi="http://www.omg.org/XMI" xmlns:uml="http://www.eclipse.org/uml2/1.0.0/UML"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xmlns:publish="http://www.ibm.com/Rational/XTools/Publish"
	xmlns:redirect="http://xml.apache.org/xalan/redirect" xmlns:dojo="http://dojotoolkit.org"
	extension-element-prefixes="redirect" exclude-result-prefixes="xmi uml xsi publish dojo">

	<!-- 3. Create initial top left frame contents (xxx-navigation-frame.html) TLF -->
	<xsl:template match="packagedElement[@xsi:type='uml:Package'] | uml:Model | uml:Profile"
		mode="createDojoNavigation">
		<!-- variables -->
		<xsl:variable name="packageListFileName">
			<xsl:call-template name="createPackageListFileName"/>
		</xsl:variable>
		<!-- Generate the file name needed for output -->
		<xsl:variable name="dojoFullPathName">
			<xsl:call-template name="prependFullPathToFileName">
				<xsl:with-param name="fileName" select="$packageListFileName"/>
			</xsl:call-template>
		</xsl:variable>

		<!-- Generate the file name needed for json output -->
		<xsl:variable name="treeModelFileName">
			<xsl:call-template name="createTreeModelFileName"/>
		</xsl:variable>
		<xsl:variable name="treeModelFullPathName">
			<xsl:call-template name="prependFullPathToFileName">
				<xsl:with-param name="fileName" select="$treeModelFileName"/>
			</xsl:call-template>
		</xsl:variable>

		<!-- Generate the file name needed for icon.css output -->
		<xsl:variable name="iconsCSSFileName">
			<xsl:call-template name="createIconsCSSFileName"/>
		</xsl:variable>
		<xsl:variable name="iconsCSSFullPathName">
			<xsl:call-template name="prependFullPathToFileName">
				<xsl:with-param name="fileName" select="$iconsCSSFileName"/>
			</xsl:call-template>
		</xsl:variable>
		
	    <xsl:variable name="modelsTitle">
	        <xsl:call-template name="getLocalizedString">
	            <xsl:with-param name="key" select="'NavTree.Models'"/>
	        </xsl:call-template>
	    </xsl:variable>
		
	    <xsl:variable name="diagramsTitle">
	        <xsl:call-template name="getLocalizedString">
	            <xsl:with-param name="key" select="'NavTree.Diagrams'"/>
	        </xsl:call-template>
	    </xsl:variable>

		<!-- use packages.xml file for the top level element -->
		<xsl:variable name="hierarchyFilePath">
			<xsl:call-template name="constructAuxilliaryXmlFilepath">
				<xsl:with-param name="guid" select="@xmi:id"/>
				<xsl:with-param name="suffix" select="'hierarchy.xml'"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:variable name="diagramsFilePath">
			<xsl:call-template name="constructAuxilliaryXmlFilepath">
				<xsl:with-param name="guid" select="@xmi:id"/>
				<xsl:with-param name="suffix" select="'diagrams.xml'"/>
			</xsl:call-template>
		</xsl:variable>
		<xsl:variable name="allElements" select="document($hierarchyFilePath)"/>
		<xsl:variable name="allDiagrams" select="document($diagramsFilePath)"/>

		<!-- xxx-navigation-frame.html -->
        <xsl:if test="element-available('redirect:open')">
        	<redirect:open file="{$dojoFullPathName}" />
        </xsl:if>
		<redirect:write file="{$dojoFullPathName}">
<html>
    <head>
    	<META http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
        <title><xsl:value-of select="$allElements/child::*/@name"/></title>

        <style type="text/css">
            @import "dojo/dijit/themes/tundra/tundra.css";
            @import "WebPublish.css";
            @import "<xsl:value-of select="$iconsCSSFileName"/>";
            .dijitTreeContent {cursor:default;white-space:nowrap !important}
        </style>

        <xsl:text disable-output-escaping="yes">
        &lt;script type=&quot;text/javascript&quot; src=&quot;dojo/dojo/dojo.js&quot;
            djConfig=&quot;parseOnLoad: true&quot;&gt;&lt;/script&gt;
        &lt;script type=&quot;text/javascript&quot; src=&quot;dojo/dojo/webpublish.js&quot;&gt;&lt;/script&gt;
        </xsl:text>

        <script language="JavaScript" type="text/javascript">
            dojo.require("dojo.data.ItemFileReadStore");
            dojo.require("dijit.Tree");
        </script>
			
    </head>
    <body class="tundra">
        <h2>
            <xsl:value-of select="$allElements/child::*/@name"/>
        </h2>

        <div dojoType="dojo.data.ItemFileReadStore" jsId="modelStore"
            url="{$treeModelFileName}"></div>

        <xsl:text disable-output-escaping="yes">
        &lt;div dojoType="dijit.tree.ForestStoreModel" jsId="treeModel" 
            store="modelStore" query="{top:'true'}"
            childrenAttrs="children"&gt;&lt;/div&gt;
        </xsl:text>
				
        <div dojoType="dijit.Tree" jsId="tree"
            model="treeModel" showRoot="false">
            <xsl:text disable-output-escaping="yes">
            &lt;script type=&quot;dojo/method&quot; event=&quot;getIconClass&quot; args=&quot;item, opened&quot;&gt;
                var icon = null;
                try {
                    icon = item &amp;&amp; modelStore.getValue(item, &quot;icon&quot;);
                } catch (e) {
                    // leave icon null;
                }
                return icon || &quot;noteIcon&quot;;
            &lt;/script&gt;
            </xsl:text>
            <script type="dojo/method" event="onClick" args="item">
                var url = modelStore.getValue(item, "object");
                if (url != null) {
                    window.open(url, "elementFrame");
                }
            </script>
        </div>
			
    </body>
    </html>
		</redirect:write>
        <xsl:if test="element-available('redirect:close')">
        	<redirect:close file="{$dojoFullPathName}" />
        </xsl:if>

		<xsl:variable name="topIconFile">
			<xsl:value-of select="$allElements/child::*/@publish:icon"/>
		</xsl:variable>
		<xsl:variable name="topIconNumber">
		    <!--- remove "_icon.png" -->
			<xsl:value-of select="substring($topIconFile, 1, (string-length($topIconFile) - 9))"/>
		</xsl:variable>
		<xsl:variable name="topIconStyle">
		    <!--- prepend "icon" -->
			<xsl:value-of select="concat(&apos;icon&apos;, $topIconNumber)"/>
		</xsl:variable>
		<xsl:variable name="topIconPath">
			<xsl:value-of select="concat(&apos;../images/&apos;, $topIconFile)"/>
		</xsl:variable>
		

		<!-- xxx-tree.json -->
        <xsl:if test="element-available('redirect:open')">
        	<redirect:open file="{$treeModelFullPathName}" />
        </xsl:if>
		<redirect:write file="{$treeModelFullPathName}">
					<xsl:variable name="topHtmlPath">
						<xsl:value-of select="concat($allElements/child::*/@xmi:id, &apos;-content.html&apos;)"/>
					</xsl:variable>
{ 
    identifier: 'id',
    label: 'title',
    items: [
        {
            title: '<xsl:value-of select="$diagramsTitle"/>',
            top: true,
            id: '_DIAGRAMS_ROOT_NODE_',
            icon: '<xsl:value-of select="$topIconStyle"/>'<xsl:for-each select="$allDiagrams/publish:diagrams/publish:diagram"><xsl:if test="position() = 1"><xsl:text>,
            children: [</xsl:text></xsl:if><xsl:if test="@xmi:id">
                {_reference: '<xsl:value-of select="@xmi:id"/>' }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if>
</xsl:if><xsl:if test="position() = last()"><xsl:text>
            ]</xsl:text></xsl:if></xsl:for-each>
        },<xsl:apply-templates select="$allDiagrams/publish:diagrams/publish:diagram" mode="diagrams"/>
        {
            title: '<xsl:value-of select="$modelsTitle"/>',
            top: true,
            id: '_MODELS_ROOT_NODE_',
            icon: '<xsl:value-of select="$topIconStyle"/>',
            children: [
                {_reference: '<xsl:value-of select="@xmi:id"/>' }
            ]

        }<xsl:apply-templates select="$allElements" mode="models"/>
    ]
}

		</redirect:write>
        <xsl:if test="element-available('redirect:close')">
        	<redirect:close file="{$treeModelFullPathName}" />
        </xsl:if>	

        <xsl:if test="element-available('redirect:open')">
        	<redirect:open file="{$iconsCSSFullPathName}" />
        </xsl:if>
		<redirect:write file="{$iconsCSSFullPathName}">
.<xsl:value-of select="$topIconStyle"/> {
	background-image: url(<xsl:value-of select="$topIconPath"/>);
	background-repeat: no-repeat; 
	width: 16px;
	height: 16px;
}
            <xsl:apply-templates select="$allDiagrams/publish:diagrams/publish:diagram" mode="icons"/>
            <xsl:apply-templates select="$allElements" mode="icons"/>
		</redirect:write>
        <xsl:if test="element-available('redirect:close')">
        	<redirect:close file="{$iconsCSSFullPathName}" />
        </xsl:if>		


	</xsl:template>
	
	<!-- build the Model Explorer navigation tree: diagrams -->
	<xsl:template match="*" mode="diagrams">
		<xsl:if test="@xmi:id"><xsl:call-template name="createDiagramNode"/>
		    <xsl:for-each select="./child::*">
		        <xsl:apply-templates select="." mode="diagrams"/>
            </xsl:for-each>
		</xsl:if>
	</xsl:template>
	
	<!-- build the Model Explorer navigation tree: model elements -->
	<xsl:template match="*" mode="models">
		<xsl:if test="@xmi:id"><xsl:call-template name="createElementNode"/>
		    <xsl:for-each select="./child::*">
			    <xsl:apply-templates select="." mode="models"/>
		    </xsl:for-each>
		</xsl:if>
	</xsl:template>
	
	<!-- create a diagram node -->
	<xsl:template name="createDiagramNode">
		<xsl:variable name="iconFile">
			<xsl:value-of select="@publish:icon"/>
		</xsl:variable>
		<xsl:variable name="iconNumber">
		    <!--- remove "_icon.png" -->
			<xsl:value-of select="substring($iconFile, 1, string-length($iconFile) - 9)"/>
		</xsl:variable>
		<xsl:variable name="iconStyle">
		    <!--- prepend "icon" -->
			<xsl:value-of select="concat(&apos;icon&apos;, $iconNumber)"/>
		</xsl:variable>
		<xsl:variable name="htmlPath">
			<xsl:value-of select="concat(@xmi:id, &apos;-content.html&apos;)"/>
		</xsl:variable>
		<xsl:variable name="title">
			<xsl:call-template name="json_escape">
				<xsl:with-param name="string" select="@publish:qualifiedname"/>
			</xsl:call-template>
		</xsl:variable>
        {
            title: '<xsl:value-of select="$title" disable-output-escaping="yes"/>',
            id: '<xsl:value-of select="@xmi:id"/>',
            object: '<xsl:value-of select="$htmlPath"/>',
            icon: '<xsl:value-of select="$iconStyle"/>'<xsl:for-each select="./child::*"><xsl:if test="position() = 1"><xsl:text>,
            children: [</xsl:text></xsl:if><xsl:if test="@xmi:id">
                {_reference: '<xsl:value-of select="@xmi:id"/>' }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if>
</xsl:if><xsl:if test="position() = last()"><xsl:text>
            ]</xsl:text></xsl:if></xsl:for-each>
        },
	</xsl:template>
	
	<!-- create an element node -->
	<xsl:template name="createElementNode">
		<xsl:variable name="iconFile">
			<xsl:value-of select="@publish:icon"/>
		</xsl:variable>
		<xsl:variable name="iconNumber">
		    <!--- remove "_icon.png" -->
			<xsl:value-of select="substring($iconFile, 1, string-length($iconFile) - 9)"/>
		</xsl:variable>
		<xsl:variable name="iconStyle">
		    <!--- prepend "icon" -->
			<xsl:value-of select="concat(&apos;icon&apos;, $iconNumber)"/>
		</xsl:variable>
		<xsl:variable name="title">
			<xsl:call-template name="json_escape">
				<xsl:with-param name="string" select="@name"/>
			</xsl:call-template>
		</xsl:variable>

	    <!-- we need to filter out 'appliedProfiles' nodes as they don't carry any page associations -->
		<xsl:if test=
					"name() != 'appliedProfiles' and 
					 name() != 'ancestor' and 
					 name() != 'inheritedAttribute' and 
					 name() != 'inheritedOperation'">
			
			<xsl:variable name="htmlPath">
				<xsl:choose >
					<xsl:when test="
							(@xsi:type = 'uml:Lifeline' )    		or
							(@xsi:type = 'uml:Property' )    		or
							(@xsi:type = 'uml:Port' )    			or
							(@xsi:type = 'uml:Operation')  			or
							(@xsi:type = 'uml:InitialNode') 	    or
							(@xsi:type = 'uml:ActivityFinalNode') 	    or
							(@xsi:type = 'uml:AcceptEventAction') 	    or
							(@xsi:type = 'uml:AcceptCallAction') 	    or
							(@xsi:type = 'uml:ClearAssociationAction') 	or
							(@xsi:type = 'uml:CreateObjectAction') 	    or
							(@xsi:type = 'uml:DestroyObjectAction') 	or
							(@xsi:type = 'uml:CallBehaviorAction') 	    or
							(@xsi:type = 'uml:CallOperationAction') 	or
							(@xsi:type = 'uml:StartObjectBehaviorAction') or
							(@xsi:type = 'uml:SendObjectAction') 	    or
							(@xsi:type = 'uml:SendSignalAction') 	    or
							(@xsi:type = 'uml:ReadLinkAction') 	        or
							(@xsi:type = 'uml:CreateLinkAction') 	    or
							(@xsi:type = 'uml:CreateLinkObjectAction') 	or
							(@xsi:type = 'uml:DestroyLinkAction') 	    or
							(@xsi:type = 'uml:OpaqueAction') 	        or
							(@xsi:type = 'uml:RaiseExceptionAction') 	or
							(@xsi:type = 'uml:ReadExtentAction') 	    or
							(@xsi:type = 'uml:ReadIsClassifiedObjectAction') 	or
							(@xsi:type = 'uml:ReadLinkObjectEndAction') or
							(@xsi:type = 'uml:ReadLinkObjectEndQualifierAction') or
							(@xsi:type = 'uml:ReadSelfAction') 	        or
							(@xsi:type = 'uml:ReclassifyObjectAction') 	or
							(@xsi:type = 'uml:ReduceAction') 	        or
							(@xsi:type = 'uml:ReplyAction') 	        or
							(@xsi:type = 'uml:StartClassifierBehaviorAction') 	or
							(@xsi:type = 'uml:StructuralFeatureAction') or			
							(@xsi:type = 'uml:ClearStructuralFeatureAction') 	or
							(@xsi:type = 'uml:ReadStructuralFeatureAction') 	or
							(@xsi:type = 'uml:WriteStructuralFeatureAction') 	or
							(@xsi:type = 'uml:AddStructuralFeatureValueAction') 	or
							(@xsi:type = 'uml:RemoveStructuralFeatureValueAction') 	or
							(@xsi:type = 'uml:TestIdentityAction') 	    or
							(@xsi:type = 'uml:UnmarshallAction') 	    or
							(@xsi:type = 'uml:ValueSpecificationAction') or
							(@xsi:type = 'uml:ClearVariableAction') 	or
							(@xsi:type = 'uml:ReadVariableAction') 	    or
							(@xsi:type = 'uml:WriteVariableAction') 	or					
							(@xsi:type = 'uml:BehaviorExecutionSpecification')
					               ">
						<xsl:value-of select="concat(../@xmi:id, &apos;-content.html&apos;, '#', @xmi:id)"/>
					</xsl:when>
					<xsl:when test="@publish:toplevelguid = @xmi:id">
						<xsl:value-of select="concat(@xmi:id, &apos;-top-summary.html&apos;)"/>
					</xsl:when>
					<xsl:otherwise>
						<xsl:value-of select="concat(@xmi:id, &apos;-content.html&apos;)"/>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:variable>,
        {
            title: '<xsl:value-of select="$title" disable-output-escaping="yes"/>',
            id: '<xsl:value-of select="@xmi:id"/>',
            object: '<xsl:value-of select="$htmlPath"/>',
            icon: '<xsl:value-of select="$iconStyle"/>'<xsl:for-each select="./child::*"><xsl:if test="position() = 1"><xsl:text>,
            children: [</xsl:text></xsl:if><xsl:if test="@xmi:id">
                <xsl:if test=
					"name() != 'appliedProfiles' and 
					 name() != 'ancestor' and 
					 name() != 'inheritedAttribute' and 
					 name() != 'inheritedOperation'">
                {_reference: '<xsl:value-of select="@xmi:id"/>' }<xsl:if test="position() != last()"><xsl:text>,</xsl:text></xsl:if>
</xsl:if></xsl:if><xsl:if test="position() = last()"><xsl:text>
            ]</xsl:text></xsl:if></xsl:for-each>
        }
		</xsl:if>
	</xsl:template>

	<!-- escape json characters -->
	<xsl:template name="json_escape">
		<xsl:param name="string"/>
		<xsl:variable name="escaped">
            <xsl:call-template name="replaceSubString">
                <xsl:with-param name="theString" select="$string"/>
            <xsl:with-param name="matchSubString">
            	<xsl:text>\</xsl:text>
            </xsl:with-param>
            <xsl:with-param name="replaceWith">
            	<xsl:text>\\</xsl:text>
            </xsl:with-param>
            </xsl:call-template>
		</xsl:variable>
        <xsl:call-template name="replaceSubString">
            <xsl:with-param name="theString" select="$escaped"/>
            <xsl:with-param name="matchSubString">
            	<xsl:text>'</xsl:text>
            </xsl:with-param>
            <xsl:with-param name="replaceWith">
            	<xsl:text>\'</xsl:text>
            </xsl:with-param>
        </xsl:call-template>
	</xsl:template>

	<!-- build the icons.css styles -->
	<xsl:template match="*" mode="icons">
		<xsl:if test="@publish:icon"><xsl:call-template name="createIconStyle"/>
		    <xsl:for-each select="./child::*">
		        <xsl:apply-templates select="." mode="icons"/>
            </xsl:for-each>
		</xsl:if>
	</xsl:template>
	
	<!-- create an icon style -->
	<xsl:template name="createIconStyle">
		<xsl:variable name="iconFile">
			<xsl:value-of select="@publish:icon"/>
		</xsl:variable>
		<xsl:variable name="iconNumber">
		    <!--- remove "_icon.png" -->
			<xsl:value-of select="substring($iconFile, 1, string-length($iconFile) - 9)"/>
		</xsl:variable>
		<xsl:variable name="iconStyle">
		    <!--- prepend "icon" -->
			<xsl:value-of select="concat(&apos;icon&apos;, $iconNumber)"/>
		</xsl:variable>
		<xsl:variable name="iconPath">
			<xsl:value-of select="concat(&apos;../images/&apos;, $iconFile)"/>
		</xsl:variable>
.<xsl:value-of select="$iconStyle"/> {
	background-image: url(<xsl:value-of select="$iconPath"/>);
	background-repeat: no-repeat; 
	width: 16px;
	height: 16px;
}
    </xsl:template>

</xsl:stylesheet>
