const path = require("path")

const entryPath = path.join(__dirname , "app" , "static" , "JS")
module.exports = {
    entry :  entryPath + "/main.js" , 
    output : {
        filename : 'bundel.js',
        path : path.resolve(__dirname ,"./app/static/dist")
    }
}