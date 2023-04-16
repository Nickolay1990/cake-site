let tds = document.querySelectorAll('.total');
let sum = document.querySelector('.sum');
let total = 100;

for(let i of tds){
    res = i.textContent.replace(',', '.')
    i.textContent += ' грн'
    total += Number(res)
    }

sum.textContent += total.toFixed(2);
sum.textContent += 'грн';