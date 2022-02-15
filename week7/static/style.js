function searchName(){
    let username = document.getElementById("name")
    username = username.value;
    let result = document.getElementById("result");
    result.innerHTML = "";
    web("http://127.0.0.1:3000/api/members?username="+username)
};
async function web(url){
    try{
        let getData = await fetch(url);
        getData = await getData.json();
        let name = getData["data"]["name"];
        result.innerText = name;
        result.setAttribute("class","text");
    }
    catch(error){
        result.innerText = "查無此人";
        result.setAttribute("class","text");
    }
}
function changeName(){
    let newname = document.getElementById("newname");
    newname = newname.value;
    newName(newname);
    let success = document.getElementById("success");
    success.innerHTML = "";
}
async function newName(newname){
    try{
        let response = await fetch(
            "http://127.0.0.1:3000/api/member",{
            method:"POST",
            headers:{"Content-Type": "application/json"},
            body:JSON.stringify({"name":newname}),
        });
        let data = await response.json();
        console.log(data)
        if (data["ok"]){
            success.innerHTML = "更新成功" ;
            success.setAttribute("class","text");
        }
    }
    catch(error){
        console.log("catach",error)
    }
}
