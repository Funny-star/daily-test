// 输出hello world
// alert ("hello world")
// document.writeln("hello world")
// console.log("hello world")

// 变量的类型检测
// var a = 10
// document.writeln(typeof a) // number

// 三元运算符
// 1. 条件 ? 表达式1 : 表达式2
// var a = 2
// a > 5 ? document.writeln("大于5") : document.writeln("小于或等于5")
// 2. 变量 = 条件 ? 表达式1 : 表达式2
// var a = 10
// var b = a > 5 ? "大于5" : "小于或等于5"
// document.writeln(b)

// 三元运算练习(嵌套)
// 满200减10，满100减5
// var a = 300
// var b = a>=200 ? b=a-10 : (a >= 100? b = a - 5 : b = a)
// document.writeln(b)

// if语句
// var a = 100,b
// if(a >= 200){
//     b = a - 10
//     document.writeln(b)
// }
// else if(200 > a && a >= 100){
//     b = a - 5
//     document.writeln(b)
// }
// else{
//     document.writeln(a)
// }

// if-test
// var year = 2016
// if(year % 400 === 0 || (year % 4 === 0 && year % 100 != 0)){ //通过加小括号来保证代码优先级，以此使得逻辑更加通顺
//     document.writeln("是润年")

// }                               
// else{
//     document.writeln("不是润年")
// }

// 优先级判断
// document.writeln(1 || 3 && 2)  数字代表优先级（数字小的优先级高）

// switch语句
// var a = 10 
// switch(a){
//     case 1 :
//         document.writeln("未付款")
//         break
//     case 2 :
//         document.writeln("已付款")
//         break
//     case 3 :
//         document.writeln("已发货")
//         break
//     default :
//         document.writeln("缺货")
//         break
// }

// switch-test
// var money = 200
// switch(true){
//     case money >= 200 :
//         document.writeln(money-10)
//         break
//     case money >= 100 && money < 200:
//         document.writeln(money-5)
//         break
//     case money >= 50 && money < 100:
//         document.writeln(money-3)
//         break
//     default :
//         document.writeln(money)
// }
// 此场景不适合使用switch
// case中尽量不要用运算符（case money >= 200）

// var month = 2
// switch(month){
//     case 1:
//     case 3:
//     case 5:
//     case 7:
//     case 8:
//     case 10:
//     case 12:
//         document.writeln("31daies")
//         break
//     case 2:
//         document.writeln("28daies")
//         break
//     default :
//         document.writeln("30daies")
//         break
// }

// var score = 100
// var flagScore = parseInt(score/10)
// switch (flagScore){
//     case 5:
//     case 4:
//         document.writeln("1")
//         break
//     case 3:
//     case 2:
//         document.writeln("2")
//         break
//     case 1:
//         document.writeln("3")
//         break
//     default:
//         document.writeln(false)
//         break
// }

