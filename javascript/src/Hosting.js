import React, { useState } from 'react';

const Hoisting = () => {
 const [number, setNumber] = useState(10);
 const [result, setResult] = useState(null);

 function isEven(n) {
   if (n === 0) return true;
   return isOdd(n - 1);
 }

 function isOdd(n) {
   if (n === 0) return false;
   return isEven(n - 1);
 }

 const handleCheck = () => {
   const result = isEven(number);
   setResult(result);
 };

 return (
   <div style={{ padding: '20px' }}>
     <input
       type="number"
       value={number}
       onChange={(e) => setNumber(parseInt(e.target.value) || 0)}
     />
     <button onClick={handleCheck}>檢查是否為偶數</button>
     
     {result !== null && (
       <p>
         {number} 是 {result ? '偶數' : '奇數'}
       </p>
     )}
   </div>
 );
};

export default Hoisting;