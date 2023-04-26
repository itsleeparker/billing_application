//This will have all the routes to the current api
import { apiGet } from "./api"
export const routes = {
    "HEALTHCHECK" : {
        "BASEPATH" : "http://localhost:8000/healthcheck" ,
        API :{
            get : async e=>{
                return await apiGet("/" , "healthcheck")
            }
        }   
    }
}