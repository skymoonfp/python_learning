//name = "name1"
//
//def Foo():
//    pass
//
//name = "name1"
//var name = "name1"
//
//Foo(null,1);
//
//function Foo(){
//    var arg1 = arguments[0] ? arguments[0] : "skymoon";
//    var arg2 = arguments[1] ? arguments[1] : "666";
//    console.log(arg1);
//    console.log(arg2);
//}
//
//
//function Foo(arg1, arg2){
//    arg1 = arg1 || "skymoon";
//    arg2 = arg2 || "666";
//    console.log(arg1);
//    console.log(arg2);
//}
//
//function Foo(arg1, arg2){
//    if(!arg1){arg1 = "skymoon";}
//    if(!arg2){arg2 = "666";}
//    console.log(arg1);
//    console.log(arg2);
//}
//
//错误
//function Foo(setting){
//    var defaultSetting={
//        arg1:"skymoon",
//        arg2:"666"
//    };
//    .extend(defaultSetting, setting);
//    var a = defaultSetting.arg1;
//    var b = defaultSetting.arg2;
//    console.log(a);
//    console.log(b);
//}
//
//Foo({arg2:"fff"});
//
////自执行函数
//(function(name){
//    console.log(name);
//})("skymoon");
//
//var name = "     skymoon  ";
////alert(name.trim());
////去空格
//console.log(name.trim());
////找字符
//console.log(name.charAt(7));
//console.log(name.trim().charAt(3));
////找子串
//console.log(name.substring(5,9));
//console.log(name.trim().substring(1,5));
////长度
//console.log(name.length);
//console.log(name.trim().length);



