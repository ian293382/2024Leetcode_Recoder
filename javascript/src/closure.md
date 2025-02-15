# Closure 閉包
1. 為了保存內部變數可藉由外部函數呼叫而進行調整改變
* The Closure function is remembers its a variable even after the outer function has finished executing.

```
#範例
function createCounter() {
    let count = 0 ;
    const addCount = () => {
        count++;
        return count ;
    }
    return addCount; // 重點:回傳第一個addCount 

}

let count = createCount(); // 重點：呼叫外層count 是一個 function addCount() => { count ++}
此時這樣包裝好的函示可以使用
console.log(count()) // 1
console.log(count()) // 2

``` 
此時有更精簡寫法

```
function createCounter() {
    let count = 0 ;
    return () => ++count; // 直接返回箭頭函數
}
const counter = createCounter();
console.log(counter()); // 1
console.log(counter()); // 2

```

第二種才是常用的使用方式
```
var arr = [];
for (var i = 0; i < 5; i +=1) {
  arr[i] = function() {
    return log(i); // => return function log 直接運行下方的 log函數
  }
}

function log(n) {
  // 在此打上你要的運算
  console.log(n);
}

arr[0](); // 0 此時會呼叫 arr函數 ＝ 0
arr[1](); // 1
```

```
const players = ['Player1', 'Player2', 'Player3'];
const scoreHandlers = players.map((player, index) => {
    return {
        addScore: () => {
            console.log(`${player} scored! (Player ${index + 1})`);
        },
        name: player,
        id: index
    };
});
```

```
// 處理 API 資料
function processApiData(apiResponse) {
    return apiResponse
        .filter(item => item.id !== "0")
        .map(item => ({
            id: item.id,
            volume_control: item.volume_control || 30, // 預設音量
            first_name: item.first_name || "None",
            last_name: item.last_name
        }));
}

```
// 音量控制處理器
function createVolumeHandlers(users) {
    return users.map(user => {
        let currentVolume = user.volume_control;
        
        return {
            id: user.id,
            // 取得當前音量
            getVolume: () => currentVolume,
            // 設置音量
            setVolume: (newVolume) => {
                currentVolume = Math.max(0, Math.min(100, newVolume));
                console.log(`${user.first_name}的音量設為: ${currentVolume}`);
                return currentVolume;
            },
            // 增加音量
            increaseVolume: () => {
                return currentVolume = Math.min(100, currentVolume + 10);
            },
            // 降低音量
            decreaseVolume: () => {
                return currentVolume = Math.max(0, currentVolume - 10);
            }
        };
    });
}

// 使用範例
const apiData = [
    { id: "1", volume_control: 50, first_name: "John" },
    { id: "2", volume_control: 30, first_name: "Jane" }
];

const processedData = processApiData(apiData);
const volumeHandlers = createVolumeHandlers(processedData);

// 使用處理器
volumeHandlers.forEach(handler => {
    console.log(`初始音量: ${handler.getVolume()}`);
    handler.increaseVolume();
    console.log(`調高後音量: ${handler.getVolume()}`);
    handler.decreaseVolume();
    console.log(`調低後音量: ${handler.getVolume()}`);
});
```