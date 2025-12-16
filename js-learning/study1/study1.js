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

// 存储
// 互相影响 ,并非真正的复制
// var obj = {
//     name:"123",
//     age:"1234"
// }
// var obj2 = obj
// document.writeln(obj2.name)

// 不影响
// var obj = {
//     name:"123",
//     age:"1234"
// };

// var obj2 = {};

// for(var i in obj){
//     obj2[i] = obj[i];
// };
// obj2.name = "12345"
// console.log(obj,obj2);


// 数组
// var arr = [1 ,"hahaha",{
//     name:"wxy",
//     age:18
// }];

// for(var i in arr){
//     console.log(arr[i]);
// };

// // length 可读可写
// var arr = [1,2,3,4,5]
// console.log(arr.length);

// // 清空数组
// arr.length = 0;
// console.log(arr);

// 索引
// console.log(arr[0]);
// arr[0] = 10;
// console.log(arr[0]);
// arr[10] = 1
// console.log(arr)

// 遍历
// for(var i = 0; i < arr.length; i++){
//     console.log(arr[i])
// }

// 复制
// arr2 = []
// for(var i in arr){
//     arr2[i] = arr[i];
// }
// console.log(arr2)


// let arr = [30, 29, 28, 37, 14, 10]
// // 冒泡排序
// for (var j = arr.length; j > 0; j--) {
//     for (var i = 0; i < arr.length; i++) {
//         if (arr[i] > arr[i + 1]) {
//             var item = arr[i]
//             arr[i] = arr[i + 1]
//             arr[i + 1] = item
//         }
//     }
// }
// console.log(arr)

// 选择排序
// for(var i = 0; i < arr.length; i++){
//     var item = arr[i];
//     var key_item = i;
//     for(var j = i+1 ; j <= arr.length; j++){
//         if(item > arr[j]){
//             var key_item = j
//         };
//     };
//     arr[i] = arr[key_item];
//     arr[key_item] = item;
// };
// console.log(arr);

// 数组操作
// var arr = [11, 10, 0, 5];
// var arr2 = [13, 16, 19];
// // push 在数组后面追加元素
// var res = arr.push(7);
// console.log(arr);
// // 返回值 追加后的长度
// console.log(res);

// //pop 后面删除元素
// var res2 = arr.pop();
// console.log(arr);
// // 返回值 删除的元素
// console.log(res2);

// //unshift 从前面加元素
// var res3 = arr.unshift(10);
// console.log(arr);
// // 返回值为添加后长度
// console.log(res3);

// //shift 从前面删除
// var res4 = arr.shift();
// console.log(arr);
// //返回值为删除的数据
// console.log(res4);

// // splice 删除
// var res5 = arr.splice(1, 1);
// console.log(arr);
// // 返回值为删除的值
// console.log(res5);

// // splice 添加
// var res6 = arr.splice(1, 0, 10);
// console.log(arr);
// // 返回值为删除的值
// console.log(res6);


// // reverse 倒叙
// arr.reverse();
// console.log(arr);


// // sort 排序
// // 一位一位排
// arr.sort();
// console.log(arr);

// // sort接受一个回调函数
// arr.sort(function(a,b){
//     return b-a
// });
// console.log(arr);

// concat 拼接
// var arr3 = arr.concat(arr2);//拼接的数组是concat的返回值
// console.log(arr,arr2,arr3);

// 也可用于复制
// var arr4 = arr.concat();

// join 数组 => 字符串
// document.writeln(arr.join("L "))

// 练习
// var arr = []
// for(var i = 0; i < 10; i++){
//     arr.push("<li>"+i+"</li>")
// }
// document.writeln(arr.join(" "))//去除数组的，

// // slice 截取(开始索引，结束索引)
// var arr = ["aaa", "bbb", "ccc", "ddd"]
// var arr2 = arr.slice(1,3)
// console.log(arr,arr2)
// var arr3 = arr.slice(1,-1)
// console.log(arr,arr3)
// // 与splice的区别是splice会改变原数组，而slice不会
// // 与concat一样可以用于复制

// // indexof 返回查找的索引值（返回-1时找不到）
// var arr = ["aaa", "bbb", "ccc", "ddd", "aaa"]
// var res = arr.indexOf("aaa")
// console.log(res)
// // 查找重复元素时，返回找到的第一个元素的值

// // lastIndexof 从后向前返回查找的索引值（返回-1时找不到）
// var arr = ["aaa", "bbb", "ccc", "ddd", "aaa"]
// var res = arr.lastIndexOf("aaa")
// console.log(res)
// // 查找重复元素时，返回找到的第一个元素的值

// 数组去重
// var arr = ["aaa", "bbb", "bbb", "ccc", "ddd", "aaa"]
// 方法一

