<%--
  Created by IntelliJ IDEA.
  User: LiveAn
  Date: 2018/3/31
  Time: 10:54
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>定义input type="file" 的样式</title>
    <style type="text/css">
        body{ font-size:14px;}
        input{ vertical-align:middle; margin:0; padding:0}
        .file-box{ position:relative;width:345px}
        .text{text-align: right; height:22px; vertical-align: middle; font-weight: bold; font-size: medium;color: #6f92ed;width:105px;}
        .txt{ height:22px; border:1px solid #cdcdcd; width:180px;}
        .btn{ background-color:#FFF; border:1px solid #CDCDCD;height:24px; width:70px;}
        .file{ position:absolute; top:0; right:90px; height:24px; filter:alpha(opacity:0);opacity: 0;width:255px }
    </style>
</head>

<body>
<p class="text">上传单个文件:</p>
<div class="file-box">
    <form method="post" action="uploadFile" enctype="multipart/form-data">
        <input type='button' class='btn' value='浏览...' />
        <input type='text' name='fileTextField' id='fileTextField' class='txt' />
        <input type="file" name="fileField" class="file" id="fileField" size="28"/>
        <input type="submit" name="submit" class="btn" id = "fileSubmit" value="上传" disabled="true" />
    </form>
</div>

<p class="text">上传文件夹:</p>
<div class="file-box">
    <form method="post" action="uploadFolder" enctype="multipart/form-data">
        <input type='button' class='btn' value='浏览...' />
        <input type='text' name='folderTextField' id='folderTextField' class='txt' />
        <input type="file" name="folderField" class="file" webkitdirectory multiple  id="folderField" size="28"/>
        <input type="submit" name="submit" class="btn" id = "folderSubmit" value="上传" disabled="true"/>
    </form>
</div>
</body>


<script type="text/javascript" src="/js/jquery-3.2.1.min.js"></script>
<script type="text/javascript" >
    document.getElementById("fileField").addEventListener("change", function(event) {
        var fileInfo = $("#fileField").val();
        if(fileInfo!="") {
            var index =fileInfo.lastIndexOf("\\");
            var name = fileInfo.substr(index + 1);
            $("#fileTextField").attr("value", name);
            $("#fileSubmit").attr("disabled", false);
        }
    }, false);

    document.getElementById("folderField").addEventListener("change", function(event) {
        var files = $(this).val();
        if(files!=""){
            var filesList = event.target.files;
            var filesCount = filesList.length;
            var filesRoot = filesList[0].name;
            $("#folderTextField").attr("value",filesRoot +" 等共" + filesCount.toString()+"个文件");
            $("#folderSubmit").attr("disabled", false);
        }
    }, false);

</script>

</html>
