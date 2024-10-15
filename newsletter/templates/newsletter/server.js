const express = require('express')
const mongoose = require('mongoose')
const path = require('path')
const port = 4040

const app = express()
app.use(express.static(__dirname))
app.use(express.urlencoded({extended:true}))

mongoose.connect('mongodb://127.0.0.1:27017/newsubmit')
const db = mongoose.connection
db.once('open',()=>{
    console.log("Mongodb connection successful")
})

const userSchema = new mongoose.Schema({
    title:String,
    content:String
})

const Users = mongoose.model("data",userSchema)

app.get('/',(req,res)=>{
    res.sendFile(path.join(__dirname,'submit_article.html'))
})
app.post('/post',async(req,res)=>{
    const {title,content} = req.body
    const user = new Users({
        title,
        content
    })
    await user.save()
    console.log(user)
    res.sendFile(path.join(__dirname,'success.html'))
})
app.listen(port,()=>{
    console.log("server started")
})