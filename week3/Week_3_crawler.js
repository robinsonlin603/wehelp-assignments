function toggleMenu(){
    let menu=document.getElementById("menu");
    if(menu.style.display=="none"){
        menu.style.display="block";
    }else{
        menu.style.display="none";
    }
}
let request=new XMLHttpRequest();
let container = document.getElementById("low-1");
request.onload=function(){
    let response=request.responseText;
    let responseObj=JSON.parse(response);
    list=responseObj.result.results;
    for (let i=0;i<8;i++){
        let pics=list[i].file.toLowerCase();
        let pic=pics.split("jpg",1);
        pic=pic+"jpg";
        text=list[i].stitle;
        let div=document.createElement("div");
        div.setAttribute("class","Image")
        let img=document.createElement("img");
        img.setAttribute("src",pic);
        img.setAttribute("class","photo");
        let span=document.createElement("span");
        span.innerText=text;
        div.appendChild(img);
        div.appendChild(span);
        container.appendChild(div);
    }
}
request.open("get","https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
request.send();
let n=0;
function init(){
    let btn=document.getElementById("btn");
    let handler2=function(){
        n+=8;
    }
    let handler=function(){
        let request=new XMLHttpRequest();
        let container = document.getElementById("low-1");
        request.onload=function(){
            let response=request.responseText;
            let responseObj=JSON.parse(response);
            list=responseObj.result.results;
            for (let i=n;i<n+8;i++){
                let pics=list[i].file.toLowerCase();
                let pic=pics.split("jpg",1);
                pic=pic+"jpg";
                text=list[i].stitle;
                let div=document.createElement("div");
                div.setAttribute("class","Image")
                let img=document.createElement("img");
                img.setAttribute("src",pic);
                img.setAttribute("class","photo");
                let span=document.createElement("span");
                span.innerText=text;
                div.appendChild(img);
                div.appendChild(span);
                container.appendChild(div);
            }
        }
        request.open("get","https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
        request.send();        
    };
    btn.addEventListener("click",handler); 
    btn.addEventListener("click",handler2);
};
