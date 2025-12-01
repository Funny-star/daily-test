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

// 循环分支语句

// while 语句
// var rum = 0
// while (rum < 10){
//     document.writeln("当前的rum的值" + rum)
//     rum++
// }

// dowhile 语句

// var rum = 0
// do {
//     document.writeln("hello"+rum)
//     rum++
// } while(rum < 10)

// var rum = 1
// var result = 0
// do{
//     result += rum
//     rum++
// } while(rum <= 100)
// document.writeln(result)

// for循环
//九九乘法表
// for (var a = 1; a <= 9; a++) {
//     for (var b = 1; b <= a; b++) {
//         var result = a * b;
//         document.writeln("<span>"+b+ "x" +a+"="+result+"</span>");
//     }
//     document.writeln("<br>");
// }


// 函数
// function test(n){
//     if(n === undefined){
//         alert("请传入参数")
//     }
//     for (var a = 1; a <= n; a++) {
//     for (var b = 1; b <= a; b++) {
//         var result = a * b;
//         document.writeln("<span>"+b+ "x" +a+"="+result+"</span>");
//     }
//     document.writeln("<br>");
// }
// }

// test(8)
// test()

// 对象
// 创建对象
// let obj1 = new Object();
// obj1.name = "wxy";
// obj1.age = 19;
// console.log(obj1); // {name: "wxy", age: 19}

// // 增 (Add)
// obj1.gender = "male";           // 添加新属性
// obj1["email"] = "wxy@example.com"; // 另一种添加方式
// console.log(obj1); // {name: "wxy", age: 19, gender: "male", email: "wxy@example.com"}

// // 删 (Delete)
// delete obj1.age;                // 删除属性
// delete obj1["email"];          // 另一种删除方式
// console.log(obj1); // {name: "wxy", gender: "male"}

// // 改 (Update)
// obj1.name = "newName";         // 修改属性值
// obj1["gender"] = "female";     // 另一种修改方式
// console.log(obj1); // {name: "newName", gender: "female"}

// // 查 (Query)
// console.log(obj1.name);        // 访问属性值 - "newName"
// console.log(obj1["gender"]);   // 另一种访问方式 - "female"
// console.log("name" in obj1);   // 检查属性是否存在 - true
// console.log(obj1.hasOwnProperty("name")); // 检查自身属性 - true

// 创建对象
// let obj2 = {
//     name: "wxy",
//     age: 19
// };
// console.log(obj2); // {name: "wxy", age: 19}

// // 增 (Add)
// obj2.gender = "male";
// obj2["hobby"] = "coding";
// console.log(obj2); // {name: "wxy", age: 19, gender: "male", hobby: "coding"}

// // 删 (Delete)
// delete obj2.age;
// delete obj2["hobby"];
// console.log(obj2); // {name: "wxy", gender: "male"}

// // 改 (Update)
// obj2.name = "updatedName";
// obj2["gender"] = "female";
// console.log(obj2); // {name: "updatedName", gender: "female"}

// // 查 (Query)
// console.log(obj2.name);        // "updatedName"
// console.log(obj2["gender"]);   // "female"
// console.log("name" in obj2);   // true
// console.log(obj2.age);         // undefined (属性不存在)
// console.log(Object.keys(obj2)); // 获取所有属性名: ["name", "gender"]
// console.log(Object.values(obj2)); // 获取所有属性值: ["updatedName", "female"]

// // 创建构造函数
// function Person() {
//     this.name = "wxy";
//     this.age = 19;
// }

// // 创建对象
// let obj3 = new Person();
// console.log(obj3); // Person {name: "wxy", age: 19}

// // 增 (Add)
// obj3.gender = "male";
// obj3["country"] = "China";
// console.log(obj3); // Person {name: "wxy", age: 19, gender: "male", country: "China"}

// // 删 (Delete)
// delete obj3.age;
// delete obj3["country"];
// console.log(obj3); // Person {name: "wxy", gender: "male"}

// // 改 (Update)
// obj3.name = "modifiedName";
// obj3["gender"] = "female";
// console.log(obj3); // Person {name: "modifiedName", gender: "female"}

// // 查 (Query)
// console.log(obj3.name);        // "modifiedName"
// console.log(obj3["gender"]);   // "female"
// console.log(obj3 instanceof Person); // true (检查对象类型)
// console.log(Object.getOwnPropertyNames(obj3)); // 获取自身属性: ["name", "gender"]

// // 遍历属性
// for (let key in obj3) {
//     if (obj3.hasOwnProperty(key)) {
//         console.log(`${key}: ${obj3[key]}`);
//     }
// }

