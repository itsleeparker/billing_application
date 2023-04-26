//This file will only have all the api end points handling
import $ from "jquery";
export async function apiGet(url , basepath){
    let validUrl = BASE_PATHS[basepath]
    if(! validUrl){
        return 
    }
    let completeUrl = validUrl + url;
    try{
        return new Promise((resolve , reject)=>{
            fetch(completeUrl , {
                method : "GET"  , 
            })
            .then(Response=>{
                resolve(Response.json())
            })
            .catch(err=>{
                //Handle here exception handling 
            })
        })
    }
    catch(err){
        console.log("Error Occured " , err);
        return null
    }
}

export async function apiPost(url , data , bastpath){
    let validUrl  = BASE_PATHS[bastpath];
    if(!validUrl){
        return
    }
    let completeUrl = validUrl + url;
    return new Promise((resolve , reject)=>{
        fetch(completeUrl , {
            method : "POST" , 
            headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
              },
            body : JSON.stringify(data)
        })
    })
}   

export async function apiPut(url , data , bastpath){
    let validUrl  = BASE_PATHS[bastpath];
    if(!validUrl){
        return
    }
    let completeUrl = validUrl + url;
    return new Promise((resolve , reject)=>{
        fetch(completeUrl , {
            method : "PUT" , 
            headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
              },
            body : JSON.stringify(data)
        })
    })
}   

export async function apiDelete(url , data , bastpath){
    let validUrl  = BASE_PATHS[bastpath];
    if(!validUrl){
        return
    }
    let completeUrl = validUrl + url;
    return new Promise((resolve , reject)=>{
        fetch(completeUrl , {
            method : "DELETE" , 
            headers: {
                "Content-Type": "application/json",
                // 'Content-Type': 'application/x-www-form-urlencoded',
              },
            body : JSON.stringify(data)
        })
    })
}   


const BASE_PATHS = {
    "healthcheck" : "http://localhost:8000/healthcheck"
}