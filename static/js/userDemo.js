$(function () {
    $("#butt").click(function () {
        addsub();
    });
});

function addsub() {
    var url = '/add/';
    var data = {
        'name':$("#name").val(),
        'pwd':$("#pwd").val()
    };
    if(confirm("确定添加此信息吗?")){
        $.post(url,data,function (result) {
            alert(result)
            window.location.reload()
        });
    }
}

function dele(id) {
    if(confirm('确定要删除吗?')){
        var url = '/dele/';
        var data = {'id': id};
        $.post(url,data,function (result) {
            alert(result);
            window.location.reload();
        });
    }
}

function modi(da) {
    $("#lege").html("修改个人信息");
    console.log(da)
    alert(da.name)
    $("#name").val(da.name)
    $("#pwd").val(da.pwd)
    alert(da);
}