import { routes } from "./utils/routes";



 async function callHealthcheck(){
        try{
            let res = await routes.HEALTHCHECK.API.get()
            console.log(res);
        }catch(err){
            console.log("Error Occured while getting api")
        }
    }
callHealthcheck()