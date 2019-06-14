function Enter(id_) {
    var id = document.getElementById(id_);
    id.className = "redYellow";

    if (id.value == "请输入搜索内容" || id.value.trim() == "") {
        id.value = "";
    }

}

function Leave(id_) {
    var id = document.getElementById(id_);
    var val = id.value;
    if (val.length == 0 || val.trim() == "") {
        id.value = "请输入搜索内容";
        id.className = "greyWhite";
    }else{
        id.className = "blackYellow";
    }
}