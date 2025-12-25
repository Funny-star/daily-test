// date
// var date = new Date()
// console.log(date)//自动转换为字符串

// 起始时间为1970年1月1号零点零秒
// var datel = new Date(100000)//单位为毫秒
// console.log(datel)

//参数
// var date = new Date(2025, 12, 16, 9, 23, 10)
// console.log(date)

// 字符串
// var date = new Date("2023-10-20 10:10:10")
// console.log(date)

// // 时间对象常用方法
// var date = new Date()
// // 获取
// // getFullYear()
// console.log(date.getFullYear())
// // getMounth()
// console.log(date.getMonth())
// // getDate
// console.log(date.getDate())
// // getDay
// console.log(date.getDay())
// // getHours
// console.log(date.getHours())
// // getMinutes
// console.log(date.getMinutes())
// // getSeconds/getMilliseconds
// console.log(date.getSeconds())
// console.log(date.getMilliseconds())
// // getTime() 时间戳
// console.log(date.getTime())//距离1970.1.1 0：0：0的毫秒数

// // 设置
// console.log(date)
// // 年
// date.setFullYear(2026)
// console.log(date)
// // 月
// date.setMonth(1)
// console.log(date)
// // 日
// date.setDate(1)
// console.log(date)
// // 时
// date.setHours(1)
// console.log(date)
// // 分
// date.setMinutes(1)
// console.log(date)
// // 秒
// date.setSeconds(1)
// console.log(date)
// // 设置时间戳
// date.setTime(1765852707610)
// console.log(date)

// 定时器
// 倒计时 延时执行
// var time1 = setTimeout(function(){
//     console.log("wxy")
// },3000)

// 间隔定时器
// setInterval
// var time2 = setInterval(function(){
//     console.log(new Date())
// },1000)

// 停止定时器
// clearInterval(time2)
// clearTimeout(time1)

// 练习
// const element = document.getElementById('but2')
// but2.onclick = function(){
//     setInterval(function(){
//     console.log(new Date())
//     },1000)
// }


// 结合时间间隔定时器制作倒计时


// function diffTime(current,target){
//     var sub = Math.ceil(target - current)/1000;
//     let day = parseInt(sub/(3600*24));
//     let hours = parseInt(sub%(3600*24)/(3600));
//     let minutes = parseInt(sub%(3600)/60);
//     let seconds = parseInt(sub%60)
//     var obj = {
//         day:day,
//         hours:hours,
//         minutes:minutes,
//         seconds:seconds,
//     };
//     return obj;
// }
// const element = document.getElementById('box')
// var time2 = setInterval(function(){
//     let currentDate = new Date()
//     let targetDate = new Date("2026-1-1")
//     let obj = diffTime(currentDate,targetDate)
//     box.innerHTML = `距离2026年还有${obj.day}
//         天${obj.hours}小时${obj.minutes}
//         分钟${obj.seconds}秒`
// },1000)

// BOM
// 获取浏览器窗口尺寸
// let windowHeight = window.innerHeight;
// console.log(windowHeight);
// let windowWidth = window.innerWidth;x
// console.log(windowWidth)

// alert
// btn.onclick = function(){
//     alert("001")
// }

// setTimeout(function(){
//     alert("缓存清理完毕")
// },2000)

// 询问框
// btn.onclick = function(){
//     let choose = confirm("确定删除吗")
//     console.log(choose)
// }

// 输入框 prompt
// btn.onclick = function(){
//     let name = prompt("请输入你的用户名")
//     alert(`welcome ${name}`)
// }

// 浏览器地址信息
// href 可读可写
// console.log(window.location.href)//window可省
// 中文会被编码，可用decodeURI解码
//跳转页面
// btn.onclick = function(){
//     location.href = "https://www.bilibili.com/"
// }

//reload 从新加载
// btn.onclick = function(){
//     location.reload()
// }

// 浏览器常用事件
// window.onload = function(){
//     console.log("加载完成")
// }
// 在页面中所有元素加载完成过后才会执行

// onresize 改变窗口大小时
// window.onresize = function(){
//     console.log("resize")
// }

// onscroll 窗口滚动时
// window.onscroll = function(){
//     console.log("1")
// }

// window.onscroll = function(){
//     console.log(document.documentElement.scrollTop)
//     console.log(this.document.documentElement.scrollLeft)
// }

// 应用
// window.onscroll = function(){
//     if((document.documentElement.scrollTop) > 1000){
//     console.log("123")
// }else{
//     console.log("")
// }

// }

// 写法一
// btn.onclick = function(){
//     window.scrollTo(0,0)
// }
// 写法二
// btn.onclick = function(){
//     window.scrollTo({
//         left: 0,
//         top: 0
//     })
// }

// 开
// btn.onclick = function(){
//     window.open("http://www.baidu.com")
// }

// 关
// btn.onclick = function(){
//     window.close()
// }

// history
// btn.onclick = function(){
//     location.href = "study2_1.html"
// }

// back_button.onclick = function(){
//     history.back()
//     history.go(-1)
// }

// forward_button.onclick = function(){
//     history.forward()
//     history.go(1)
// }

// 本地存储
// store.onclick = function(){
//     localStorage.setItem("age","200"m)
//     console.log("存储成功")
// }