// var arr2 = []
// for(var i in arr){
//     if(arr2.indexOf(arr[i]) == -1){
//         arr2.push(arr[i])
//     }
// }
// console.log(arr,arr2)

// 方法2
// var arr2 = []
// var obj = {}
// for(var i in arr){
//     obj[arr[i]] = arr[i];
// }    
// for(var i in obj){
//     arr2.push(obj[i])
// }
// console.log(arr2)

// // 方法三 new-set
// var set1 = new Set(arr)
// var arr1 = Array.from(set1)
// console.log(arr1)

// forEach 遍历
// var arr = ["aaa","bbb","ccc"];
// arr.forEach(function(item,index,arr){
//     console.log(item,index,arr)
// })

// map 映射
// var arr = [1 ,2 ,3 ,4];
// var arr2 = arr.map(function(item){
//     return item*item;
// })
// console.log(arr , arr2)

// 练习
// var arr = ["aaa", "bbb", "ccc"];
// var arr2 = arr.map(function (item) {
//     return "<li>" + item + "</li>";
// })
// console.log(arr2)
// document.writeln(arr2.join(""));

// filter 过滤
// var arr = [1 ,2 ,3 ,4];
// var arr2 = arr.filter(function(item){
//     return item >= 3;
// })

// console.log(arr2);

// var arr = [
//     {
//         name:"aaa",
//         price:100
// },
//     {
//         name:"bbb",
//         price:200
// },
//     {
//         name:"ccc",
//         price:300
// },
// ]
// var arr2 = arr.filter(function(item){
//     return item.price >= 200;
// })
// console.log(arr2);


// every 每一个 会返回boor值
// var arr = [10, 20, 30, 40]
// var arr2 = arr.every(function(item){
//     return item <= 50;
// })
// console.log(arr2)

// some 有一个以上 会返回boor值
// var arr = [10, 20, 30, 40]
// var arr2 = arr.some(function(item){
//     return item <= 20;
// })
// console.log(arr2)

// find 重复只找第一项
// var arr = [
//         {
//         name:"语文",
//         grade:100
//     },
//         {
//         name:"数学",
//         grade:100
//     },
//         {
//         name:"英语",
//         grade:100
//     }
// ]
// var arr2 = arr.find(function(item){
//     return item.grade === 100;
// })
// console.log(arr2)

// reduce 叠加
// var arr = [1, 2, 3, 4]
// var arr2 = arr.reduce(function(prev,item){
//     return prev+item;
// },100)//100为初始值
// console.log(arr2)



// 字符串
// var str1 = "123"
// var str2 = new String("123")
// console.log(str1,str2)
// console.log(str1.length)

// charAt（索引） 返回索引的字符
// var str1 = "12345456"
// console.log(str1.charAt(4))


// charCodeAt  返回对应字符的ASCLL编码
// var str1 = "12345456"
// console.log(str1.charCodeAt(4))

// 输出字母表
// var arr = [];
// for(var i = 65; i < 91; i++){
//     console.log(String.fromCharCode(i));
//     arr.push(String.fromCharCode(i));
// }
// console.log(arr);

// toUpperCase() toLowerCase()   转换大小写
// var str1 = "hellow";
// var str2 = 'HELLOW'
// console.log(str1.toUpperCase())
// console.log(str2.toLowerCase())

// 截取  substr   substring   slice
// var str = "123456"
// var str1 = str.substring(2, 5)//开始索引和结束索引，当第二个值小于第一个值时令算
// var str2 = str.slice(1 ,2)//开始索引和结束索引
// console.log(str1,str2)

// replace
// var str = "abdkhsj";
// var str1 = str.replace("a", "*");
// console.log(str1);

// split 分割 join
// var str = "a|b|c|d"
// console.log(str.split("|"))

// trim 去除首尾部空格
// trimStart() trimRight或 trimEnd() trimLeft去除首或尾部空格
// var str = "    hellow    world    "
// console.log("|"+str.trim()+"|")

// 模糊查询
// var arr = ["aaa", "bbb", "ccc", "abcd", "cbd"]
// var imput = prompt("亲输入查询内容")
// var result = arr.filter(function(item){
//      return item.indexOf(imput) > -1
// })
// document.writeln(result.join("|"))

// json字符串
// var str1 = '{"name":"wxy", "age":"123"}'
// console.log(JSON.parse(str1))
// var obj1 = {
//     name:"wxy",
//     age:19
// }
// console.log(JSON.stringify(obj1))

// 模板字符串
// var str = `<li>1</li>
// <li>1</li>
// <li>1</li>`
// document.writeln(str)

// var myname = "wxy"
// var str = `my name is ${myname} ${10+20}`//也可以是三目表达式
// document.writeln(str)    