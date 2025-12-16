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
