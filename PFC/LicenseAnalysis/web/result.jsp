<%--
  Created by IntelliJ IDEA.
  User: LiveAn
  Date: 2018/3/12
  Time: 10:48
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>reslt</title>
</head>
<body>
<%
    String uploadInfo = (String)request.getAttribute("uploadInfo");
    String licenseInfo = (String)request.getAttribute("licenseInfo");
%>
<p>
    upload information：<%=uploadInfo%>
</p>

<p>
    license information：<%=licenseInfo==null?"unclear":licenseInfo%>
</p>

</body>
</html>