// get.onclick = function(){
//     console.log(localStorage.getItem("age"))
// }

// del.onclick = function(){
//     localStorage.removeItem("age")
//     console.log("删除成功")
// }

// cle.onclick = function(){
//     localStorage.clear()
//     console.log("清除成功")
// }

// 存取对象要先将对象转化为json格式
// store.onclick = function(){
//     localStorage.setItem("obj",JSON.stringify({name:"wxy",age:"19"}))
// }

// get.onclick = function(){
//     console.log(JSON.parse(localStorage.getItem("obj")))
// }

// sessionStorage 会话存储
// store.onclick = function(){
//     sessionStorage.setItem("obj",JSON.stringify({name:"wxy",age:"19"}))
// }

// get.onclick = function(){
//     console.log(JSON.parse(sessionStorage.getItem("obj")))
// }

// DOM
// 获取节点
// html,head,body 非常规
// console.log(document.documentElement)
// console.log(document.head)//获取head
// console.log(document.body)//获取body

// 常规

// id
// let obox = document.getElementById("box")
// obox.innerHTML = "222"

// class
// let onew = document.getElementsByClassName("new")
// console.log(onew)//伪数组 无法调用部分 数组相关方法

// 遍历
// for (let i = 0; i < onew.length; i++){
//     console.log(`new-${i}-${onew[i]}`)
// }

// 转化为真数组
// let onewArr = Array.from(onew)
// console.log(onewArr.filter)

// name标签名
// getElementsByName 同上

// querySelector 和css选择器规则类似
// let obox = document.querySelector("#box")
// obox.innerHTML = "222"

// querySelectorAll
// let onew = document.querySelectorAll(".new,#box")  

// 元素操作
// 调用元素属性
// let checkedInput = document.getElementById("check")
// checkedInput.onclick = function () {
//     console.log(checkedInput.checked)
// }

// 修改元素属性
// let photo = document.querySelector("img")
// checkedInput.onclick = function () {
//     let ocondition = checkedInput.checked
//     if (checkedInput.checked) {
//         photo.src = "/js-learning/study2/img/OIP-C.jpg"
//         photo.style.display = "block"
//     } else {
//         photo.style.display = "none"
//     }
// }

// 自定义属性

//方法一
// checkedInput.setAttribute("times",0)
// let ocondition = checkedInput.checked
// checkedInput.onclick = function(){
//     if(ocondition !== checkedInput.checked){
//         var times = parseInt(checkedInput.getAttribute("times"))
//         checkedInput.setAttribute("times",++times)
//         ocondition = checkedInput.checked
//         console.log(`你已经点击了${times}次`)
//     }
// }

//方法2
//data-自定义属性
// checkedInput.dataset.times = 0
// checkedInput.onclick = function(){
//     checkedInput.dataset.times++
//     console.log(`你已经点击了${checkedInput.dataset.times}次`)
// }

//练习

// let passwardInput =document.getElementById("passward")
// let eyeInput = document.getElementById("eye")
// passwardInput.type = "password"
// eyeInput.onclick = function(){
//     if(eyeInput.checked){
//         passwardInput.type = "text"
//     }else{
//         passwardInput.type = "password"
//     }
// }

//操作元素文本内容
//innerhtml
// let obox = document.getElementById("box")
// obox.innerHTML = "222"
// //innerText
// console.log(obox.innerText)//获取文本内容不解析HTML内容
// obox.innerText = "<div>333</div>"//设置文本内容不解析HTML内容
// //value
// let oinput = document.querySelector("input")
// console.log(oinput.value)//获取输入框的值
// oinput.value = "hello"//设置输入框的值


//操作元素样式
// .style 只能获取行内属性 --读写
// let box = document.getElementById("box")
// console.log(box.style.width)
// console.log(box.style["background-color"])
// console.log(box.style.backgroundColor)
// 设置
// box.style.width = "200px"
// box.style["background-color"] = "red"
// 内部样式，外部样式，行内样式
// getComputedStyle() 只读
// let boxStyle = getComputedStyle(box)
// console.log(boxStyle.height)
// console.log(boxStyle.backgroundColor)

// 操作元素类名
// className 读写
// let box3 = document.getElementById("box3")
// console.log(box3.className)//获取类名
// box3.className = "item item2"//设置类名
// classList 读写
// console.log(box3.classList)//获取类名列表
// add 添加类名
// box3.classList.add("item2")
// remove 删除类名
// box3.classList.remove("item2")
// toggle 切换类名
// btn3.onclick = function(){
//     box3.classList.toggle("item2")
// }

// 练习 选项卡
// let header = document.querySelectorAll(".header li")
// let text = document.querySelectorAll(".text li")
// let oindex = 0
// let setuation = true
// for (let i = 0; i < header.length; i++) {
//     header[i].dataset.index = i
//     header[i].onclick = backgroundChange
// }


// function backgroundChange(){
//     if (oindex === this.dataset.index&&setuation) {
//         text[oindex].classList.remove("active2")
//         header[oindex].classList.remove("active")
//         setuation = false
//     } else {
//         header[oindex].classList.remove("active")
//         text[oindex].classList.remove("active2")
//         oindex = this.dataset.index
//         header[oindex].classList.add("active")
//         text[oindex].classList.add("active2")
//         setuation = true
//     }
// }