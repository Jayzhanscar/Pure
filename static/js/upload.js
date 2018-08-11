/**
 * Created by zhanlingjie on 2018/8/8.
 */

function getCookie(cname)
{
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++)
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) {
        return c.substring(name.length, c.length);
    }
  }
  return "";
}


function imgPreview(fileDom){
            //判断是否支持FileReader
            if (window.FileReader) {
                var reader = new FileReader();
            } else {
                mui.alert("您的设备不支持图片预览功能，如需该功能请升级您的设备！");
            }

            //获取文件
            var file = fileDom.files[0];
            console.log(file);
            var imageType = /^image\//;
            //是否是图片
            if (!imageType.test(file.type)) {
                mui.alert("请选择图片！");
                return;
            }
         if($('#title').val() != ''){
            var file_pic = new FormData();
            file_pic.append('file',file);
            file_pic.append('title',$('#title').val());

            //上传图片

                 $.ajax({
                url:'/material/api/img',
                type:'POST',
                data:file_pic,
                processData : false,
                 // 告诉jQuery不要去设置Content-Type请求头
                 contentType : false,
                success:function (res) {
                    mui.alert('发表成功');
                    console.log(res)
                }

            });
             }
             else{
                 mui.alert('请先写标题')
             }
            //读取完成
            // reader.onload = function(e) {
            //     //获取图片dom
            //     var img = document.getElementById("preview");
            //     //图片路径设置为读取的图片
            //     img.src = e.target.result;
            //
            // };
            // reader.readAsDataURL(file);
        }

function VideoPreview(fileDom){
            //判断是否支持FileReader
            if (window.FileReader) {
                var reader = new FileReader();
            } else {
                mui.alert("您的设备不支持图片预览功能，如需该功能请升级您的设备！");
            }

            //获取文件
            var file = fileDom.files[0];
            console.log(file);
         if($('#title2').val() != ''){
            var file_pic = new FormData();
            file_pic.append('file',file);
            file_pic.append('title',$('#title2').val());

            //上传图片

                 $.ajax({
                url:'/material/api/video',
                type:'POST',
                data:file_pic,
                processData : false,
                 // 告诉jQuery不要去设置Content-Type请求头
                 contentType : false,
                success:function (res) {
                    mui.alert('上传成功')
                    console.log(res)
                }

            });
             }
             else{
                 mui.alert('请先写标题')
             }
            //读取完成
            // reader.onload = function(e) {
            //     //获取图片dom
            //     var img = document.getElementById("preview");
            //     //图片路径设置为读取的图片
            //     img.src = e.target.result;
            //
            // };
            // reader.readAsDataURL(file);
        }

function ArticlePreview(){
            //判断是否支持FileReader
         if($('#title1').val() != '' & $('#teat').val() != ''){

                 $.ajax({
                url:'/material/api/article',
                type:'POST',
                data: {
                    'title': $('#title1').val(),
                    'content': $('#teat').val()
                },
                success:function (res) {
                    mui.alert('发表成功')
                }

            });
             }
             else{
                 mui.alert('请先写标题')
             }
            //读取完成
            // reader.onload = function(e) {
            //     //获取图片dom
            //     var img = document.getElementById("preview");
            //     //图片路径设置为读取的图片
            //     img.src = e.target.result;
            //
            // };
            // reader.readAsDataURL(file);
        }