/**
 * Created by zhanlingjie on 2018/8/7.
 */
 var x = document.cookie;
 console.log(x, typeof x);

 if(getCookie('uuid') != '' & getCookie('_puremach')!= ''){
     console.log(getCookie('uuid'),'okoko');
     $.ajax({
                type: 'POST',
                 url:'/user/userinfo',
                 data:{
                      uuid :  getCookie('uuid')
                 },
                 success:function (res) {
                    $('.login').css('display', 'none');
                    console.log(res);
                    if(res.name){

                        $('.user').append(res.name)
                    }
                    else{

                        $('.user').append(res.mobile)

                    }
                    $('.user').val(res)
                 }
             });

 }


 function getCookie(cname)
{
  var name = cname + "=";
  var ca = document.cookie.split(';');
  for(var i=0; i<ca.length; i++)
  {
    var c = ca[i].trim();
    if (c.indexOf(name)==0) return c.substring(name.length,c.length);
  }
  return "";
}