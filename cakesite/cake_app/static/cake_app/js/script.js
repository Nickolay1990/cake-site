let tds = document.querySelectorAll('.total');
let sum = document.querySelector('.sum');
let total = 100;
let link = document.querySelector('#delete-link');


for(let i of tds){
    res = i.textContent.replace(',', '.')
    i.textContent += ' грн'
    total += Number(res)
    }

sum.textContent += total.toFixed(2);
sum.textContent += 'грн';


if(link){
    link.addEventListener('click', del);
}

function del(e){
    conf = window.confirm('Вы уверены что хотите удалить торт?');
    if(!conf){
        e.preventDefault()
    }
}